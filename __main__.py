"""
__main__.py
"""

import pathlib
import sys

import geopandas
import numpy
import rasterio

from utils.geometry_util import get_geom_by_key_value_pair
from utils.globals       import COUNTRIES_SHP, CRS, LAND_COVER_TIF, LUT, RANGE_OF_YEARS, SHPS_DIR
from utils.raster_util   import get_band_data, get_geometry_mask, get_window, get_window_transform


def main() -> int:
    """
    main
    """

    countries_gdf      = geopandas.read_file(COUNTRIES_SHP).to_crs(CRS)
    canada_geom        = get_geom_by_key_value_pair(countries_gdf, "NAME", "Canada"       )
    united_states_geom = get_geom_by_key_value_pair(countries_gdf, "NAME", "United States")

    with rasterio.open(LAND_COVER_TIF) as land_cover_tif:
        # Open handle to land_cover.tif.

        for year in RANGE_OF_YEARS:
            # Do the following for each year in the range (1984, 2025):

            fire_polys_shp = SHPS_DIR / pathlib.Path(f"fire_polys/fire_polys{year}/fire_polys{year}.shp")
            fire_polys_gdf = geopandas.read_file(fire_polys_shp).to_crs(CRS)

            for country_geom in [canada_geom, united_states_geom]:
                # Do the following for each country in ("Canada", "United States"):

                class_id_counts = numpy.zeros(5, dtype=numpy.int64)
                # Initialise a 1-indexed array to accumulate class id counts for the subject (year,-
                #  country). Index 0 is unused.

                for _, fire_poly in fire_polys_gdf.iterrows():
                    # Do the following for each fire_poly object in fire_polys_gdf:

                    fire_poly_geom = fire_poly.geometry

                    if not fire_poly_geom.intersects(country_geom):
                        continue
                    # If the fire_poly geometry does not intersect the country geometry, continue.

                    clipped_fire_poly_geom = fire_poly_geom.intersection(country_geom)
                    # fire_poly geometries can intersect multiple country geometries. To avoid coun-
                    # t duplication, clip the fire_poly geometry to the subject country geometry.

                    if clipped_fire_poly_geom.is_empty:
                        continue
                    # If the clipped fire_poly geometry does not contain any vertices, continue. Th-
                    # is can occur if the unclipped fire_poly geometry touches the subject country -
                    # geometry, resulting in fire_poly_goem.intersects returning true, but there is-
                    #  no overlap, resulting in fire_poly_geom.intersection returning a shapely.Geo-
                    # metry with 0 vertices.

                    window                   = get_window(clipped_fire_poly_geom)
                    window_transform         = get_window_transform(land_cover_tif, window)
                    band_data                = get_band_data(land_cover_tif, 1, window)
                    geometry_mask            = get_geometry_mask(clipped_fire_poly_geom, window.shape, window_transform) # pylint: disable=no-member
                    band_data[geometry_mask] = 0
                    class_id_data            = LUT[band_data]

                    for class_id in range(1, 5):
                        # Do the following for each land cover class in the range (1, 5):

                        class_id_counts[class_id] += numpy.sum(class_id_data == class_id)
    return 0


if __name__ == '__main__':
    sys.exit(main())
