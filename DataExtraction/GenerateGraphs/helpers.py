"""
Drop all other users from dataframe
"""
def select_user(df, user):
    df.drop(df[df["User"] != user].index, inplace = True)
    return df