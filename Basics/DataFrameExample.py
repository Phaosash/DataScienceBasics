import pandas as pd

#   This example creates a data frame with 3 columns and 5 rows with fictional numbers
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

#   This counts the number of columns
count_column = df.shape[1]

print(f"Total number of Columns: {count_column}")

#   This counts the number of rows
row_count = df.shape[0]

print(f"Total number of rows: {row_count}")