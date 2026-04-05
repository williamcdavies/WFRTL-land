"""
utils.globals
"""


import pathlib

import numpy
import rasterio


PIXEL_AREA_KM2 = 0.0009
"""
30 meters by 30 meters expressed in km2
"""

OUTPUT_CSV     = pathlib.Path.cwd() / "wfrtl-land.csv"
"""
Path to the output destination
"""

MAIN_SRC_DIR   = pathlib.Path(__file__).parent.parent
"""
Path to the directory containing `main.py`.
"""

SHPS_DIR       = MAIN_SRC_DIR   / pathlib.Path("shps")
"""
Path to the shps directory.
"""

COUNTRIES_DIR  = SHPS_DIR       / pathlib.Path("countries")
"""
Path to the shps/countries directory.
"""

COUNTRIES_SHP  = COUNTRIES_DIR  / pathlib.Path("countries.shp")
"""
Path to shps/countries/countries.shp.
"""

TIFS_DIR       = MAIN_SRC_DIR   / pathlib.Path("tifs")
"""
Path to the tifs directory.
"""

LAND_COVER_DIR = TIFS_DIR       / pathlib.Path("land_cover")
"""
Path to the tifs/land_cover directory.
"""

LAND_COVER_TIF = LAND_COVER_DIR / pathlib.Path("land_cover.tif")
"""
Path to tifs/land_cover/land_cover.tif.
"""

RANGE_OF_YEARS = range(1984, 2025)
"""
Range of years for which burn area geometries are available.
"""

CRS:       rasterio.crs.CRS             = None
"""
Coordinate Reference System (CRS) of :obj:`LAND_COVER_TIF`.
"""

TRANSFORM: rasterio.transform.TRANSFORM = None
"""
Transform of :obj:`LAND_COVER_TIF`.
"""

with rasterio.open(LAND_COVER_TIF) as land_cover_tif:
    CRS       = land_cover_tif.crs       # assigned here
    TRANSFORM = land_cover_tif.transform # assigned here

RAST_VALUE_TO_CLASS_ID = {
    1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
    7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 15: 2,
    17: 3,
    13: 4, 14: 4, 16: 4, 18: 4, 19: 4,
}
"""
Mapping of NALCMS raster values to land cover class IDs.

- Class 1 (Forest):                        raster values 1-6
- Class 2 (Shrubland/Grassland/Cropland):  raster values 7-12, 15
- Class 3 (Urban):                         raster value 17
- Class 4 (Barren/Wetland/Water/Snow/Ice): raster values 13, 14, 16, 18, 19
"""

CLASS_ID_TO_CLASS_NAME = {
    1: "Forest",
    2: "Shrubland/Grassland/Cropland",
    3: "Urban",
    4: "Barren/Wetland/Water/Snow/Ice",
}
"""
Mapping of land cover class IDs to land cover class names.

- Class 1 (raster values 1-6):                Forest
- Class 2 (raster values 7-12, 15):           Shrubland/Grassland/Cropland
- Class 3 (raster value 17):                  Urban
- Class 4 (raster values 13, 14, 16, 18, 19): Barren/Wetland/Water/Snow/Ice
"""

LUT = numpy.zeros(256, dtype=numpy.uint8)
"""
256-element lookup table mapping raster values to land cover class IDs. Unmapped values default to 
0.
"""

for rast_value, class_id in RAST_VALUE_TO_CLASS_ID.items():
    LUT[rast_value] = class_id # assigned here
