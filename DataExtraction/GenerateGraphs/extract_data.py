import pandas as pd 
from helpers import select_user
from generate_graphs import generate_scatter_plot

df_all_users = pd.read_csv("../ConvertJSON/user_data.csv")
generate_scatter_plot(df_all_users)
#pd.set_option('display.max_columns', None)
#print(df_all_users)
# df_select_user = select_user(df_all_users, "Michael8pho")
# print(df_select_user.head())