import os
from config import DATA_DIR
from src.transactions import read_transactions_csv


if __name__ == '__main__':
    operations_path = os.path.join(DATA_DIR, 'transactions.csv')
    print(read_transactions_csv(operations_path))
    # print(read_transactions_json(operations_path))
    # print(get_mask_card_number('1596837868705199'))
    #print(get_mask_account('646473678894779589'))
