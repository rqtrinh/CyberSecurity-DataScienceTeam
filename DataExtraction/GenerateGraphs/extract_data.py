import pandas as pd 
from helpers import select_user

df_all_users = pd.read_csv("user_data.csv")
pd.set_option('display.max_columns', None)
df_select_user = select_user(df_all_users, "Michael8pho")
print(df_select_user)