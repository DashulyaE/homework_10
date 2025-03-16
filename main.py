import os
from config import DATA_DIR
from src.transactions import read_transactions_csv, read_transactions_excel


if __name__ == "__main__":
    operations_path = os.path.join(DATA_DIR, "transactions.csv")
    operations_path_ex = os.path.join(DATA_DIR, "transactions_excel.xlsx")
    print(read_transactions_csv(operations_path))
    print(read_transactions_excel(operations_path_ex))
