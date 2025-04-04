import pandas as pd
import seaborn as sns
df = sns.load_dataset('iris')
print("First few rows of the dataset:")
print(df.head())
print("\nDataset Info (Data types and missing values):")
print(df.info())
print("\nMissing values in the dataset:")
print(df.isnull().sum())
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())
grouped_data = df.groupby('species').mean()
print("\nMean values for each species:")
print(grouped_data)
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sales = [100, 120, 150, 170, 200, 250, 300, 280, 320, 350]

plt.figure(figsize=(8, 6))
plt.plot(days, sales, marker='o', linestyle='-', color='b')
plt.title('Sales Trend Over Time')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], bins=20, kde=True, color='green')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species', palette='Set1')
plt.title('Relationship Between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
try:
    df = pd.read_csv('your_dataset.csv') 
    print(df.head())
except FileNotFoundError:
    print("Error: The dataset file was not found.")
except pd.errors.EmptyDataError:
    print("Error: The dataset is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
