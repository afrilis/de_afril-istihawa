import pandas as pd
import numpy as np
import os

class DataLakeBuilder:
    def read_csv_data(self, data_source):
        return pd.read_csv(data_source)
    
    def handle_missing_values(self, df):
        return df.fillna(method='ffill').fillna(method='bfill')
    
    def handle_outliers(self, df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), df[column].median(), df[column])
        return df
    
    def save_to_parquet(self, df, file_parquet):
        df.to_parquet(file_parquet)
    
    def validate_data(self, file_parquet):
        df = pd.read_parquet(file_parquet)
        print("Summary Statistics:")
        print(df.describe())
        print("\nSample Data:")
        print(df.head())

if __name__ == "__main__":
    # Create an instance of DataLakeBuilder
    data_lake_builder = DataLakeBuilder()
    
    # List of CSV files
    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    
    # Directory to store Parquet files
    parquet_dir = 'parquet_files'
    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)
    
    # Process each CSV file
    data_source_dir = r'C:\Users\user\OneDrive\Documents\GitHub\data-engineer_afril-istihawa\19_Code Competence 2 DE\data_source'
    for file in csv_files:
        # Read data from CSV
        file_path = os.path.join(data_source_dir, file)
        df = data_lake_builder.read_csv_data(file_path)
        
        # Handle missing values
        df = data_lake_builder.handle_missing_values(df)
        
        # Handle outliers (assuming numeric columns)
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for column in numeric_columns:
            df = data_lake_builder.handle_outliers(df, column)
        
        # Save to Parquet
        parquet_file = os.path.join(parquet_dir, file.split('.')[0] + '.parquet')
        data_lake_builder.save_to_parquet(df, parquet_file)
        
    # Validate data
    for file in os.listdir(parquet_dir):
        parquet_file_path = os.path.join(parquet_dir, file)
        print(f"\nValidating data from {parquet_file_path}:")
        data_lake_builder.validate_data(parquet_file_path)
