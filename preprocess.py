import re
import pandas as pd
# import psycopg2
from tqdm import tqdm

OSM_HOST = '10.110.69.95'
OSM_PORT = '5432'
OSM_DB = 'openstreetmap'
OSM_USER = 'gmap_user'
OSM_PASSWORD = 'v78xzTArbexG8KKbmGaLvpTe'

OSM = {
    'host': OSM_HOST,
    'port': OSM_PORT,
    'database': OSM_DB,
    'user': OSM_USER,
    'password': OSM_PASSWORD
}

dict_map = {
    "òa": "oà",
    "Òa": "Oà",
    "ÒA": "OÀ",
    "óa": "oá",
    "Óa": "Oá",
    "ÓA": "OÁ",
    "ỏa": "oả",
    "Ỏa": "Oả",
    "ỎA": "OẢ",
    "õa": "oã",
    "Õa": "Oã",
    "ÕA": "OÃ",
    "ọa": "oạ",
    "Ọa": "Oạ",
    "ỌA": "OẠ",
    "òe": "oè",
    "Òe": "Oè",
    "ÒE": "OÈ",
    "óe": "oé",
    "Óe": "Oé",
    "ÓE": "OÉ",
    "ỏe": "oẻ",
    "Ỏe": "Oẻ",
    "ỎE": "OẺ",
    "õe": "oẽ",
    "Õe": "Oẽ",
    "ÕE": "OẼ",
    "ọe": "oẹ",
    "Ọe": "Oẹ",
    "ỌE": "OẸ",
    "ùy": "uỳ",
    "Ùy": "Uỳ",
    "ÙY": "UỲ",
    "úy": "uý",
    "Úy": "Uý",
    "ÚY": "UÝ",
    "ủy": "uỷ",
    "Ủy": "Uỷ",
    "ỦY": "UỶ",
    "ũy": "uỹ",
    "Ũy": "Uỹ",
    "ŨY": "UỸ",
    "ụy": "uỵ",
    "Ụy": "Uỵ",
    "ỤY": "UỴ",
}


def replace_all(text, dict_map):
    for i, j in dict_map.items():
        text = text.replace(i, j)
    return text


if __name__ == '__main__':

    f = open("data_train/addresses.txt", "r")
    f1 = open("data_train/data_train_ver02.txt", 'w')
    lines = f.readlines()
    new_lines = []
    for line in tqdm(lines, total=len(lines)):
        if line:
            line = line.lower()
            line = line.strip()
            match = re.search('[pf]\s*\.?\s*(?P<ward>\d+)\s*q\s*\.?\s*(?P<district>\d+)', line, flags=re.IGNORECASE)
            if match:
                ward = match.group('ward')
                district = match.group('district')
                line = re.sub(match.group(), f'phường {ward} quận {district}', line, flags=re.IGNORECASE)
            line = re.sub('\s+', ' ', line)
            line = replace_all(line, dict_map)
            line = line.strip()
            f1.write(line + '\n')

