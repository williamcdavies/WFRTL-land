# WFRTL-land

## Overview
The purpose of this project is to generate $41$ datasets of the following schema:

```
(YEAR: int, 
COUNTRY: str, 
CLASS_1_BURN_AREA: km2, 
CLASS_2_BURN_AREA: km2, 
CLASS_3_BURN_AREA: km2, 
CLASS_4_BURN_AREA: km2, 
CLASS_1_BURN_PERCENTAGE: %, 
CLASS_2_BURN_PERCENTAGE: %, 
CLASS_3_BURN_PERCENTAGE: %, 
CLASS_4_BURN_PERCENTAGE: %)
```

such that `YEAR` is in the range (1984, 2025), `COUNTRY` is in ("Canada", "United States"), and `CLASS_N_BURN_PERCENTAGE` is taken as a percentage of the area of the subject country.

## Data & Project Structure
The data required by this program is not intended to be published to github due to its volume. However, tifs/land_cover/land_cover.tif can be downloaded from [here](https://www.cec.org/files/atlas/?z=3&x=-119.4434&y=48.5748&lang=en&layers=polbounds%2Clandcover2015ls&opacities=100%2C100&labels=true), shps/countries/countries.* can be downloaded from [here](https://www.arcgis.com/home/item.html?id=fa510018bdd044b08fc64d2a16bc680a), and shps/fire_polys/fire_polys*/fire_polys.* can be downloaded from [NO LINK PROVIDED].

In order for certain global variables to resolve correctly at import, this project must have the following structure:

```
.
├── __main__.py
├── shps
│   ├── countries
│   │   ├── countries.cpg
│   │   ├── countries.dbf
│   │   ├── countries.prj
│   │   ├── countries.shp
│   │   └── countries.shx
│   └── fire_polys
│       ├── fire_polys1984
│       │   ├── fire_polys1984.cpg
│       │   ├── fire_polys1984.dbf
│       │   ├── fire_polys1984.prj
│       │   ├── fire_polys1984.shp
│       │   └── fire_polys1984.shx
│       │   .
│       │   .
│       │   .
│       └── fire_polys2024
│           ├── fire_polys2024.cpg
│           ├── fire_polys2024.dbf
│           ├── fire_polys2024.prj
│           ├── fire_polys2024.shp
│           └── fire_polys2024.shx
├── tifs
│   └── land_cover
│       └── land_cover.tif
```

## Compilation & Execution
This program can be compiled and executed with the following commands. This assumes the current working directory contains `__main__.py` and the required data and project structure is correct.

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 __main__.py
```