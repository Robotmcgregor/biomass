## Field Data Processing
### Converting basal to AGB

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

Or this: [http://localhost:8888/notebooks/projects/cdu/biomass/nb/collate_data/colate_slats_and_tern_agb_datasets.ipynb](http://localhost:8888/notebooks/projects/cdu/biomass/nb/collate_data/colate_slats_and_tern_agb_datasets.ipynb)

This notebook functions on:

* env - baimass_zonal
* It searches for the TERN and SLATS csv files: slats_c_bio_site_totals.csv and c_tern_bio_site_totals.csv
* Located here: cdu\data\tern_data
* Outputs are: C:\Users\robot\projects\cdu\data\output\{date}\slats_tern_biomass.csv

------------------------------------------------------------------------------------------

height: Height data is on the 0565 HD and in the biomass directory.

----------------------------------------------------------------------------

##### Create site plots, and calculate seasonal means and seasonal index.

Local machine: ntg_repo/carbon/biomass/nb/report/meteorological_trends_for_loop.ipynb

Add height from model to site data - try using different allometry.

Local machine: ntg_repo/carbon/biomass/nb/field_data/agb_with_height/biomass_from_basal_and_height.ipynb

----------------------------------------------------------------------------------------

##### Collate meteorological data - seasonal and si

PGB-BAS21: biomass/nb/seasonal_index/merge_meteorological_var_seasonal_si.ipynb

---------------------------------------------------------------------------------------------

## Create Height data

PGB-BAS21: http://localhost:8891/notebooks/clearing/lsat/landsat_workflow/height_landsat_processing_workflow_env_ana_base.ipynb

### Create Density data

#### PGB-BAS21:

##### Extract zonal Statistics

Extract zonal statistics for Landsat tile SR and FC data, and create and extract fire mask data.

PGB-BAS21: biomass/tile_biomass_zonal_pipeline/code/step1_1_initiate_fractional_cover_zonal_stats_pipeline.py

Extract density and height classes or classifications zonal statistics PGB-BAS21: biomass/tile_biomass_zonal_height_density_pipeline/code/step1_1_initiate_fractional_cover_zonal_stats_pipeline.py

### Collate zonal stats data

Collate zonal statistics outputs into a singe data frame (i.e. fire masked data no fire masked data, height density and meteorological data) PGB-BAS21: biomass/biomass_collation/code/step1_1_initiate_biomass_zonal_stats_collation_pipeline.py

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

| Variable | SLATS | SLATS & TERN |
|:-:|:-:|:-:|
|daily_rain | X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1825 | Running |
|rh_tmax | X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1823 | Running | 
|rh_tmin|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1822|Running|
|et_actual|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1821|Running|
|min_temp|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1820|Running|
|max_temp|X:\PGB\RSU\biomass\zonal\slats_met\rmcgr_meteorological_20231102_1824|Running|
	

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

* Local machine: http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_proportion_tern_field_data_clean_v2.ipynb

* Local machine: ntg_repo/carbon/biomass/nb/report/meteorological_trends_for_loop.ipynb

* Local machine: ntg_repo/carbon/biomass/nb/field_data/agb_with_height/biomass_from_basal_and_height.ipynb


Met zonal stats per site: need to be redone.

ml: outputs are corrupt.

ml_data_dir: corrupt
