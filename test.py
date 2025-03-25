from transformers import pipeline
path_to_model = 'models/model'
path_to_model = 'anlt69/bartpho_1'
# path_to_model = 'anlt69/7_epoch'
# path_to_model='anlt69/vietnamese_correction_2'
# path_to_model='anlt69/test'
# path_to_model='models/model_ver03'
corrector = pipeline("text2text-generation", model=path_to_model)
import unicodedata



import unidecode
if __name__ == '__main__':
    import pandas as pd
    import re

    final_result = []
    df = pd.read_csv('data/full_data.csv')
    # addresses = list(df['name'])
    # for a in addresses:
    #     print(a)
    #     a = unicodedata.normalize('NFC', a)
    #     result = corrector(a.lower(), max_length=128)[0]['generated_text'].strip()
    #     print(result)
    #     x = (a, result)
    #     final_result.append(x)
    #     print('\n')
    #
    # final_result = pd.DataFrame(final_result, columns=['text', 'corrected_text'])
    # final_result.to_csv("data/validation.csv")
    # # text = 'd3/1d.ap 4xã lê minh xuân, huyện bình chánh, thành phố hồ chí minh'
    # # text = 'ph. ng hữSu huân'
    #
    # text = unicodedata.normalize('NFC', text)
    # print(corrector(text.lower(), max_length=128))

    final_result = []
    df = pd.read_csv('data/validation.csv')
    for i, row in df.iterrows():
        print(i)
        text = row['text']
        corrected_text = row['corrected_text']
        check = row['check']
        result = 0
        if text.lower().strip() == corrected_text.strip():
            result = 1
        x =(text, corrected_text, check, result)
        final_result.append(x)
    final_result = pd.DataFrame(final_result, columns=['text', 'corrected_text', 'check', 'result'])
    final_result.to_csv("data/validation.csv")

    # df = pd.read_csv("data/ward_district.csv")
    # result = []
    # for i, row in df.iterrows():
    #     name = row['name']
    #     print(name)
    #     true_name = row['summary']
    #     # match = re.search('[pf]\s*\.?\s*(?P<ward>\d+)\s*q\s*\.?\s*(?P<district>\d+)', name, flags=re.IGNORECASE)
    #     # if match:
    #     #     ward = match.group('ward')
    #     #     district = match.group('district')
    #     #     name = re.sub(match.group(), f'phường {ward} quận {district}', name, flags=re.IGNORECASE)
    #     #     name = name.lower()
    #     #     name = corrector(name)[0]['generated_text']
    #     name = name.lower()
    #     name = re.sub('\s+', ' ', name)
    #     name = name.strip()
    #
    #     true_name = true_name.lower()
    #     true_name = re.sub('\s+', ' ', true_name)
    #     true_name = true_name.strip()
    #     result.append((name, true_name))
    # result = pd.DataFrame(result, columns=['text', 'summary'])
    # result.to_csv('data/ward_district_process.csv')

