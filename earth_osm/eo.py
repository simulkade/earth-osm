__author__ = "PyPSA meets Earth"
__copyright__ = "Copyright 2022, The PyPSA meets Earth Initiative"
__license__ = "MIT"

"""
This is the principal module of the earth_osm project.
"""

import logging
import os

import pandas as pd

# suppress pandas warning about fragmented dataframes
# TODO: do not suppress warnings
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# from earth_osm.config import primary_feature_element, feature_columns
from earth_osm.filter import get_filtered_data
from earth_osm.gfk_data import get_region_tuple, view_regions
from earth_osm.utils import OutFileWriter, lonlat_lookup, way_or_area

logger = logging.getLogger("osm_data_extractor")
logger.setLevel(logging.INFO)

def process_region(region, primary_name, feature_name, mp, update, data_dir):
    """
    Process Country

    Args:
        region: Region object
        primary_name: Primary Feature Name
        feature_name: Feature Name
        mp: Multiprocessing object
        update: Update flag

    Returns:
        None
    """
    primary_dict, feature_dict = get_filtered_data(region, primary_name, feature_name, mp, update, data_dir)

    primary_data = primary_dict['Data']
    feature_data = feature_dict['Data']

    df_node = pd.json_normalize(feature_data["Node"].values())
    df_way = pd.json_normalize(feature_data["Way"].values())

    if df_way.empty:
        logger.debug(f"df_way is empty for {region.short}, {primary_name}, {feature_name}")
        # for df_way, check if way or area
    else:
        type_col = way_or_area(df_way)
        df_way.insert(1, "Type", type_col)
        logger.debug(df_way['Type'].value_counts(dropna=False))

        # Drop rows with None in Type
        logger.debug(f"Dropping {df_way['Type'].isna().sum()} rows with None in Type")
        df_way.dropna(subset=["Type"], inplace=True)

        # convert refs to lonlat
        lonlat_column = lonlat_lookup(df_way, primary_data)
        df_way.insert(1, "lonlat", lonlat_column)

    # check if df_node is empty
    if df_node.empty:
        logger.debug(f"df_node is empty for {region.short}, {primary_name}, {feature_name}")
    else:
        # df node has lonlat as [lon, lat] it should be [(lon, lat)]
        df_node["lonlat"] = df_node["lonlat"].apply(lambda x: [tuple(x)])
        
        # set type to node
        df_node["Type"] = "node"
    
    # concat ways and nodes
    df_feature = pd.concat([df_way, df_node], ignore_index=True)

    # remove columns that are all nan
    df_feature.dropna(axis=1, how="all", inplace=True)

    if df_feature.empty:
        logger.debug(f"df_feature is empty for {region.short}, {primary_name}, {feature_name}")
    else:
        df_feature.insert(3, 'Region', region.short)
        
    return df_feature

def get_osm_data(
        region_str,
        primary_name,
        feature_name,
        cached,
):
    region_tuple = get_region_tuple(region_str)
    mp = True
    update = cached
    data_dir=os.path.join(os.getcwd(), 'earth_data')
    
    df = process_region(
        region_tuple,
        primary_name,
        feature_name,
        mp,
        update,
        data_dir
    )

    # TODO: improve get_osm_data funciton with post processing
    return df
    


# TODO: Plan
# Use an intermediary super efficient file format such as parquet
# save a region,feauture pair in temp files
# implement planetary file from osm (https://planet.openstreetmap.org/)
# read keys, values, tags and their frequencies from taginfo api (https://taginfo.openstreetmap.org/taginfo/apidoc)
# use **kwargs and allow for dropping of refs column
# implement post processing functions: i) create_geojson 2) filter_by_bbox


def save_osm_data(
    region_list=['germany'],
    primary_name='power',
    feature_list=['tower'],
    update=False,
    mp=True, # TODO: remove mp arg
    data_dir=os.path.join(os.getcwd(), 'earth_data'),
    out_format="csv", # TODO: rename out_format -> format
    out_aggregate=True, # TODO: rename out_aggregate -> aggregate
):
    """
    Get OSM Data for a list of regions and features
    args:
        region_list: list of regions to get data for
        primary_name: primary feature to get data for
        feature_list: list of features to get data for
        update: update data
        mp: use multiprocessing
    returns:
        dict of dataframes
    """
    region_tuple_list = [get_region_tuple(r) for r in region_list]
    region_short_list = [r.short for r in region_tuple_list]

    if out_aggregate == 'region' or out_aggregate is True:
        # for each feature, aggregate all regions
        for feature_name in feature_list:
            with OutFileWriter(region_short_list, [feature_name], data_dir, out_format) as writer:
                for region in region_tuple_list:
                    df_feature = process_region(region, primary_name, feature_name, mp, update, data_dir)
                    writer(df_feature)
                    # output_creation(df_feature, primary_name, [feature_name], region_short_list, data_dir, out_format)

    elif out_aggregate == 'feature':
        # for each region, aggreagate all features
        for region in region_tuple_list:
            with OutFileWriter([region.short], feature_list, data_dir, out_format) as writer:
                for feature_name in feature_list:
                    df_feature = process_region(region, primary_name, feature_name, mp, update, data_dir)
                    writer(df_feature)
    
    elif out_aggregate is False:
        # no aggregation, one file per region per feature
        for region in region_tuple_list:
                for feature_name in feature_list:
                    df_feature = process_region(region, primary_name, feature_name, mp, update, data_dir)
                    with OutFileWriter([region.short], [feature_name], data_dir, out_format) as writer:
                        writer(df_feature)


    # combinations = ((region, feature_name) for region in region_tuple_list for feature_name in feature_list)

    # processed_data = map(lambda combo: process_region(combo[0], primary_name, combo[1], mp, update, data_dir), combinations)

    # for i, combo in enumerate(combinations):
    #     output_creation(processed_data[i], primary_name, combo[1], [combo[0]], data_dir, out_format, out_aggregate)

