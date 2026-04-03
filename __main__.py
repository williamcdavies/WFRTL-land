import geopandas
import numpy
import pathlib
import sys

from shapely       import Geometry
from utils.globals import *


def get_geom_by_idx(gdf: geopandas.GeoDataFrame, idx: numpy.int64) -> Geometry:
    """
    Get a :class:`shapely.Geometry` from a :obj:`shapely.Geometry` by positional index.

    Parameters
    ----------
    gdf : geopandas.GeoDataFrame
        geopandas::GeoDataFrame.
    idx : numpy.int64
        Positional index.

    Returns
    ----------
    :class:`shapely.Geometry`
    """
    
    return gdf.geometry.iloc[idx]


def get_geom_by_key_value_pair(gdf: geopandas.GeoDataFrame, key: str, value: str) -> Geometry:
    """
    Get a :class:`shapely.Geometry` from a :obj:`shapely.Geometry` by (key, value) pair.

    Parameters
    ----------
    gdf : geopandas.GeoDataFrame
        geopandas::GeoDataFrame.
    key : str
        Some column label.
    value : str
        Some unique cell value in subject column.

    Returns
    ----------
    :class:`shapely.Geometry`
    """

    idx = gdf[gdf[key] == value].index

    assert len(idx) == 1, f"count of records having ({key}, {value}) expected to equal 1, got: {len(idx)}"
    return get_geom_by_idx(gdf, idx[0])


def main() -> int:
    countries_gdf      = geopandas.read_file(COUNTRIES_SHP).to_crs(CRS)
    canada_geom        = get_geom_by_key_value_pair(countries_gdf, "NAME", "Canada"       )
    united_states_geom = get_geom_by_key_value_pair(countries_gdf, "NAME", "United States")

    with rasterio.open(LAND_COVER_TIF) as land_cover_tif:
        """
        Open handle to land_cover.tif.
        """

        for year in RANGE_OF_YEARS:
            """
            Do the following for each year in the range (1984, 2025):
            """

            fire_polys_shp = SHPS_DIR / pathlib.Path("fire_polys") / pathlib.Path(f"fire_polys{year}") / pathlib.Path(f"fire_polys{year}.shp")
            fire_polys_gdf = geopandas.read_file(fire_polys_shp).to_crs(CRS)

            for country_geom in [canada_geom, united_states_geom]:
                """
                Do the following for each country in ("Canada", "United States"):
                """
                
                for _, fire_poly in fire_polys_gdf.iterrows():
                    """
                    Do the following for each fire_poly object in fire_polys_gdf:
                    """
                    
                    fire_poly_geom = fire_poly.geometry
                    
                    if not fire_poly_geom.intersects(country_geom):
                        continue
                    """
                    If the fire_poly geometry does not intersect the country geometry, continue.
                    """
                    
                    clipped_fire_poly_geom = fire_poly_geom.intersection(country_geom)
                    """
                    fire_poly geometries can intersect multiple country geometries. To avoid count 
                    duplication, clip the fire_poly geometry to the subject country geometry.
                    """
                    
                    if clipped_fire_poly_geom.is_empty:
                        continue
                    """
                    If the clipped fire_poly geometry does not contain any vertices, continue. This
                    can occur if the unclipped fire_poly geometry touches the subject country geome-
                    try, resulting in fire_poly_goem.intersects returning true, but there is no ove-
                    rlap, resulting in fire_poly_geom.intersection returning a shapely.Geometry wit-
                    h 0 vertices.  
                    """
            
        

    return 0


if __name__ == '__main__':
    sys.exit(main())