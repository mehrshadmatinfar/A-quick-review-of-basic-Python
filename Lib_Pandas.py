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

# information
print('--- Info ---')
df.info()

# Indexing & Slicing
print('--- Indexing & Slicing ---')
# Indexing
print('--- Indexing ---')
print(df['ages'])
print(df[['ages', 'heights']])
# Slicing
print('--- Slicing ---')
print(df.iloc[2])
print(df.iloc[:3])
print(df.iloc[1:3])
print(df.head(1))  # return first row
print(df.tail(2))  # return last 2 rows
# Conditions
print('--- Conditions ---')
print(df[(df['ages'] > 18) & (df['heights'] > 180)])

# Save
df.to_csv('file/pd_01_df.csv')
df.to_excel('file/pd_01_df.xlsx')

df.to_csv('file/pd_02_df.csv', index=False)
df.to_excel('file/pd_02_df.xlsx', index=False)

df.to_csv('file/pd_03_df.csv', index=False, header=False)
df.to_excel('file/pd_03_df.xlsx', index=False, header=False, sheet_name='my sheet')

# Load
print('--- Load ---')
Loaded_df = pd.read_excel('file/pd_01_df.xlsx')
print(Loaded_df)
Loaded_df = pd.read_excel('file/pd_01_df.xlsx', index_col=0)
print(Loaded_df)

Loaded_df = pd.read_csv('file/pd_01_df.csv')
print(Loaded_df)
Loaded_df.set_index("ages", inplace=True)
print(Loaded_df)
Loaded_df.drop(labels='Unnamed: 0', axis=1, inplace=True)  # axis=1 for drop a column & axis=0 for drop a row
print(Loaded_df)
Loaded_df = pd.read_csv('file/pd_01_df.csv', index_col=0)
print(Loaded_df)

# Working with data
print('--- Working with data ---')
Loaded_df['age*height'] = Loaded_df['ages'] * Loaded_df['heights']
print(Loaded_df)
print(Loaded_df.describe())

# Grouping
print('--- Grouping ---')
another_df = pd.DataFrame(
    {
        'Grouping': [1, 1, 2, 1, 2, 3, 2, 3, 3],
        'ages': [10, 50, 32, 19, 81, 21, 24, 7, 4]
    }
)
print(another_df)
print(another_df.groupby('Grouping')['ages'].sum())

