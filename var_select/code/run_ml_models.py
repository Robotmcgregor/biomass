# GBR_all_data_w_met_sddv3_h99_add_knn_xgboost


import pandas as pd

pd.set_option('display.float_format', '{:.2f}'.format)
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.ensemble import ExtraTreesRegressor as etr
from sklearn.ensemble import GradientBoostingRegressor as gbr
from sklearn.ensemble import AdaBoostRegressor as abr
from sklearn.tree import DecisionTreeRegressor as dtr
from sklearn.neighbors import KNeighborsRegressor as knn
from xgboost import XGBRegressor as xgboost
from sklearn.model_selection import train_test_split
import scipy.stats as sc
import textwrap

# stats module
import statsmodels.api as sm
from statsmodels.tools.tools import add_constant
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.metrics import explained_variance_score

# import plotting and stats modules
import matplotlib.pyplot as plt
import seaborn as sns
import os
import scipy
import pandas as pd
import pandas as pd
from scipy.stats import zscore
import numpy as np

# Set option to display floating-point numbers without scientific notation
pd.set_option('display.float_format', lambda x: '%.2f' % x)

from bokeh.io import output_notebook, output_file
from bokeh.plotting import save  # figure, show,
#%matplotlib inline

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import make_scorer, mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
import numpy as np


# Function to detect outliers using Z-score
def detect_outliers(df, target_column):
    # Select only numeric columns except the target column
    numeric_df = df.select_dtypes(include=[np.number]).drop(columns=[target_column])

    # Calculate the Z-scores
    z_scores = np.abs(zscore(numeric_df))

    # Identify rows with Z-scores greater than 3 in any column
    outliers = (z_scores > 3).any(axis=1)

    return outliers


# Function to detect outliers using Z-score
def detect_outliers2(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])

    # Calculate the Z-scores
    z_scores = np.abs(zscore(numeric_df))

    # Identify rows with Z-scores greater than 3 in any column
    outliers = (z_scores > 3).any(axis=1)

    return outliers


def is_scientific_notation(value):
    # Function to check if a value is in scientific notation
    try:
        float_value = float(value)
        return '{:e}'.format(float_value) == value.lower()
    except ValueError:
        return False


def main_routine():
    rs = 0
    csv_file_list = [r"C:\Users\robot\projects\biomass\collated_zonal_stats\dry_mask\dp1_dbi_si_dry_mask_density.csv",

                     ]

    csv_type_lit = ["dp1_dbi_si_dry_mask_density",
                    ]

    for csv_file in csv_file_list:
        print("Working on {}".format(csv_file))
        var_ = os.path.split(csv_file[:-4])[1]

        print(var_)
        output = r"C:\Users\robot\projects\biomass\model_test\{}".format(var_)

        if not os.path.isdir(output):
            os.mkdir(output)

        for mdl in ["RFR", "ABR", "GBR", "KNN" "XGBR"]:
            print("Running model: {}".format(mdl))

            mdl_output = os.path.join(output, mdl)
            if not os.path.isdir(mdl_output):
                os.mkdir(mdl_output)

                # read as dataframe and copy
                df1 = pd.read_csv(csv_file, header=0)  # the first row is read in as the header for you columns
                print(df1.shape)  # prints out the number of rows and columns in your csv file 
                print(list(df1))
                df1.shape

                # Check for null values in each column
                columns_with_nulls = df1.columns[df1.isnull().any()]
                columns_with_nulls

                # Fill missing values with the minimum value of each column
                df1 = df1.apply(lambda col: col.fillna(col.min()), axis=0)

                df = df1.rename(columns={'bio_agb_kg1ha': 'target'})

                # ============================= Choose features =================

                for stats in ["mean", "h99"]:

                    df_columns = list(df.columns)
                    keep = ['site_clean', "target",
                            stats,
                            "major",
                            # "p99",
                            "GNDVI", "MSR", "NBR", "_NDVI", "CVI", "GDVI", "GSAVI",
                            "NDGI", "RI", "NDII", "MSAVI", "SAVI"
                                                           'r32', 'r42', 'r43',
                            'r52', 'r53', 'r54', 'r62', 'r63', 'r64', 'r65',

                            ]
                    header = [ele for ele in df_columns for x in keep if x in ele]
                    df2 = df[header]

                    # drop fdc - no need for this data

                    # Identify columns that contain "fdc" in their column names
                    columns_to_drop = df2.columns[df2.columns.str.contains("fdc", case=False)]

                    # Drop these columns
                    df2 = df2.drop(columns=columns_to_drop)

                    df_columns = list(df2.columns)
                    keep = ['major']

                    # create list of classified features for one hot encoding
                    classified_cols = [ele for ele in df_columns for x in keep if x in ele]
                    print(classified_cols)

                    # Check for duplicate columns and print them
                    duplicate_columns = df2.columns[df2.columns.duplicated()]

                    if duplicate_columns.any():
                        print("Duplicate columns found:")
                        for col in duplicate_columns:
                            print(col)
                    else:
                        print("No duplicate columns found.")

                    # Assuming df2 is your DataFrame with mixed data types and 'target' is the target column
                    df = df2.copy()

                    # Define the target column
                    target_column = 'target'  # Replace 'target' with the name of your target column

                    # Detect outliers
                    outliers = detect_outliers(df, target_column)

                    # Print the detected outliers
                    print("Detected Outliers:")
                    print(df[outliers])

                    # If you want to highlight these outliers in the original DataFrame
                    df_highlighted = df.copy()

                    for col in df.select_dtypes(include=[np.number]).drop(columns=[target_column]).columns:
                        df_highlighted[col + '_outlier'] = np.where(outliers, 'Outlier', 'Normal')

                    print("Original DataFrame with Outliers Highlighted:")
                    print(df_highlighted)

                    output_ = os.path.join(output, f"dry_mask_{var_}_not_target_outlier.csv")
                    df_highlighted.to_csv(output_, index=False)

                    # Assuming df2 is your DataFrame with mixed data types
                    df = df2.copy()

                    # Detect outliers
                    outliers = detect_outliers2(df)

                    # Print the detected outliers
                    print("Detected Outliers:")
                    print(df[outliers].site_clean)

                    # Drop rows that contain outliers
                    df_cleaned = df[~outliers]

                    print("Cleaned DataFrame (without outliers):")

                    for i in classified_cols:
                        df2 = pd.get_dummies(df2, columns=[i], prefix=f'{i}_en')

                    df_ml = df2

                    # drop some of the unwanted values
                    df_ml.drop(['site_clean', ], axis=1, inplace=True)

                    print(list(df_ml))

                    for samp in ["all_data", "10x0"]:
                        if samp == "all_data":
                            out_df = df_ml
                        elif samp == "10x0":
                            sample_size = 10
                            no_0_df = df_ml[df_ml['target'] > 0.0]

                            agb_0 = df_ml[df_ml['bio_agb_kg1ha'] == 0.0].sample(sample_size)
                            out_df = pd.concat([no_0_df, agb_0])
                            out_df.to_csv(os.path.join(output, "ml_df_0_sample_{0}kgha.csv".format(str(sample_size))))
                        else:
                            import sys
                            sys.exit("Invalid sample size")

                    # All variables
                    df_ml = out_df

                    # df_ml.to_csv(, index=False)
                    df_ml.to_csv(os.path.join(output, "{0}_{1}_{2}_ml_data.csv".format(var_, mdl, samp)), index=False)

                    # Check for scientific notation in each cell
                    for column in df_ml.columns:
                        for value in df_ml[column]:
                            if is_scientific_notation(str(value)):
                                print(f"Column {column}: {value} is in scientific notation")

                    value_x = "target"

                    # randomly split data into train and test datasets, the user needs to define the variables
                    xdata1 = df_ml.iloc[:, 1:].astype('float32')
                    ydata1 = df_ml[[value_x]].astype('float32')
                    ydata2 = ydata1.values
                    ydata = ydata2.ravel()
                    # y_data_float=ydata.astype("float32")
                    x_validation, x_remaining, y_validation, y_remaining = train_test_split(xdata1, ydata,
                                                                                            train_size=0.20,
                                                                                            random_state=rs)
                    x_train, x_test, y_train, y_test = train_test_split(x_remaining, y_remaining, train_size=0.70,
                                                                        random_state=rs)
                    print(x_validation.shape, y_validation.shape)
                    print("remaining.....")
                    print(x_remaining.shape, y_remaining.shape)
                    print("-" * 50)
                    print(x_train.shape, y_train.shape)
                    print(x_test.shape, y_test.shape)

                    # =======================================================================
                    # Create subplots: 1 row, 3 columns
                    fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Adjust figsize as needed

                    # Define the data and titles for each subplot
                    data = [y_train, y_test, y_validation]
                    titles = ['Training Data Distribution', 'Testing Data Distribution', 'Validation Data Distribution']

                    for i, (data_set, title) in enumerate(zip(data, titles)):
                        mean = np.mean(data_set)
                        median = np.median(data_set)

                        # Plot histogram with seaborn
                        sns.histplot(data_set, kde=True, bins=20, ax=axs[i], color='blue', alpha=0.7)

                        # Plot mean and median lines
                        axs[i].axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
                        axs[i].axvline(median, color='green', linestyle='dashed', linewidth=2,
                                       label=f'Median: {median:.2f}')

                        axs[i].set_title(title, fontsize=16)
                        axs[i].set_xlabel('Target', fontsize=14)
                        axs[i].set_ylabel('Frequency', fontsize=14)
                        axs[i].legend(fontsize=12)

                    # Adjust layout
                    plt.tight_layout()

                    # Save the figure
                    out = os.path.join(output, "plots", f"{var_}_{mdl}_{rs}_train_test_validation_distribution.JPG")
                    plt.savefig(out, dpi=300)
                    #plt.show()

                    print("saved to: ", out)

                    # ======================================= Grid search =======================

                    if mdl == "RFR":
                        from sklearn.ensemble import RandomForestRegressor as rfr

                        # Define model
                        model = rfr()

                        # Define parameter grid
                        param_grid = {
                            'n_estimators': [50, 100, 150, 200, 300],
                            'max_depth': [None, 2, 3, 4, 5, 10, 20],
                            'max_features': ['auto', 'sqrt'],
                            'bootstrap': [True, False]
                        }

                    elif mdl == "GBR":
                        from sklearn.ensemble import GradientBoostingRegressor as gbr

                        # Define model
                        model = gbr()

                        # Define parameter grid
                        param_grid = {
                            'n_estimators': [50, 100, 150, 200, 300],
                            'learning_rate': [0.01, 0.1, 1.0],
                            'max_depth': [3, 5, 7],
                        }

                    elif mdl == "ABR":
                        from sklearn.ensemble import AdaBoostRegressor as abr

                        # Define model
                        model = abr()

                        # Define parameter grid
                        param_grid = {
                            'n_estimators': [50, 100, 150, 200, 300],
                            'learning_rate': [0.01, 0.1, 1.0],
                        }

                    elif mdl == "XGBR":
                        from xgboost import XGBRegressor as xgboost

                        # Define model
                        model = xgboost()

                        # Define parameter grid
                        param_grid = {
                            'n_estimators': [50, 100, 150, 200, 300],
                            'learning_rate': [0.01, 0.1, 0.3],
                            'max_depth': [3, 5, 7],
                            'subsample': [0.6, 0.8, 1.0],
                            'colsample_bytree': [0.6, 0.8, 1.0],
                        }

                    elif mdl == "KNN":
                        from sklearn.neighbors import KNeighborsRegressor as knn

                        # Define model
                        model = knn()

                        # Define parameter grid
                        param_grid = {
                            'n_neighbors': [3, 5, 7, 10, 15],
                            'weights': ['uniform', 'distance'],
                            'p': [1, 2]  # p=1 is for Manhattan distance, p=2 is for Euclidean distance
                        }

                    else:
                        print("ERROR__" * 100)

                    # Define custom scorers for RMSE, MAE, R2
                    def custom_rmse_scorer(y_true, y_pred):
                        return -np.sqrt(mean_squared_error(y_true, y_pred))

                    def custom_mae_scorer(y_true, y_pred):
                        return -mean_absolute_error(y_true, y_pred)

                    def custom_r2_scorer(y_true, y_pred):
                        return r2_score(y_true, y_pred)

                    r2_scorer = make_scorer(custom_r2_scorer)
                    rmse_scorer = make_scorer(custom_rmse_scorer)
                    mae_scorer = make_scorer(custom_mae_scorer)

                    # Create GridSearchCV objects
                    grid_search_rmse = GridSearchCV(model, param_grid, scoring=rmse_scorer, cv=5)
                    grid_search_rmse.fit(x_train, y_train)

                    # ----------------------------- RMSE ---------------------------------
                    print(mdl)
                    print("-" * 100)
                    print("RMSE Best Score: ", grid_search_rmse.best_score_)
                    print("RMSE Best Parameters: ", grid_search_rmse.best_params_)

                    grid_search_mae = GridSearchCV(model, param_grid, scoring=mae_scorer, cv=5)
                    grid_search_mae.fit(x_train, y_train)

                    # ----------------------------- MAE ---------------------------------
                    print("MAE Best Score: ", grid_search_mae.best_score_)
                    print("MAE Best Parameters: ", grid_search_mae.best_params_)

                    grid_search_r2 = GridSearchCV(model, param_grid, scoring=r2_scorer, cv=5)
                    grid_search_r2.fit(x_train, y_train)

                    # ----------------------------- R2 ---------------------------------
                    print("R2 Best Score: ", grid_search_r2.best_score_)
                    print("R2 Best Parameters: ", grid_search_r2.best_params_)

                    for matrix in ["R2", "MAE", "RSME"]:

                        matrix_output = os.path.join(mdl_output, matrix)
                        if not os.path.isdir(matrix_output):
                            os.mkdir(matrix_output)

                        if matrix == "R2":
                            # Get best r2 parameters
                            # best_params = grid_search_r2.best_params_
                            best_model = grid_search_r2.best_estimator_
                            fac = "r2"
                            p_out = matrix_output
                            print("r2 Best Score: ", grid_search_r2.best_score_)
                            print("r2Best Parameters: ", grid_search_r2.best_params_)
                            print(best_model)

                        elif matrix == "MAE":

                            # best_params = grid_search_rmse.best_params_
                            best_model = grid_search_mae.best_estimator_
                            fac = "MAE"
                            p_out = matrix_output
                            print("MAE Best Score: ", grid_search_mae.best_score_)
                            print("MAE Best Parameters: ", grid_search_mae.best_params_)
                            print(best_model)

                        elif matrix == "RSME":
                            # best_params = grid_search_rmse.best_params_
                            best_model = grid_search_rmse.best_estimator_
                            fac = "RMSE"
                            p_out = matrix_output
                            print("RMSE Best Score: ", grid_search_rmse.best_score_)
                            print("RMSE Best Parameters: ", grid_search_rmse.best_params_)
                            print(best_model)
                        else:
                            import sys
                            sys.exit()





    if __name__ == '__main__':
        main_routine()
