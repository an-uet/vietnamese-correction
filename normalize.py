import re
import pandas as pd

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
    'uỳnh': 'ùynh',
    'uýnh': 'úynh',
    'uỷnh': 'ủynh',
    'uỹnh': 'ũynh',
    'uỵnh': 'ụynh',
    'uỳa': 'ùya',
    'uýa': 'úya',
    'uỷa': 'ủya',
    'uỹa': 'ũya',
    'uỵa': 'ụya',
    'oá(nh|ch|ng|p|n|t|c|m': 'óa(nh|ch|ng|p|n|t|c|m',
    'oà(nh|ch|ng|p|n|t|c|m': 'òa(nh|ch|ng|p|n|t|c|m',
    'oả(nh|ch|ng|p|n|t|c|m': 'ỏa(nh|ch|ng|p|n|t|c|m',
    'oã(nh|ch|ng|p|n|t|c|m': 'õa(nh|ch|ng|p|n|t|c|m',
    'oạ(nh|ch|ng|p|n|t|c|m': 'ọa(nh|ch|ng|p|n|t|c|m',
    'oè(t|n)': 'òe(t|n)',
    'oẻ(t|n)': 'ỏe(t|n)',
    'oé(t|n)': 'óe(t|n)',
    'oẽ(t|n)': 'õe(t|n)',
    'oẹ(t|n)': 'ọe(t|n)',
    'uý(n|t|p)': 'úy(n|t|p)',
    'uỷ(n|t|p)': 'ùy(n|t|p)',
    'uỹ(n|t|p)': 'ũy(n|t|p)',
    'uỵ(n|t|p)': 'ụy(n|t|p)'
}


def replace_all(text, dict_map):
    for i, j in dict_map.items():
        text = text.replace(j, i)
    return text


if __name__ == '__main__':
    # dict = {}
    # df = pd.read_csv("/home/anlt69/Downloads/thcsbevandan.csv")
    # for i, row in df.iterrows():
    #     row = row['row']
    #     match = re.search('\#\s*(?P<am>\w+)\–', row, flags=re.IGNORECASE)
    #     if match:
    #         result = match.group('am').lower()
    #         dict[result] = result
    # print(dict)

    text = 'thuý, huỳnh, quỳnh, '
    print(replace_all(text, dict_map))
