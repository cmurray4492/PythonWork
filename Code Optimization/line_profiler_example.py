import csv
import random
from datetime import datetime, timedelta
import time


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


def process_transactions(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        transactions = []
        for row in reader:
            transaction = {}
            transaction['id'] = int(row['TransactionID'])
            transaction['customer_id'] = int(row['CustomerID'])
            transaction['date'] = row['Date']
            transaction['amount'] = float(row['Amount'])
            transaction['category'] = row['Category']
            transactions.append(transaction)

    # Perform some processing
    category_totals = {}
    for transaction in transactions:
        category = transaction['category']
        amount = transaction['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
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
