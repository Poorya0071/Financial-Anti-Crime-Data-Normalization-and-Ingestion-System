# generate_data.py
import random
import csv
from datetime import datetime, timedelta

def generate_transactions(num_transactions):
    transactions = []
    start_date = datetime.now() - timedelta(days=30)
    for _ in range(num_transactions):
        transaction_id = random.randint(100000, 999999)
        timestamp = start_date + timedelta(minutes=random.randint(0, 43200))
        account_number = f'ACC{random.randint(10000, 99999)}'
        amount = round(random.uniform(10.0, 10000.0), 2)
        transaction_type = random.choice(['deposit', 'withdrawal', 'transfer'])
        dest_account = f'ACC{random.randint(10000, 99999)}'
        geolocation = f'{random.uniform(-90, 90):.6f},{random.uniform(-180, 180):.6f}'
        
        transactions.append([
            transaction_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            account_number, amount, transaction_type,
            dest_account, geolocation
        ])
    
    return transactions

def write_to_csv(transactions, filename='transactions.csv'):
    headers = ['TransactionID', 'Timestamp', 'AccountNumber', 'Amount', 'TransactionType', 'DestinationAccount', 'Geolocation']
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(transactions)

if __name__ == "__main__":
    transactions = generate_transactions(1000)
    write_to_csv(transactions)
