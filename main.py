from src.utils import read_transactions_json
from src.masks import get_mask_card_number, get_mask_account
import os
from config import DATA_DIR


if __name__ == '__main__':
    operations_path = os.path.join(DATA_DIR, 'operations.json')
    print(read_transactions_json(operations_path))
    print(get_mask_card_number('1596837868705199'))
    #print(get_mask_account('646473678894779589'))
