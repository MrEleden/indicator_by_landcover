# indicator_by_landcover

## Data acquisiton
You can download all the necessary data as described below. The downloaded data should be placed in the root directory of this repository (i.e., the same place as this README.md)

1. Land cover maps  
The land cover maps are based on the existing dataset available on the link below:
http://maps.elie.ucl.ac.be/CCI/viewer/download.php  
Each time you visit this site, you should enter your name, organization and e-mail address (dummies are okay).  
In this web site, click `by year: 24 tif files, 1 band` and `Legend (csv)` to download the global land cover map and the legend, respectively. The global land cover map covers from 1992 to 2015 and a channel of this image file corresponds to one of the years.


2. GDP data  
This can be downloaded from https://drive.google.com/drive/u/0/folders/1bRV0ufLdLzeskhWjgSOyoyDjCmNd_uPR
, named "Download-GDPcurrent-NCU-countries.xls".


## Prepare nation-wise land cover maps
Run `python extract_lcmap_by_nation.py <country_name>`.  
`<country_name>` should be one of country names in `country_name.txt`.  
This will create the directory `./nation_lcmaps` and save a land cover map of a nation you chose in that directory.
