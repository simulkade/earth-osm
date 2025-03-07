<!-- markdownlint-disable -->

# API Overview

## Modules

- [`args`](./args.md#module-args)
- [`config`](./config.md#module-config)
- [`eo`](./eo.md#module-eo)
- [`extract`](./extract.md#module-extract)
- [`filter`](./filter.md#module-filter)
- [`gfk_data`](./gfk_data.md#module-gfk_data)
- [`gfk_download`](./gfk_download.md#module-gfk_download)
- [`osmpbf`](./osmpbf.md#module-osmpbf)
- [`utils`](./utils.md#module-utils)

## Classes

- [`osmpbf.Node`](./osmpbf.md#class-node): Node(id, tags, lonlat)
- [`osmpbf.Relation`](./osmpbf.md#class-relation): Relation(id, tags, members)
- [`osmpbf.Way`](./osmpbf.md#class-way): Way(id, tags, refs)
- [`utils.OutFileWriter`](./utils.md#class-outfilewriter)

## Functions

- [`args.main`](./args.md#function-main): The main function executes on commands:
- [`eo.get_osm_data`](./eo.md#function-get_osm_data)
- [`eo.process_region`](./eo.md#function-process_region): Process Country
- [`eo.save_osm_data`](./eo.md#function-save_osm_data): Get OSM Data for a list of regions and features
- [`extract.filter_file_block`](./extract.md#function-filter_file_block)
- [`extract.filter_pbf`](./extract.md#function-filter_pbf): Parallized pre-Filtering of OSM file by a pre_filter
- [`extract.id_filter`](./extract.md#function-id_filter)
- [`extract.pool_file_query`](./extract.md#function-pool_file_query): returns query function that accepts a filter function and returns a list of filtered entries
- [`extract.primary_entry_filter`](./extract.md#function-primary_entry_filter)
- [`extract.way_filter`](./extract.md#function-way_filter)
- [`filter.feature_filter`](./filter.md#function-feature_filter)
- [`filter.get_filtered_data`](./filter.md#function-get_filtered_data)
- [`filter.run_feature_filter`](./filter.md#function-run_feature_filter)
- [`filter.run_primary_filter`](./filter.md#function-run_primary_filter)
- [`gfk_data.get_all_regions_dict`](./gfk_data.md#function-get_all_regions_dict): It takes a level argument, and returns a dictionary of all regions, grouped by their parent region
- [`gfk_data.get_all_valid_list`](./gfk_data.md#function-get_all_valid_list): Returns a list of all valid region ids
- [`gfk_data.get_code_by_id`](./gfk_data.md#function-get_code_by_id): Takes a region id (eg. germany) and returns its code (eg. DE)
- [`gfk_data.get_geom_sitemap`](./gfk_data.md#function-get_geom_sitemap)
- [`gfk_data.get_id_by_code`](./gfk_data.md#function-get_id_by_code): Takes a region code (eg. DE) and returns its id (eg. germany)
- [`gfk_data.get_id_by_str`](./gfk_data.md#function-get_id_by_str): Takes a region id or code (eg. DE, germany) and returns its id (eg. germany)
- [`gfk_data.get_region_dict`](./gfk_data.md#function-get_region_dict): Takes a region id (eg. germany) and returns a ditctionary consisting of
- [`gfk_data.get_region_tuple`](./gfk_data.md#function-get_region_tuple): Takes a region id or code (eg. DE, germany) and returns a named tuple with 
- [`gfk_data.get_root_list`](./gfk_data.md#function-get_root_list): Returns a list of regions without parents (i.e continents)
- [`gfk_download.download_pbf`](./gfk_download.md#function-download_pbf)
- [`gfk_download.download_sitemap`](./gfk_download.md#function-download_sitemap)
- [`gfk_download.earth_downloader`](./gfk_download.md#function-earth_downloader): Download file from url to dir
- [`utils.columns_melt`](./utils.md#function-columns_melt)
- [`utils.convert_pd_to_gdf`](./utils.md#function-convert_pd_to_gdf)
- [`utils.convert_ways_lines`](./utils.md#function-convert_ways_lines): Convert Ways to Line Coordinates
- [`utils.convert_ways_points`](./utils.md#function-convert_ways_points): Convert Ways to Point Coordinates
- [`utils.convert_ways_polygons`](./utils.md#function-convert_ways_polygons): Convert Ways to Polygon and Point Coordinates
- [`utils.get_list_slug`](./utils.md#function-get_list_slug)
- [`utils.lonlat_lookup`](./utils.md#function-lonlat_lookup): Lookup refs and convert to list of longlats
- [`utils.output_creation`](./utils.md#function-output_creation): Save Dataframe to disk
- [`utils.tags_explode`](./utils.md#function-tags_explode)
- [`utils.tags_melt`](./utils.md#function-tags_melt)
- [`utils.way_or_area`](./utils.md#function-way_or_area)
- [`utils.write_csv`](./utils.md#function-write_csv): Create csv file. Optimized for large files as write on disk in chunks
- [`utils.write_geojson`](./utils.md#function-write_geojson): Create geojson file. Optimized for large files as write on disk in chunks
