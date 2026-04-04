import geopandas
import numpy

from shapely import Geometry


def get_geom_by_idx(gdf: geopandas.GeoDataFrame, idx: numpy.int64) -> Geometry:
    """
    Get a :class:`shapely.Geometry` from a :obj:`geopandas.GeoDataFrame` by positional index.

    Parameters
    ----------
    gdf : :obj:`geopandas.GeoDataFrame`
        :obj:`geopandas.GeoDataFrame`.
    idx : :class:`numpy.int64`
        Positional index.

    Returns
    ----------
    :class:`shapely.Geometry`
    """
    
    return gdf.geometry.iloc[idx]


def get_geom_by_key_value_pair(gdf: geopandas.GeoDataFrame, key: str, value: str) -> Geometry:
    """
    Get a :class:`shapely.Geometry` from a :obj:`geopandas.GeoDataFrame` by (key, value) pair.

    Parameters
    ----------
    gdf : :obj:`geopandas.GeoDataFrame`
        :obj:`geopandas.GeoDataFrame`.
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