# indicator_by_landcover

## Data acquisiton
You can download all the necessary data as described below. The downloaded data should be placed in the root directory of this repository (i.e., the same place as this README.md)

1. Land cover maps  
The land cover maps are based on the existing dataset available on the link below:
http://maps.elie.ucl.ac.be/CCI/viewer/download.php  
Each time you visit this site, you should enter your name, organization and e-mail address (dummies are okay).  
In this web site, click `1 tif file, 24 bands, zip compression` and `Legend (csv)` to download the global land cover map and the legend, respectively.
The global land cover map covers from 1992 to 2015 and a channel of this image file corresponds to one of the years.  
The file names of the downloaded map and legend will be `ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992_2015-v2.0.7.tif` and `ESACCI-LC-Legend.csv`, respectively.

2. GDP data  
This can be downloaded from [Google Drive](https://drive.google.com/drive/u/0/folders/1bRV0ufLdLzeskhWjgSOyoyDjCmNd_uPR)
, named "Download-GDPcurrent-NCU-countries.xls".


## Prepare nation-wise land cover maps
Run `python extract_lcmap_by_nation.py <country_name>`.  
`<country_name>` should be one of country names in `country_name.txt`.  
This will create the directory `./nation_lcmaps` and save a land cover map of a nation you chose in that directory.


## Dependency
`gdal` is required.

conda create -n gdal_env
conda activate gdal_Env
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 gdal

## Others
The graphs on the initial check (as I posted on [DocBase](https://synspective.docbase.io/posts/979916) or [Slack](https://synspective.slack.com/archives/CPSFZ39EY/p1574954671000700)) can be reproduced by following [lc.ipynb](https://github.com/synspective/indicator_by_landcover/blob/master/lc.ipynb).
