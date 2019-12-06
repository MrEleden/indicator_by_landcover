import argparse
import os
import requests
import json
from urllib.parse import quote
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--country', required=True, help='A country name based on `country_name.txt`')
    parser.add_argument('-o', '--output_dir', default='nation_lcmaps')
    parser.add_argument('-i', '--raster_path', default='./ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992_2015-v2.0.7.tif')
    parser.add_argument('--nodata_value', type=int, default=255)
    args = parser.parse_args()

    country = args.country
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    print('Fetching geojson of {}...\n'.format(country))
    COUNTRY_CITY_DB_BASE_URL = "http://35.200.84.0/countries"
    SHAPE_DB_URL = "{}/{}".format(COUNTRY_CITY_DB_BASE_URL, quote(country))
    response = requests.get(SHAPE_DB_URL)
    response = response.json()

    # If the URL is wrong, `response['features']` will return None.
    assert response['features'] != None

    json_path = os.path.join(output_dir, '{}.json'.format(country.replace(' ', '_')))
    with open(json_path,'w') as fp:
        json.dump(response, fp)

    print('Executing gdalwarp...\n')
    output_path = os.path.join(output_dir, '{}.tif'.format(country.replace(' ', '_')))    

    cmd_str = ['gdalwarp', '--config', 'GDAL_CACHEMAX', '4096', '-cutline', 
    json_path, '-crop_to_cutline', '{}'.format(args.raster_path), output_path]
    subprocess.run(cmd_str)

if __name__ == "__main__":
    main()
