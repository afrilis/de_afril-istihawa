import pandas as pd
import os
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

class DataWarehouseLoader:
    def __init__(self):
        cred = credentials.Certificate(r"C:\Users\user\OneDrive\Documents\GitHub\data-engineer_afril-istihawa\19_Code Competence 2 DE\Praktikum\accountKey.json")
        firebase_admin.initialize_app(cred, {
            "storageBucket": "code-com-2.appspot.com"
        })
        self.bucket = storage.bucket()

    def load_data(self, file_path):
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        merged_df = pd.merge(df_transactions, df_tickets, on='ticket_id', how='inner')
        merged_df = pd.merge(merged_df, df_events, on='event_id', how='inner')

        tickets_sold_per_event = merged_df.groupby('event_id')['quantity'].sum().reset_index()
        tickets_sold_per_event.columns = ['event_id', 'tickets_sold']

        revenue_per_event = merged_df.groupby('event_id')['total_amount'].sum().reset_index()

        if 'transaction_id' in df_customer_feedback.columns:
            feedback_analysis = pd.merge(df_customer_feedback, df_transactions, on='transaction_id', how='inner')
            if 'event_id' in feedback_analysis.columns:
                avg_rating_per_event = feedback_analysis.groupby('event_id')['rating'].mean().reset_index()
            else:
                avg_rating_per_event = pd.DataFrame()
        else:
            avg_rating_per_event = pd.DataFrame()

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

    def save_to_warehouse(self, df, table_name):
        current_date = datetime.now().strftime('%Y/%m/%d')
        os.makedirs(current_date, exist_ok=True)

        file_name = f"{current_date}_{table_name}.parquet"
        df.to_parquet(file_name, index=False)

        blob = self.bucket.blob(file_name)
        blob.upload_from_filename(file_name)
        print(f"Data berhasil disimpan di Firebase Storage: {file_name}")

if __name__ == "__main__":
    loader = DataWarehouseLoader()

    events_df = loader.load_data('parquet_files/events.parquet')
    customers_df = loader.load_data('parquet_files/customers.parquet')
    tickets_df = loader.load_data('parquet_files/tickets.parquet')
    transactions_df = loader.load_data('parquet_files/transactions.parquet')
    customer_feedback_df = loader.load_data('parquet_files/customer_feedback.parquet')

    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)

    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')
