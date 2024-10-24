# Clipping data for missouri basin

import geopandas as gpd
from shapely.geometry import Polygon

# access us states shapefile

us_map = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip")
conus = us_map[~us_map.STUSPS.isin(["AK", "HI", "PR"])].to_crs("EPSG:4326")

import os
import requests
import zipfile

# automatically download/extract watershed boundary shapefiles
for wbd in [10]:
    if not os.path.isfile(f"WBD_{wbd}_HU2_Shape/Shape/WBDHU2.shp"):
        print(f"Downloading/extracting WBD {wbd}")
        r = requests.get(
            f"https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/WBD/HU2/Shape/WBD_{wbd}_HU2_Shape.zip"
        )
        with open(f"WBD_{wbd}_HU2_Shape.zip", "wb") as zip_file:
            zip_file.write(r.content)
        with zipfile.ZipFile(f"WBD_{wbd}_HU2_Shape.zip", 'r') as zip_file:
            zip_file.extractall(f"WBD_{wbd}_HU2_Shape")

mo_basin = gpd.read_file("WBD_10_HU2_Shape/Shape/WBDHU2.shp")
mo_basin = gpd.GeoSeries(Polygon(mo_basin.iloc[0].geometry.exterior), crs="EPSG:4326")
print('Files successfully loaded')