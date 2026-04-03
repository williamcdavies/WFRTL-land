import pathlib
import rasterio


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

CRS = None
"""
Coordinate Reference System (CRS) of :obj:`LAND_COVER_TIF`.
"""
with rasterio.open(LAND_COVER_TIF) as land_cover_tif:
    CRS = land_cover_tif.crs # assigned here


# import numpy
# import rasterio




# PATH_TO_COUNTRIES_SHP  = "../shps/countries/countries.shp"
# PATH_TO_FIRE_POLYS_DIR = "../shps/fire_polys/"
# PATH_TO_LAND_COVER_DIR = "../land_cover_2015v4_30m_tif"
# PATH_TO_LAND_COVER_TIF = "../land_cover_2015v4_30m_tif/NA_NALCMS_landcover_2015v4_30m/data/NA_NALCMS_landcover_2015v4_30m.tif"

# SET_OF_COUNTRIES = ["Canada", "United States"]
# RANGE_OF_YEARS   = range(1984, 2025) # = [1984, 2024]

# RAST_VALUE_TO_CLASS_ID = {
#     # RAST VALUES IN (1,2,3,4,5,6)       MAP TO CLASS ID 1
#     1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,
#     # RAST VALUES IN (7,8,9,10,11,12,15) MAP TO CLASS ID 2
#     7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 15: 2,
#     # RAST VALUES IN (17)                MAP TO CLASS ID 3
#     17: 3,
#     # RAST VALUES IN (13,14,16,18,19)    MAP TO CLASS ID 4
#     13: 4, 14: 4, 16: 4, 18: 4, 19: 4,
# }

# CLASS_ID_TO_CLASS_NAME = {
#     1: "Forest",
#     2: "Shrubland/Grassland/Cropland",
#     3: "Urban",
#     4: "Barren/Wetland/Water/Snow/Ice",
# }

# NODATA = 127

# LUT = numpy.zeros(256, dtype=numpy.uint8)
# for rast_value, class_id in RAST_VALUE_TO_CLASS_ID.items():
#     LUT[rast_value] = class_id

# with rasterio.open(PATH_TO_LAND_COVER_TIF) as src:
#     CRS               = src.crs
#     TRANSFORM         = src.transform
#     PIXEL_AREA_IN_KM2 = abs(TRANSFORM.a * TRANSFORM.e) / 1e6