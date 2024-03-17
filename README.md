## Field Data Processing
### Converting basal to AGB

#### SLATS

Local machine: http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_field_data_clean_v5.ipynb

----------------------------------------------------------------------------------

#### TERN
##### Collate SLATS and TERN

Local machine: http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/collate_data/collate_slats_tern.ipynb

Local machine: http://localhost:8888/notebooks/ntg_repo/carbon/biomass/nb/field_data/biomass_proportion_tern_field_data_clean_v2.ipynb

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




Random Forrest Regression: sklearn_random_forest_regression_for_seasonal_selections.ipynb
Adda Boost Regression: sklearn_adda_boost_regression_for_seasonal_selections.ipynb
Gradient Boosting Regression: sklearn_gradient_boosting_regression_for_seasonal_selections.ipynb
SVR Regression: sklearn_svr_regression_for_nt_mosaic_2023.ipynb
Tensor Flow ANN: tensorflow_ann_for_seasonal_selections_v1.ipynb 




Met zonal stats per site: need to be redone.

ml: outputs are corrupt.

ml_data_dir: corrupt
