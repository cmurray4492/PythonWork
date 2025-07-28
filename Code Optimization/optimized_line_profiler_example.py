import csv
import random
from datetime import datetime, timedelta
import time
import pandas as pd


def create_sample_transactions_csv(filename, num_records):
    categories = ['Groceries', 'Electronics', 'Clothing', 'Utilities', 'Dining', 'Entertainment']
    start_date = datetime(2023, 1, 1)

    with open(filename, 'w', newline='') as file:
        fieldnames = ['TransactionID', 'CustomerID', 'Date', 'Amount', 'Category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, num_records + 1):
            transaction = {
                'TransactionID': i,
                'CustomerID': random.randint(1000, 5000),
                'Date': (start_date + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d'),
                'Amount': round(random.uniform(5.0, 500.0), 2),
                'Category': random.choice(categories)
            }
            writer.writerow(transaction)

    print(f"{filename} file created successfully with {num_records} records.")

@profile
def process_transactions(filename):
    dtypes = {'TransactionID': 'int32',
              'CustomerID': 'int32',
              'Date': 'string',
              'Amount': 'float64',
              'Category': 'string'}

    transaction_df = pd.read_csv(filename, dtype=dtypes)

    category_totals = transaction_df.groupby('Category')['Amount'].sum().to_dict()
    return category_totals


if __name__ == '__main__':
    input_file = 'transactions.csv'
    num_records = 5000000

    #create_sample_transactions_csv(input_file, num_records)

    start_time = time.time()
    totals = process_transactions(input_file)
    print(f'Execution time: {time.time() - start_time} seconds')
    for category, total in totals.items():
        print(f"Category: {category}, Total Amount: {total}")
