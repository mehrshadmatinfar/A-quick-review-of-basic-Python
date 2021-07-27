import pandas as pd

# Creating DataFrames
Dictionary = {
    'ages': [14, 19, 24, 40],
    'heights': [163, 170, 175, 184]
}
df = pd.DataFrame(Dictionary)
print(type(Dictionary))  # <class 'dict'>
print(Dictionary)  # {'ages': [14, 19, 24, 40], 'heights': [163, 170, 175, 184]}
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(df)
df = pd.DataFrame(Dictionary, index=['Bob', 'Ali', 'James', 'Dave'])
print(df)
print(df.loc["Bob"])

# Indexing & Slicing
print('--- Indexing & Slicing ---')
# Indexing
print(df['ages'])
print(df[['ages', 'heights']])
# Slicing
print(df.iloc[2])
print(df.iloc[:3])
print(df.iloc[1:3])
# Conditions
print(df[(df['ages'] > 18) & (df['heights'] > 180)])

