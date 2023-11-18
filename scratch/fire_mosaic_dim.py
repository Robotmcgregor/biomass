zonal_list = []
sub_dir_list = []
single_list = []
year_list = []
seasonal_list = []
dja_list = []
dbi_list = []
dim_list = []
dis_list = []
dka_list = []
dp0_list = []
dp1_list = []
h99a2_list = []
fpca2_list = []
stc_list = []

for sub_dir in sub_list:

    file_list = []
    if "zonal_stats" in sub_dir:
        sub_dir_list.append(sub_dir)
        print(sub_dir)
        print("looking in : ", os.path.join(dir_, sub_dir, "*.csv"))
        for file_ in glob(os.path.join(dir_, sub_dir, "*.csv")):
            print(file_)
            df = pd.read_csv(file_)
            file_list.append(df)
            print("appended: ", file_)

    if len(file_list) > 1:
        df1 = pd.concat(file_list)
        print("+" * 50)
        print(df1.shape)

        if "date" in df1.columns and "im_date" not in df1.columns:
            print(df1.columns)

            df1.rename(columns={"date": "im_date"}, inplace=True)

            print(df1.columns)

        print("+" * 50)
        print(sub_dir)
        print("+" * 50)

        if sub_dir == "dka_zonal_stats":
            #         if sub_dir == "dka_zonal_stats":
            print(df1.columns)
            dka = df1.copy()
            if "date" in dka.columns and "im_date" not in dka.columns:
                print(dka.columns)

                dka.rename(columns={"date": "im_date"}, inplace=True)
            dka = im_date_annual(dka)

            var_ = "dka"
            dka_dict = {"count": "{0}_count".format(var_),
                        "min": "{0}_min".format(var_),
                        "max": "{0}_max".format(var_),
                        "mean": "{0}_mean".format(var_),
                        "sum": "{0}_sum".format(var_),
                        "std": "{0}_std".format(var_),
                        "median": "{0}_med".format(var_),
                        "majority": "{0}_major".format(var_),
                        "minority": "{0}_minor".format(var_),
                        "one": "{0}_one".format(var_),
                        "two": "{0}_two".format(var_),
                        "three": "{0}_three".format(var_),
                        "four": "{0}_four".format(var_),
                        "five": "{0}_five".format(var_),
                        "six": "{0}_six".format(var_),
                        "seven": "{0}_seven".format(var_),
                        "eight": "{0}_eight".format(var_),
                        "nine": "{0}_nine".format(var_),
                        "ten": "{0}_ten".format(var_)}

            dka.rename(columns=dka_dict, inplace=True)

            dka_s = convert_to_datetime(dka, "s_date", "image_s_dt")
            dka_s.sort_values(by="s_date", inplace=True)
            dka_s.dropna(subset=['dka_min'], inplace=True)

            # call fire frequency etc functions
            dka_s = fire_percent_fn(dka_s)
            dka_s = fire_yn_fn(dka_s)
            dka_s = fire_intensity_fn(dka_s)
            dka_s = prop_fire_freq_fn(dka_s)
            dka_s = fire_previous_year(dka_s)
            dka_s = fire_gap_fn(dka_s)
            dka_s = poisson_fn(dka_s, 1, 2)
            dka_s = poisson_fn(dka_s, 1, 5)
            dka_s = poisson_fn(dka_s, 1, 10)

            #             dka_s.to_csv(os.path.join(temp_dir, "s_dkk.csv"), index=False)

            #             dka_s = fire_fn(dka_s)
            #             df = dka_s[dka_s['dka_min'].isnull()]
            #             print("+"*100)
            #             print(df.shape)
            dka_s.sort_values(by="image_s_dt", inplace=True)
            dka_s.dropna(subset=['dka_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dka_s_single = pd.merge_asof(basal_df, dka_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_dka_start.csv")
            dka_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            #             # -------------------------------------------------------------------------------------------------------------

            dka_e = convert_to_datetime(dka, "e_date", "image_e_dt")
            dka_e.sort_values(by="e_date", inplace=True)
            dka_e.dropna(subset=['dka_min'], inplace=True)

            #             dka_s = pd.read_csv(r"F:\cdu\data\ml_outputs\20230109\dkk_prior.csv")
            dka_e = fire_percent_fn(dka_e)
            dka_e = fire_yn_fn(dka_e)
            dka_e = fire_intensity_fn(dka_e)
            dka_e = prop_fire_freq_fn(dka_e)
            dka_e = fire_previous_year(dka_e)
            dka_e = fire_gap_fn(dka_e)
            dka_e = poisson_fn(dka_e, 1, 2)
            dka_e = poisson_fn(dka_e, 1, 5)
            dka_e = poisson_fn(dka_e, 1, 10)

            #             dka_e.to_csv(os.path.join(temp_dir, "e_dkk.csv"), index=False)

            dka_e.sort_values(by="e_date", inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dka_e_single = pd.merge_asof(basal_df, dka_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_dka_end.csv")
            dka_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            dis_list.append(df)
            print("Done")


        elif sub_dir == "dim_zonal_stats":
            print(df1.columns)
            dim = df1.copy()
            dim_s = convert_to_datetime(dim, "s_date", "image_s_dt")
            dim_s.sort_values(by="s_date", inplace=True)
            dim_s.dropna(subset=['b1_dim_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dim_s_single = pd.merge_asof(basal_df, dim_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_dim_start.csv")
            dim_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # -------------------------------------------------------------------------------------------------------------

            dim_e = convert_to_datetime(dim, "e_date", "image_e_dt")
            dim_e.sort_values(by="e_date", inplace=True)
            dim_e.dropna(subset=['b1_dim_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dim_e_single = pd.merge_asof(basal_df, dim_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_dim_end.csv")
            dim_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            print("Done")


        elif sub_dir == "dis_zonal_stats":
            print(df1.columns)
            dis = df1.copy()
            var_ = "dis"
            dis_dict = {"count": "{0}_count".format(var_),
                        "min": "{0}_min".format(var_),
                        "max": "{0}_max".format(var_),
                        "mean": "{0}_mean".format(var_),
                        "sum": "{0}_sum".format(var_),
                        "std": "{0}_std".format(var_),
                        "median": "{0}_med".format(var_),
                        "majority": "{0}_major".format(var_),
                        "minority": "{0}_minor".format(var_),
                        "one": "{0}_one".format(var_),
                        "two": "{0}_two".format(var_),
                        "three": "{0}_three".format(var_),
                        "four": "{0}_four".format(var_),
                        "five": "{0}_five".format(var_),
                        "six": "{0}_six".format(var_),
                        "seven": "{0}_seven".format(var_),
                        "eight": "{0}_eight".format(var_),
                        "nine": "{0}_nine".format(var_),
                        "ten": "{0}_ten".format(var_)}

            dis.rename(columns=dis_dict, inplace=True)

            dis_s = convert_to_datetime(dis, "s_date", "image_s_dt")
            dis_s.sort_values(by="s_date", inplace=True)
            dis_s.dropna(subset=['dis_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dis_s_single = pd.merge_asof(basal_df, dis_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_dis_start.csv")
            dis_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # -------------------------------------------------------------------------------------------------------------

            dis_e = convert_to_datetime(dis, "e_date", "image_e_dt")
            dis_e.sort_values(by="e_date", inplace=True)
            dis_e.dropna(subset=['dis_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dis_e_single = pd.merge_asof(basal_df, dis_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_dis_end.csv")
            dis_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # dis_list.append(df)
            print("Done")


        elif sub_dir == "dja_zonal_stats":

            print(df1.columns)
            dja = df1.copy()

            dja_s = convert_to_datetime(dja, "s_date", "image_s_dt")
            dja_s.sort_values(by="s_date", inplace=True)
            dja_s.dropna(subset=['b1_dja_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dja_s_single = pd.merge_asof(basal_df, dja_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_dja_start.csv")
            dja_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # -------------------------------------------------------------------------------------------------------------

            dja_e = convert_to_datetime(dja, "e_date", "image_e_dt")

            dja_e.sort_values(by="e_date", inplace=True)
            dja_e.dropna(subset=['b1_dja_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dja_e_single = pd.merge_asof(basal_df, dja_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_dja_end.csv")
            dja_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            print("Done")

        elif sub_dir == "dbi_zonal_stats":

            print(df1.columns)
            dbi = df1.copy()

            dbi_s = convert_to_datetime(dbi, "s_date", "image_s_dt")
            dbi_s.sort_values(by="s_date", inplace=True)
            dbi_s.dropna(subset=['b1_dbi_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dbi_s_single = pd.merge_asof(basal_df, dbi_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_dbi_start.csv")
            dbi_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # -------------------------------------------------------------------------------------------------------------

            dbi_e = convert_to_datetime(dbi, "e_date", "image_e_dt")
            dbi_e.sort_values(by="e_date", inplace=True)
            dbi_e.dropna(subset=['b1_dbi_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            dbi_e_single = pd.merge_asof(basal_df, dbi_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_dbi_end.csv")
            dbi_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # dbi_list.append(df)
            print("Done")


        elif sub_dir == "dp0_zonal_stats":
            dp0_list.append(df)

        elif sub_dir == "dp1_zonal_stats":
            dp1_list.append(df)

        elif sub_dir == "h99a2_zonal_stats":

            print(df1.columns)
            h99a2_annual = df1.copy()

            h99a2_annual = convert_to_datetime(h99a2_annual, "s_date", "image_s_dt")

            h99a2_annual_df = h99a2_annual[h99a2_annual["s_month"] == 1]
            h99a2_annual_df.sort_values(by="image_s_dt", inplace=True)
            h99a2_annual_df.dropna(subset=['b1_h99a2_min'], inplace=True)

            h99a2_annual = pd.merge_asof(basal_df, h99a2_annual_df, left_on="basal_dt", right_on="image_s_dt",
                                         by="site", direction="nearest")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_h99a2_annual.csv")
            h99a2_annual.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            print("Done")
            h99a2_list.append(df)

        elif sub_dir == "fpca2_zonal_stats":

            print(df1.columns)
            fpca2_dry = df1.copy()

            fpca2_dry = convert_to_datetime(fpca2_dry, "s_date", "image_s_dt")

            fpca2_dry_df = fpca2_dry[fpca2_dry["s_month"] == 5]
            fpca2_dry_df.sort_values(by="s_date", inplace=True)
            fpca2_dry_df.dropna(subset=['b1_fpca2_min'], inplace=True)

            fpca2_dry = pd.merge_asof(basal_df, fpca2_dry_df, left_on="basal_dt", right_on="image_s_dt", by="site",
                                      direction="nearest")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_fpca2_dry.csv")
            fpca2_dry.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            print("Done")
            # h99a2_list.append(df)

            fpca2_list.append(df)

        elif sub_dir == "stc_zonal_stats":
            print(df1.columns)
            stc = df1.copy()

            var_ = "stc"
            stc_dict = {"count": "{0}_count".format(var_),
                        "min": "{0}_min".format(var_),
                        "max": "{0}_max".format(var_),
                        "mean": "{0}_mean".format(var_),
                        "sum": "{0}_sum".format(var_),
                        "std": "{0}_std".format(var_),
                        "median": "{0}_med".format(var_),
                        "majority": "{0}_major".format(var_),
                        "minority": "{0}_minor".format(var_),
                        "one": "{0}_one".format(var_),
                        "two": "{0}_two".format(var_),
                        "three": "{0}_three".format(var_),
                        "four": "{0}_four".format(var_),
                        "five": "{0}_five".format(var_),
                        "six": "{0}_six".format(var_),
                        "seven": "{0}_seven".format(var_),
                        "eight": "{0}_eight".format(var_),
                        "nine": "{0}_nine".format(var_),
                        "ten": "{0}_ten".format(var_),
                        "eleven": "{0}_elev".format(var_),
                        "twelve": "{0}_twelv".format(var_),
                        "thirteen": "{0}_thirt".format(var_),
                        "fourteen": "{0}_fourt".format(var_),
                        "fifteen": "{0}_fift".format(var_),
                        "sixteen": "{0}_sixt".format(var_),
                        "seventeen": "{0}_sevent".format(var_)}

            stc.rename(columns=stc_dict, inplace=True)

            stc_s = convert_to_datetime(stc, "s_date", "image_s_dt")
            stc_s.sort_values(by="s_date", inplace=True)

            #           output_path = os.path.join(output_dir, "stc_before_drop_na.csv")
            #             stc_s.to_csv(os.path.join(output_path), index=False)
            #             print("File output to: ", output_path)

            stc_s.dropna(subset=['stc_min'], inplace=True)

            #             output_path = os.path.join(output_dir, "stc_after_drop_na.csv")
            #             stc_s.to_csv(os.path.join(output_path), index=False)
            #             print("File output to: ", output_path)

            # merge data with basal datset based on the nearest date to the field data colection
            stc_s_single = pd.merge_asof(basal_df, stc_s, left_on="basal_dt", right_on="image_s_dt", by="site",
                                         direction="forward")
            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_agb_nt_mosaic_stc_start.csv")
            stc_s_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            # -------------------------------------------------------------------------------------------------------------

            stc_e = convert_to_datetime(stc, "e_date", "image_e_dt")
            stc_e.sort_values(by="e_date", inplace=True)
            stc_e.dropna(subset=['stc_min'], inplace=True)

            # merge data with basal datset based on the nearest date to the field data colection
            stc_e_single = pd.merge_asof(basal_df, stc_e, left_on="basal_dt", right_on="image_e_dt", by="site",
                                         direction="backward")

            output_path = os.path.join(no_fire_scar_basal_dir, "merged_slats_field_abg_nt_mosaic_stc_end.csv")
            stc_e_single.to_csv(os.path.join(output_path), index=False)
            print("File output to: ", output_path)

            stc_list.append(df)
            print("Done")
        else:
            print("FAILED")
            print("+" * 50)
            print(sub_dir)
            print("+" * 50)

