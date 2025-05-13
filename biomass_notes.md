Annual masked dp1 and dbi - 106_069

106_069 
1996
2000
2001
2006
2011
2013

105_069
1995
2000
2004
2005
2006
209
2013

104_070
1995
2000
2004
2005
20009
2010
2013

104_070
1995
2000
2005
2009
2010
2013


SLATS and TERN data : "C:\Users\robot\projects\biomass\collated_agb\20240707\slats_tern_biomass.csv"

SLATS TERN MET MOVE SITES: "C:\Users\robot\projects\biomass\collated_agb\20240707\slats_tern_biomass_ep01_buff01_shift.csv"


BioLib data: "C:\Users\robot\projects\biomass\agb\20240922\biolib_agb.csv"
RERB BioLib: https://portal.tern.org.au/metadata/TERN/fc4a7249-ebb2-4ada-8e06-b552bfb297a3

### collate data

http://localhost:8890/notebooks/code/biomass/nb/collate_data/collate_slats_tern_biolib.ipynb


concatenated: C:\Users\robot\projects\biomass\collated_agb\20240923\slats_tern_biolib_biomass.csv
shp: C:\Users\robot\projects\biomass\collated_agb\20240923\slats_tern_biolib_biomass.shp

http://localhost:8888/notebooks/code/biomass/nb/field_data/Biolib_data_processing_v2.ipynb

## ML Metrics

Too much data so instead of using:
http://localhost:8888/notebooks/code/biomass/var_select/code/concatinate_ml_metrics.Copy.ipynb

Run:
1. collate ML metrics: ml pipeline: C:\Users\robot\code\ml\landsat\collate_validation_metrics.py
2. http://localhost:8888/notebooks/code/biomass/var_select/code/concatinate_ml_metrics_read_total_metrics.ipynb

Determine feature importance to reduce model computational requirements:

Adjust head_score
http://localhost:8888/notebooks/code/biomass/var_select/code/concatinate_ml_metrics_read_total_metrics.ipynb



http://localhost:8888/notebooks/code/biomass/var_select/code/concatinate_ml_metrics_read_total_metrics.ipynb

http://localhost:8888/notebooks/code/biomass/var_select/code/gbr/all_target_exc_sd3_mean/gbr_all_data_sddv3_mean_add_knn_xgboost_with_metrics.ipynb

http://localhost:8888/notebooks/code/biomass/nb/corrolation_heatmap/overall_met_feature_corolation_heatmap.ipynb

http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/model_variation%20anova_residuals_plots.ipynb

http://localhost:8888/notebooks/code/biomass/nb/species_list/Latex%20multicolum%20output%20species%20list.ipynb

http://localhost:8888/notebooks/code/biomass/nb/species_list/Latex%20multicolum%20output%20species%20list.ipynb

http://localhost:8889/notebooks/code/biomass/nb/clean_variables_for_ml/annual_fire_mask_variable_correction_and_clean_for_ml.ipynb

http://localhost:8888/notebooks/code/biomass/nb/outliers/outliers_to_latex.ipynb

http://localhost:8888/notebooks/code/biomass/var_select/code/strattify_data_training_test.ipynb

http://localhost:8888/notebooks/code/add_reason_to_excluded_df.ipynb

http://localhost:8891/notebooks/code/landast_file_move_and%20check.ipynb#

http://127.0.0.1:8889/notebooks/code/biomass/nb/clip_10000/colate_agb_model_zonal_stats_timetrace.ipynb

http://127.0.0.1:8889/notebooks/code/biomass/nb/clip_10000/delete_mdl_zonal_dir.ipynb

http://127.0.0.1:8889/notebooks/code/biomass/nb/clip_10000/concat_missing_data_csv.ipynb
http://localhost:8890/notebooks/code/pipelines/clearing/lsat/height/lsat_run_tile_h99_hcv_hsd_hmc_seasonal_comp_pgb-bas20_21_all_years_10000_i_v3.ipynb
http://localhost:8892/notebooks/code/biomass/ml/all00_rs0_RFR_p99_std3_all0_RMSE_sel_num_12_validate_redo.ipynb

does a whole bunch of move files and delete dir's

## H25
height 25 in density pipeline

collate ML metrics: ml pipeline

## Zero values 
C:\Users\robot\projects\biomass\collated_zonal_stats\biomass_0_analysis.csv
http://localhost:8888/notebooks/code/add_reason_to_excluded_df.ipynb


http://localhost:8888/notebooks/code/biomass/nb/collate_data/train_test_add_lat_long.ipynb

Steps following outliers:
http://localhost:8888/notebooks/code/biomass/nb/outliers/outliers_to_latex.ipynb
Check notes for removal of sites and features, also Barkley needs to be changed to Barkly 1 - 7

### features
 - dr mavg
 - dr_mmed
 - dr_msum etc. - review Barkly01

### Fire features:

    file_dict = {"ann_fsm_afsum": ["afsm"],
                 "ann_fyn_afysn": ["afyn"],
                 "ann_pos_aposf": ["apos"],
                 "ann_rio_afrio": ["ario"],

                 "dry_fsm_afsum": ["dfsm"],
                 "dry_fyn_afysn": ["dfyn"],
                 "dry_pos_aposf": ["dpos"],
                 "dry_rio_afrio": ["drio"],

                 "ldy_fsm_afsum": ["lfsm"],
                 "ldy_fyn_afysn": ["lfyn"],
                 "ldy_pos_aposf": ["lpos"],
                 "ldy_rio_afrio": ["lrio"],

                 "cor": ["corr"],

                 }

Removed from:
 - C:\Users\robot\code\pipelines\model_dev\run_ml_models_regularisation_auto.py
 - http://localhost:8888/notebooks/code/biomass/nb/clean_variables_for_ml/dry_fire_mask_variable_correction_and_clean_for_ml_pca_edit.ipynb
 - http://localhost:8888/notebooks/code/biomass/nb/clean_variables_for_ml/annual_fire_mask_variable_correction_and_clean_for_ml_pca_edit.ipynb
 - 
### Sites

- ntagfu0034_2012 - not homegenous 
- NTAMGD0001 - not homegenous 
- NTASTU0005 - potental pixcel bleed form track


## Sorting out corrected ML feature imports

### PCA and concat Dry and Annual values
http://localhost:8888/tree/code/biomass/nb/clean_variables_for_ml

Annual: http://localhost:8888/notebooks/code/biomass/nb/clean_variables_for_ml/dry_fire_mask_variable_correction_and_clean_for_ml_pca_edit.ipynb

Dry: http://localhost:8888/notebooks/code/biomass/nb/clean_variables_for_ml/annual_fire_mask_variable_correction_and_clean_for_ml_pca_edit.ipynb


#### upside down image

\rotatebox{180}{\includegraphics[width=\linewidth]{your-image-file.jpg}}


### Validating model from grid cvs
env: tf_grid2.13_biomass
http://localhost:8890/notebooks/code%2Fbiomass%2Fml%2Fread_model_param_from_pickle.ipynb

http://localhost:8890/notebooks/code/biomass/ml/all02_rs0_GBR_p99_std3_all0_r2_sel_num_12_validate.ipynb

## Create composite
### greyscale
C:\Users\robot\code\biomass_model_footprint\main_routine_greyscale_ALL04.py
### apply model
C:\Users\robot\code\biomass_model_footprint\main_routine_composite_all04.py


### height

file data and remove site name: C:\Users\robot\code\biomass_model_footprint\automate_greyscale_ALL01_on_clipped_lsat_working_on.py

rerin height on 1000 clip: http://localhost:8888/notebooks/code/pipelines/clearing/lsat/height/lsat_run_tile_h99_hcv_hsd_hmc_seasonal_comp_pgb-bas20_21_all_years_10000_v2.ipynb

Run density on clipped data: http://localhost:8889/edit/code/pipelines/density/step1_density_lsat_all_years_10000.py


delete unused sub dirs in landsat_dir: http://localhost:8888/notebooks/code/AGB_deletae_unused_sub_dirs.ipynb

producing height: http://localhost:8888/notebooks/code/pipelines/clearing/lsat/height/lsat_run_tile_h99_hcv_hsd_hmc_seasonal_comp_pgb-bas20_21_all_years_10000_i_v2.ipynb
! 100000
## 10000 clip

create 10000 square clip from lsat dir
http://localhost:8891/notebooks/code/biomass/nb/clip_10000/clip_1000.ipynb

run height models: http://localhost:8888/notebooks/code/pipelines/clearing/lsat/height/lsat_run_tile_h99_hcv_hsd_hmc_seasonal_comp_pgb-bas20_21_all_years_10000_i_v2.ipynb

run density: gulf11

## Model timetrace:
predict scatterplot: http://localhost:8889/notebooks/code%2Fbiomass%2Fnb%2Fcollate_data%2Fcolate_agb_model_zonal_stats_scatter_plot.ipynb

http://localhost:8889/notebooks/code/biomass/nb/collate_data/colate_agb_model_zonal_stats_timetrace.ipynb

#### 105_070
jdr01
jdr02
jdr03
jdr04


all set to run: I:\Landsat\10000


## density

#### 105_070
jdr01 - run
jdr02 - run
jdr03 - run
jdr04 - run
jdr05 - run
jdr06 - running


## Report


Timetrace - model: http://localhost:8889/notebooks/code/biomass/nb/collate_data/colate_agb_model_zonal_stats_timetrace.ipynb


Upto here: http://localhost:8889/notebooks/code%2Fbiomass%2Fnb%2Fcollate_data%2Fcolate_agb_model_zonal_stats_scatter_plot.ipynb

http://localhost:8889/notebooks/code/biomass/nb/collate_data/colate_agb_model_zonal_stats_timetrace.ipynb

 need to apply carbon calculation to 
 
open

http://localhost:8888/notebooks/code/pipelines/clearing/lsat/height/lsat_run_tile_h99_hcv_hsd_hmc_seasonal_comp_pgb-bas20_21_all_years_10000_i_v2.ipynb

http://localhost:8889/notebooks/code/biomass/nb/collate_data/colate_agb_model_zonal_stats_timetrace.ipynb

http://localhost:8889/notebooks/code%2Fbiomass%2Fnb%2Fcollate_data%2Fcolate_agb_model_zonal_stats_scatter_plot.ipynb

http://localhost:8888/notebooks/code/AGB_deletae_unused_sub_dirs.ipynb

### outliers on clip data final models for report


http://127.0.0.1:8889/notebooks/code/biomass/nb/report/model_outliers_run_on_test_train.ipynb

data used for model: "H:\biomass\test_train3\AGB\all04_rs30\ABR\p99\AGB_all04_rs30_ABR_std3_p99_cleaned_df.csv"

separate plots and validation plots

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/seperate_validation_plots.ipynb

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/final_validation_scatter_and%20class_matrix.ipynb

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/final_timeseries_plots.ipynb


pre december
data that was used in teh models:

used in ABR GBR and RFR models random state 50
H:\biomass\test_train3\AGB\all04_rs30\ABR\p99\AGB_all04_rs30_ABR_std3_p99_cleaned_df.csv
"H:\biomass\test_train3\AGB\all04_rs30\ABR\p99\AGB_all04_rs30_ABR_std3_p99_cleaned_df.csv"
"H:\biomass\test_train3\AGB\all04_rs30\ABR\p99\AGB_all04_rs30_ABR_std3_p99_cleaned_df.csv"
Post December 2024

SILO SI check

http://localhost:8888/notebooks/code/biomass/nb/arcpro_silo_check.ipynb
missing data

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/concat_missing_data_csv.ipynb


PCA SILO and Fire:
http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/silo_fire_correlation_and_pca.ipynb
http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/silo_all_correlation.ipynb

Annual and dry season composite - before PCA
http://localhost:8888/notebooks/code/biomass/nb/clean_variables_for_ml/dry_annual_fire_mask_variable_correction_and_clean_for_ml_current.ipynb

Correlation and PCA

http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/silo_all_correlation.ipynb

http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/silo_rain_correlation.ipynb etc.
http://localhost:8889/notebooks/code/biomass/nb/statistical_analysis/silo_all_correlation_pca_run_after_fire_pca.ipynb
process fire data - run pipeline

http://localhost:8888/notebooks/code/biomass/nb/fire/looop_fire_analysis.ipynb

Calculate seasonal index:

http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/calculate_seasonal_index.ipynb

Concat missing data:

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/concat_missing_data_csv.ipynb

Delete missing file reports:

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/delete_missing_files_reports.ipynb

Clip data for 10000 composites:

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/clip_1000_partial_overlap_met.ipynb

Miscellaneous:

http://localhost:8888/notebooks/code/biomass/nb/ml/match_sitename_with_site_clean.ipynb
http://localhost:8888/notebooks/code/check_for_missing_sites_rename_collation.ipynb

2025 process


ouliers for latex:

http://localhost:8888/notebooks/code/biomass/nb/outliers/outliers_to_latex.ipynb
plot variables with ploty and test train split and visualisation

http://localhost:8890/notebooks/code/biomass/nb/statistical_analysis/ploty_agb_vrs_feature_plots.ipynb
http://localhost:8889/notebooks/code/biomass/nb/statistical_analysis/ploty_agb_vrs_feature_plots.ipynb

Var_select - run ru assess the model runs for the normalised best performign models

C:\Users\robot\code\biomass\var_select\test_train_all010203040506\concatinate_ml_metrics.ipynb

C:\Users\robot\code\biomass\var_select\code\test_train_all010203040506_v5\concatenate_ml_metrics_model_all010203040506_rs10_all02.ipynb

C:\Users\robot\code\biomass\var_select\code\test_train_all010203040506_v5\concatenate_ml_metrics_model_all010203040506_rs10_all03.ipynb



Feature importance scores are part of that

C:\Users\robot\code\biomass\var_select\code\test_train_all010203040506_v5\feature_importance_grouped_by_model.ipynb

Build model

http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank01_rs5_gbr_attemp1.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank01_rs5_gbr_attemp2.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank02_rs5_knn_attemp1.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank02_rs5_knn_attempt2.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank03_rs5_xgbr_attemp1.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank03_rs5_xgbr_attemp2.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank04_rs5_rfr_attemp1.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank04_rs5_rfr_attemp2.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank05_rs5_abr_attemp1.ipynb
http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Fall02_rank05_rs5_abr_attemp2.ipynb
http://localhost:8889/notebooks/code/biomass/ml/test_train_all010203040506/all03_rank01_rs5_knn_attemp1.ipynb

biomass/nb/ml


Apply models

zonal stats models

C:\Users\robot\code\pipelines\clip_10000_model_biomass_zonal_pipeline

Final validation: http://localhost:8889/notebooks/code/biomass/nb/clip_10000/final_validation_scatter_and%20class_matrix.ipynb

http://localhost:8889/notebooks/code/biomass/nb/clip_10000/final_validation_scatter_and%20class_matrix_check_all_sites.ipynb

# test and train split for better results

http://localhost:8889/notebooks/code/biomass/nb/report/test_train_final.ipynb

identify how many model files or comp files exist : http://localhost:8891/notebooks/code%2Fpipelines%2Fapply_biomass%2Fnb%2Fidentify_comp_files_in_comp_dirs.ipynb



Report

veg analysis: http://localhost:8888/notebooks/code/biomass/nb/species_list/vegetation_analysis.ipynb

good train test rs5 http://localhost:8889/notebooks/code/biomass/ml/test_train_all010203040506/all04_rank03_rs5_rfr_attempt2_plot.ipynb



### Redo validation plots to contain kg/ha

http://localhost:8889/notebooks/code%2Fbiomass%2Fml%2Ftest_train_all010203040506%2Freproduce_testing_plots.ipynbModel time series

http://localhost:8888/notebooks/code/biomass/nb/clip_10000/model_smoothed_line_timeseries_plots_v2.ipynb

## raster check

http://localhost:8888/notebooks/code/biomass/nb/raster_validation/raster_no_data_check.ipynb

basic stats:

http://localhost:8888/notebooks/code/biomass/nb/statistical_analysis/basic_statistics_of_dataset.ipynb

outliers:

http://localhost:8888/notebooks/code/biomass/nb/outliers/outliers_to_latex-Copy1.ipynb

all feature importance:

http://localhost:8888/notebooks/code/biomass/var_select/code/test_train_all010203040506_v5/feature_importance_grouped_by_model.ipynb


compare features normaised between model and itterations:

http://localhost:8888/notebooks/code/biomass/var_select/code/test_train_all010203040506_v5/feature_comparison_between_models.ipynb

feature comparisons: http://localhost:8888/notebooks/code/biomass/var_select/code/test_train_all010203040506_v5/feature_comparison_between_models.ipynb





