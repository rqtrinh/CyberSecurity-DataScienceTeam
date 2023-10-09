import pandas as pd 
from .generate_graphs import *

def extract_data():
    df_all_users = pd.read_csv("DataExtraction/ConvertJSON/user_data.csv")
    generate_scatter_plot(df_all_users)
    generate_duration_correct_user(df_all_users)
    generate_duration_correct(df_all_users)
    generate_pi_chart(df_all_users)
    correct_vs_category(df_all_users)

    print("Generated all graphs \n")
