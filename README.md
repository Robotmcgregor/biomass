## Field Data Processing
### Converting basal to AGB

## Zonal Stats Processing Status Rerun
|Tile | SR & FC Zonal | Density & Height | Density & Height Zonal | Met | Seasonal & SI | Fire | Number of Sites |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 101_072 | masking | 1988-1991 - Complete | Re-ran| Complete | Complete | Complete | 10 |
| 101_073 | zs - running | 2011-2014 - Complete | Re-ran | Complete | Complete | Complete | 9 | 
| 101_074 | masked | 2011-2014 - Complete | Complete | Complete | Complete | Complete | 2 |
| 102_071 | masking | 1988-1991 - Complete | Re-running | Complete | Complete | Complete | 13 | 
| 102_072 | masking | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 13 | 
| 102_073 | masking | 2010-2021 - Complete | Complete | Complete | Complete | Complete| 8 | 
| 103_070 | masking | 1988-1992 - Complete | Complete | Complete | Complete | Complete | 12|
| 103_071 | masking | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 3 | 
| 103_072 | masking | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 11 | 
| 104_069 | masking | 1998-2022 - Complete | Running | Complete | Complete | Complete | 2 |
| 104_070 | masked  | 1988-2022 - Complete | Running | Complete | Complete | Complete | 10 |
| 104_071 | masking | 1988-2022 - Complete | Complete | Complete | Complete | Complete| 5|
| 105_069 | masked | 1988-2023 - Complete | Running | Complete | Complete | Complete | 15| 
| 105_070 | msking | 1988-2022 - Complete | Complete | Complete | Complete | Complete | 10 |
| 105_071 |  masked | 1988-2021 - Complete | Complete | Complete | Complete | Complete | 9 |
| 105_072 | masking | 1988-2022 - Complete | Complete | Complete | Complete | Complete | 17 |
| 105_073 | masked | 2010-2021 - Complete | Complete | Complete | Complete | Complete | 1 |
| 106_069 | checked| 1988-2022 - Complete | Complete | Complete | Complete | Complete | 29 |
| 106_071 | checked | 1988-2023 - Complete | Complete | Complete | Complete | Complete | 16 |

#### SLATS

NTG system:
Local machine: [http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_field_data_clean_v5.ipynb](http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_field_data_clean_v5.ipynb)

Lenovo location: 
Local machine: [http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_field_data_clean_v5.ipynb](http://localhost:8888/notebooks/projects/cdu/biomass/nb/field_data/biomass_field_data_clean_v6.ipynb)

This notebook functions on:

* env - baimass_zonal
* It searches for an Excel spreadsheet called: slats_biomass_field_data.xlsx
* Located here: cdu\data\slats\varified_by_rm
* Outputs are: C:\Users\robot\projects\cdu\data\output\{date}\slats_c_bio_site_totals.csv

----------------------------------------------------------------------------------

#### TERN

Local machine: [http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_proportion_tern_field_data_clean_v2.ipynb](
http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_proportion_tern_field_data_clean_v2.ipynb)

This notebook functions on:

* env - baimass_zonal
* It searches for an Excel spreadsheet called: TERN basal_area_data_Grant_SEPT2022.xlsx
* Located here: cdu\data\tern_data
* Outputs are: :\Users\robot\projects\cdu\data\output\{date}\c_tern_bio_site_totals.csv

-----------------------------------------------------------------------------------------

##### Collate SLATS and TERN

Local machine: [http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/collate_data/collate_slats_tern.ipynb](http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/collate_data/collate_slats_tern.ipynb)

This notebook functions on:

* env - baimass_zonal
* It searches for the TERN and SLATS csv files: slats_c_bio_site_totals.csv and c_tern_bio_site_totals.csv
* Located here: cdu\data\tern_data
* Outputs are: "D:\biomass\collate_agb\{date}\slats_tern_biomass.csv"

------------------------------------------------------------------------------------------

## Processing Status

### QLD silo data

rerunning:

| Variable | SLATS | SLATS & TERN | DATE |
|:-:|:-:|:-:|:-:|
|daily_rain | "U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1624" | Complete | 20240317 |
|rh_tmax | "U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1625" | Complete | 20240317 |
|rh_tmin|"U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1851"| Complete | 20240317 |
|et_actual|"U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1622"| Complete | 20240317 |
|min_temp|"U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1853"| Complete | 20240317 |
|max_temp|"U:\biomass\zonal_stats_raw\met\rmcgr_meteorological_20240317_1855"| Complete| 20240317 |
	

* rh_tmax - final data
* rh_tmin - final data
* daily_rain - final data
* et_actual - final data
* min_temp - final data
* max_temp - final data

----------------------------------------------------------------------------

##### Create site plots, and calculate seasonal means and seasonal index.

Local machine: ntg_repo/carbon/biomass/nb/report/meteorological_trends_for_loop.ipynb

This notebook functions on:

* env - biomass_zonal
* It searches for Met zonal stats files: {site}.{year}_1ha_{data_type}_zonal_stats.csv
* Located here: X:\PGB\RSU\biomass\zonal_stats_raw\met_clean\{data_type}
* Outputs are:
  	- plots
  	- mean monthly {data type}: i.e. agb02_monthly_daily_rain.csv)
  	- monthly daily rain: agb02_mean_monthly_daily_rain.csv
  	- si_daily_rain: seasonal_agb02_2012_daily_rain.csv
  	- box plots
  	- line plots


----------------------------------------------------------------------------------

Add height from model to site data - try using different allometry.

Local machine: ntg_repo/carbon/biomass/nb/field_data/agb_with_height/biomass_from_basal_and_height.ipynb


----------------------------------------------------------------------------------------

##### Collate meteorological data - seasonal and si - check this as it runs out of memory.

PGB-BAS21: biomass/nb/seasonal_index/merge_meteorological_var_seasonal_si.ipynb - located

Note: collation pipeline pulls this data not collated: U:\biomass\raw_zonal_stats\met\collation\slats_tern

---------------------------------------------------------------------------------------------

## Create Height data

PGB-BAS21: [http://localhost:8891/notebooks/clearing/lsat/landsat_workflow/height_landsat_processing_workflow_biomass_env_ana_base.ipynb](http://localhost:8891/notebooks/clearing/lsat/landsat_workflow/height_landsat_processing_workflow_biomass_env_ana_base.ipynb)

check that the new location works?
[http://localhost:8888/notebooks/biomass/height_landsat_processing_workflow_biomass_env_ana_base.ipynb](http://localhost:8888/notebooks/biomass/height_landsat_processing_workflow_biomass_env_ana_base.ipynb)

### Create Density data

#### PGB-BAS21:

##### Extract zonal Statistics

#ISSUE \data\slats_tern site is {site}_{date}

Current data is {site}

* The issue was the dates month and day was confused in some areas - check the colation on Metabox.

## Zonal Stats Processing Status
|Tile | SR & FC Zonal | Density & Height | Density & Height Zonal | Met | Seasonal & SI | Fire | Number of Sites |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 101_072 | Rerunning | 1988-1991 - Complete | Complete | Complete | Complete | Complete | 10 |
| 101_073 | Complete | 2011-2014 - Complete | Complete | Complete | Complete | Complete | 9 | 
| 101_074 | Complete | 2011-2014 - Complete | Complete | Complete | Complete | Complete | 2 |
| 102_071 | Complete | 1988-1991 - Complete | Complete | Complete | Complete | Complete | 13 | 
| 102_072 | Complete | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 13 | 
| 102_073 | Complete | 2010-2021 - Complete | Complete | Complete | Complete | Complete| 8 | 
| 103_070 | Complete | 1988-1992 - Complete | Complete | Complete | Complete | Complete | 12|
| 103_071 | Complete | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 3 | 
| 103_072 | Complete | 1988-2022 - Complete | Complete | Complete| Complete | Complete | 11 | 
| 104_069 | Complete | 1998-2022 - Complete | Running | Complete | Complete | Complete | 2 |
| 104_070 | Complete | 1988-2022 - Complete | Running | Complete | Complete | Complete | 10 |
| 104_071 | Complete | 1988-2022 - Complete | Complete | Complete | Complete | Complete| 5|
| 105_069 | Complete | 1988-2023 - Complete | Running | Complete | Complete | Complete | 15| 
| 105_070 | Complete | 1988-2022 - Complete | Complete | Complete | Complete | Complete | 10 |
| 105_071 | Complete | 1988-2021 - Complete | Complete | Complete | Complete | Complete | 9 |
| 105_072 | Complete | 1988-2022 - Complete | Complete | Complete | Complete | Complete | 17 |
| 105_073 | Complete | 2010-2021 - Complete | Complete | Complete | Complete | Complete | 1 |
| 106_069 | Complete | 1988-2022 - Complete | Complete | Complete | Complete | Complete | 29 |
| 106_071 | Complete | 1988-2023 - Complete | Complete | Complete | Complete | Complete | 16 |

Extract zonal statistics for Landsat tile SR and FC data, and create and extract fire mask data.

Fire:
 nt_mosaic_biomass_burnscar_zonal_pipeline

PGB-BAS21: biomass/tile_biomass_zonal_pipeline/code/step1_1_initiate_fractional_cover_zonal_stats_pipeline.py

Extract density and height classes or classifications zonal statistics PGB-BAS21: biomass/tile_biomass_zonal_height_density_pipeline/code/step1_1_initiate_fractional_cover_zonal_stats_pipeline.py

### Collate zonal stats data

Collate zonal statistics outputs into a singe data frame (i.e. fire masked data no fire masked data, height density and meteorological data) PGB-BAS21: biomass/biomass_collation/code/step1_1_initiate_biomass_zonal_stats_collation_pipeline.py

## ISSUES
biomass 1 too many.... check calcs with original data

<img width="346" alt="image" src="https://github.com/Robotmcgregor/biomass/assets/35555135/cf1b7261-a64b-4660-90d3-4bf9b21473fc">


dp1 dry
dp1 annual
dp1fm

#Soloution testing

df_dp1_mask_dropna.csv has dy and annual 189 items
df_dp1_dropna has dry and annual but only some 32 sites.

## Pipelines
Tile Biomass Zonal Stats
Tile Biomass Zonal Stats Height & Density Pipeline

NT Mosaic Biomass Burnscar Zonal Pipeline

NT Mosaic Biomass Zonal Pipeline

QLD Meteorological Biomass Zonal Pipeline
Biomass Collation
Pipeline outputs:

U:\scratch\rob\pipelines\outputs


### Machine Learning
Notebook locations:

C:\Users\rmcgr\ntg_repo\carbon\biomass\nb\ml


Random Forrest Regression: sklearn_random_forest_regression_for_seasonal_selections.ipynb (http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/ml/clean_models/sklearn_random_forest_regression_for_seasonal_selections.ipynb)
Adda Boost Regression: sklearn_adda_boost_regression_for_seasonal_selections.ipynb (http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/ml/clean_models/sklearn_adda_boost_regression_for_seasonal_selections.ipynb)
Gradient Boosting Regression: sklearn_gradient_boosting_regression_for_seasonal_selections.ipynb (http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/ml/clean_models/sklearn_gradient_boosting_regression_for_seasonal_selections.ipynb)
SVR Regression: sklearn_svr_regression_for_nt_mosaic_2023.ipynb (http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/ml/sklearn_svr_regression_for_nt_mosaic_2023.ipynb)
Tensor Flow ANN: tensorflow_ann_for_seasonal_selections_v1.ipynb (http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/ml/tensorflow_ann_for_seasonal_selections_v1.ipynb)

-------------------------------------------------------------------------------------------------------------

## Collation Pipeline Notes

Latest biomass data: U:\biomass\collated_agb\20230927\slats_tern_biomass.csv

| Script | Description | Status | Output location | Scratch outputs | Issue | Error corrected | Merged output rows |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| step1_initiate_biomass_zonal_stats_collation_pipeline | Workflow and final merge | Merge not complete| | | | | 
| step2_merge_tile_density_height_zonal_stats.py | Separate seasons for density and height, rename dry season columns and merge data set to one complete data set | Complete | | U:\biomass\scratch\density_height\ccw_fdc_h99_hcv_hmc_hsd_n17_wdc_wfp_clean.csv	| | | 158|
| step4_merge_tile_zonal_stats | Separate seasons for fc and sr , rename dry season columns and merge data set to one complete data set | Complete  |	| U:\biomass\scratch\sr_fc\dbg_dbi_dbi_mask_dp0_dp1_dp1_mask_clean.csv	| DBI zonal stats exporting incorrect file name	| No| 157 |
| step3_calculate_indices	| Apply vegetation indices to dbg and dbi values | Complete  | | X:\PGB\RSU\biomass\scratch\veg_ind	 | | 142 |
| step4_merge_meteorological_data_agb_zonal_stats.py | | Complete |  | X:\PGB\RSU\biomass\scratch\met | | | |
| step5_merge_meteorological_si	| Merging dataframes not complete	| Complete	| U:\biomass\met_zonal_stats_per_site\	| X:\PGB\RSU\biomass\scratch\met |||	
| step6_merge_tile_seasonal_fire_zonal_stats | Need to concat dka, dkn and dkh together before calculating fire si | Complete | U:\scratch\rob\pipelines\outputs\ and (dir)\mosaic_concat\fire_scar_zonal_stats\	| X:\PGB\RSU\biomass\scratch\fire ||||	

----------------------------------------------------------------------------------------

## QLD silo data

rerunning:

| Variable | SLATS | SLATS & TERN | DATE |
|:-:|:-:|:-:|:-:|
|daily_rain | X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1825 | Running | 20240317 |
|rh_tmax | X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1823 | Running | 20240317 |
|rh_tmin|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1822|| |
|et_actual|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1821|Running| 20240317 |
|min_temp|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1820|| |
|max_temp|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1824|| |
	

* rh_tmax - final data
* rh_tmin - final data
* daily_rain - final data
* et_actual - final data
* min_temp - final data
* max_temp - final data

## Biomass data errors:
| Site | Issue | Solution | Completed | 
|:-:|:-:|:-:|:-:|
|buf01|Incorrect date 2021 → 2012rerun all zonal stats SILO and Mosaic and 106_069|Done|


## Zonal stats code names

|Data | Type | Code Name |
|:-:|:-:|:-:|
| Burn scar mapping | QLD | dkk | 
| Burn scar mapping | NAFI | dkh | 
| Burn scar mapping | NAFI | dkn |

## Fractional Cover
| Data | Type | Code Names |
|:-:|:-:|:-:|
| Fractional Cover | Annual seasonal composite with fire mask applied | dp1fm | 
| Fractional Cover | Dry seasonal composite with fire mask applied | dp1fm_dry |
| Fractional Cover | Annual seasonal composite | dp1 |
| Fractional Cover | Dry seasonal composite | dp1_dry | 
| Fractional Cover | Single date with fire mask applied| dp0fm | 
| Fractional Cover | Single date | dp0 |

## Surface Reflectance

| Data | Typ e| Code Names |
|:-:|:-:|:-:|
| Surface Reflectance| Annual seasonal composite with fire mask applied| dbifm |
| Surface Reflectance | Dry seasonal composite with fire mask applied | dbifm_dry |
| Surface Reflectance | Annual seasonal composite | dbi |
| Surface Reflectance | Dry seasonal composite | dbi_dry |

Additional tables are here: https://confluence.nt.gov.au/display/ENVD/Collation+Pipeline+notes

--------------------------------------------------------------------------------------------
slats only: "U:\biomass\agb\20231102\slats_tern_biomass.csv"




slats and tern: "U:\biomass\collated_agb\20231103\slats_tern_biomass.csv"






QLD silo data

-------------------------------------------------------------------------------------------------------------

## To do list

Locate and git: 

* Local machine: http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/collate_data/collate_slats_tern.ipynb


* Local machine: ntg_repo/carbon/biomass/nb/report/meteorological_trends_for_loop.ipynb

* Local machine: ntg_repo/carbon/biomass/nb/field_data/agb_with_height/biomass_from_basal_and_height.ipynb

## Other issues
* There may have been an issue related to dates??
* Site 21 and 22 have the same photo and site 22 is dense closed forest


Met zonal stats per site: need to be redone.

ml: outputs are corrupt.

ml_data_dir: corrupt
