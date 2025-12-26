import pandas as pd
res = pd.DataFrame([[1,2,3,4,5]], columns = ['a','b','c','d','e']);
print(res);

#################################################################################################################################

import pandas as pd
Data = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]], columns = ['a','b','c','d','e'], index =['R1','R2','R3']);
print(Data)

####################################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
dis_data = {
            "EmpName":['Anurag','Sarthak','Sagar','Aman'],
            "EmpAge": [20,22,24,26],
            "Salary": [25000,30000,45000,60000]
};

df = pd.DataFrame(dis_data);

# Create a line chart fir the 'Salary' Column:
df['Salary'].plot(kind='line')
plt.title("Sales Distribution")
plt.ylabel("Salary") 
#PNG,JPG,PDF :
plt.savefig("sales_pie_chart.png", dpi=300, bbox_inches='tight');
#plt.show()

#################################################################################################################################
#IMPORT FILE :
import pandas as pd

# Load dataset
df = pd.read_csv('./IT_Employees_Info_2000.csv')

# Rename column and export file
df.rename(columns={"Salary": 'AnnualSalary'}, inplace=True)
df.to_csv('IT_Employees_Info_2000.csv', index=False)
print("File updated")

#############################################################################################################################
# Basic and Common DataFrame Functions

print(df.tail())              # Show last 5 Rows
print(df.info())              # Info about dataset
print(df.describe())          # Statistical summary
print(df.columns)             # Column names
print(df.index)               # Index info
print(df.shape)               # Shape (rows, columns)
print(df.dtypes)              # Data types
print(df.reset_index())       # Reset index

#############################################################################################################################
# Advanced DataFrame Functions and File Operation

print(df.loc[1, ['Name', 'Department']])
print(df.iloc[3, 3])  # 4th row, 4th column (0-based index)

# Add new column: Bonus
df['Bonus'] = df['AnnualSalary'] * 0.10
print("\nAdded new column 'Bonus':\n", df[['Name', 'AnnualSalary', 'Bonus']].head())

# Add TotalPay column
df['TotalPay'] = df['AnnualSalary'] + df['Bonus']
print("\nSalary + Bonus = TotalPay:\n", df[['Name', 'AnnualSalary', 'Bonus', 'TotalPay']].head())

#############################################################################################################################
# Example 2: Basic Functions

df = pd.read_csv('./IT_Employees_Info_2000.csv')

print("1. DataFrame:")
print(df)

print("\n2. First 3 rows:")
print(df.head(3))

print("\n3. Last 2 rows:")
print(df.tail(2))

print("\n4. DataFrame info:")
df.info()

print("\n5. Statistical summary:")
print(df.describe())

print("\n6. Column names:")
print(df.columns)

print("\n7. Index values:")
print(df.index)

print("\n8. Shape (rows, columns):")
print(df.shape)

print("\n9. Data types:")
print(df.dtypes)

print("\n11. Reset index:")
print(df.reset_index())

print("\n12. Sort by 'AnnualSalary':")
print(df.sort_values(by='AnnualSalary'))

print("\n13. Rename column 'Salary' to 'AnnualSalary':")
print(df.rename(columns={'Salary': 'AnnualSalary'}))

print("\n14. Select single column 'Name':")
print(df['Name'])

print("\n15. Select multiple columns 'Name' and 'Department':")
print(df[['Name', 'Department']])

print(df.loc[5, ['Name', 'Department']])
print(df.iloc[0, 3])  # third column value

# Add new column
df['Newcolumn'] = 50
print("\nAfter adding Newcolumn:\n", df)

# Add a 'Bonus' column
df['Bonus'] = df['AnnualSalary'] * 0.10
print("\nAdd new column 'Bonus':\n", df[['Name', 'AnnualSalary', 'Bonus']].head())

# Add 'Bonus' only for Ankit
df['Bonus'] = df['Name'].apply(lambda x: 53 if x == 'Ankit' else 0)
print("\nAfter adding Bonus only for Ankit:\n", df)

# Add Bonus for Ankit and Ali
df['Bonus'] = df['Name'].apply(lambda x: 58 if x in ['Ankit', 'Ali'] else 0)
print("\nAfter adding Bonus for Ankit and Ali:\n", df)

# Arithmetic operation between columns
df['TotalPay'] = df['AnnualSalary'] + df['Bonus']
print("\nSalary + Bonus = TotalPay:\n", df[['Name', 'AnnualSalary', 'Bonus', 'TotalPay']].head())

# Replace values
df['Name'] = df['Name'].replace({'Helen  ': 'Bobby'})
print("\nAfter replace:\n", df)

print("\nReplace 'IT' ➜ 'Tech':\n", df.replace({'HR': 'Tech'}).head())

# Duplicates check and removal
df = df.drop_duplicates(subset=['Gender'])
print("\n1️⃣ Drop duplicates:\n", df.drop_duplicates().head())

#############################################################################################################################
# Concatenate and Merge Examples

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Ankit', 'Ankita', 'Anisha', 'Ali'],
    'Score': [85, 90, 95, 90]
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5],
    'City': ['Delhi', 'Mumbai', 'Chennai']
})

# Concatenate DataFrames
combined = pd.concat([df1, df2])
print("\nConcatenated DataFrame:\n", combined)

# Merge DataFrames
print("\nInner join on 'ID':")
print(pd.merge(df1, df2, how='inner', on='ID'))

print("\nOuter join on 'ID':")
print(pd.merge(df1, df2, how='outer', on='ID'))

print("\nLeft join on 'ID':")
print(pd.merge(df1, df2, how='left', on='ID'))

print("\nRight join on 'ID':")
print(pd.merge(df1, df2, how='right', on='ID'))

#############################################################################################################################
# Aggregations

df = pd.read_csv('./IT_Employees_Info_2000.csv')

print("\n1. Sum:\n", df.sum(numeric_only=True))
print("\n2. Mean:\n", df.mean(numeric_only=True))
print("\n3. Count:\n", df.count())
print("\n4. Min:\n", df.min(numeric_only=True))
print("\n5. Max:\n", df.max(numeric_only=True))
print("\n6. Median:\n", df.median(numeric_only=True))
print("\n7. Std:\n", df.std(numeric_only=True))

# Group by example
mean_by_dept = df.groupby('Department')[['AnnualSalary']].max()
print(mean_by_dept)

# Pivot table
print(pd.pivot_table(df, values='AnnualSalary', index='Department'))

# Crosstab example
print(pd.crosstab(df['Department'], df['Age']))

#############################################################################################################################
# Date Example

df = pd.DataFrame({
    'JoinDate': ['2022-01-15', '2021-07-10', '2023-03-05', '2020-11-20']
})
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['JoinYear'] = df['JoinDate'].dt.year
print(df)

#############################################################################################################################
