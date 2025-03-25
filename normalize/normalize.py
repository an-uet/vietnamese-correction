import re
import unicodedata

import pandas as pd

from constants import *


# from constants import *
class Normalize:
    """some function for text pre-processing problem, import to use"""

    @classmethod
    def unicode_converter(cls, text):
        text = text.lower()
        for key in MAP_DICT_UNICODE:
            text = text.replace(key, MAP_DICT_UNICODE[key])
        return text

    @classmethod
    def normalize_text(cls, text):
        text = cls.unicode_converter(text)
        text = re.sub(r"([\(),-._{}\[\]<>?|\"\'=*&^%$#@!~`])", r" \1 ", text)
        text = re.sub("\s+", " ", text).strip()
        return text

    @classmethod
    def homo_glyph(cls, text: str) -> str:
        for x in standard_variations:
            text = re.sub(re.compile(standard_variations[x]), x, text)
        return text

    @classmethod
    def vietnamese_tone_normalize(cls, text):
        for i, j in VIETNAMESE_TONE_NORMALIZATION.items():
            text = re.sub(f'{j}(\s|\,|\.|$)', i + " ", text)
        return text

    @classmethod
    def fix_missing_space(cls, text: str) -> str:
        # f2q3 --> phường 2 quận 3
        match1 = re.search('((p|F|ph|ph[ưu][ơờo]ng)(\d+))((qu[aâa]n|q)(\d+))', text, flags=re.IGNORECASE)
        if match1:
            text = re.sub(match1.group(1), ' phường ' + match1.group(3), text)
            text = re.sub(match1.group(4), ' quận ' + match1.group(6), text)

        # 34/17nguyen duy --> 34/17 nguyen duy
        match2 = re.search('(\d)([a-zàáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹý]{4,})', text,
                           flags=re.IGNORECASE)
        if match2:
            text = re.sub(match2.group(), match2.group(1) + " " + match2.group(2), text, flags=re.IGNORECASE)

        # kp3 --> khu phố 3
        text = " " + text + " "
        all_prefix = PREFIX
        for prefix, true_form in all_prefix.items():
            missing_space = re.findall(fr"(\s{prefix}\s*\d+[a-z]?\s)", text)
            for missing_space_term in missing_space:
                fixed_term = re.sub(fr"{prefix}\s*", f"{true_form} ", missing_space_term)
                text = re.sub(missing_space_term, fixed_term, text)
        text = re.sub(r"(xã|phường|thị trấn|quận|huyện|thành phố|tỉnh)", r" \1 ", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def resolve_abbr(cls, text: str) -> str:
        for pattern, repl in RESOLVE_ABBR:
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def remove_emojis(cls, data):
        emoj = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030"
                          "]+", re.UNICODE)
        return re.sub(emoj, '', data)

    @classmethod
    def format_date_address(cls, text):
        formatted, n = re.subn(
            r'(?:(?<=\W)|(?<=^))([đd](([uưừ][oơờ]n)?g)?|p(hố|\.)|đại lộ)\s*(?P<day>\d{1,2})\s*(/|-|tháng)\s*(?P<month>\d{1,2})',
            lambda m: ('phố ' if m.group(1)[
                                     0].lower() == 'p' else 'đường ') + f"{m.group('day')} tháng {m.group('month')}",
            text, flags=re.IGNORECASE)
        if n == 0:
            formatted, n = re.subn(r'(?<=\d)\s+(?P<day>\d{1,2})\s*(tháng)\s*(?P<month>\d{1,2})',
                                   lambda m: ' đường ' + f"{m.group('day')} tháng {m.group('month')}",
                                   text, flags=re.IGNORECASE)
        if n == 0:
            if re.match(r'^[a-z0-9/]+\s+(?P<day>\d{1,2})\s*(-|/)\s*(?P<month>\d{1,2})$', text,
                        flags=re.IGNORECASE) is not None:
                formatted, n = re.subn(r'\s+(?P<day>\d{1,2})\s*(-|/)\s*(?P<month>\d{1,2})$',
                                       lambda m: ' đường ' + f"{m.group('day')} tháng {m.group('month')}",
                                       text, flags=re.IGNORECASE)
        if n > 0:
            match = re.search(r'(?P<day>\d{1,2}) tháng (?P<month>\d{1,2})', formatted)
            day, month = match.group('day'), match.group('month')
            if int(day) > 31 or int(month) > 12:
                return text
        return formatted

    @classmethod
    def format_address_element(cls, text, l):
        if int(l) in PATTERN_FORMAT_ADDRESS_ELEMENT.keys():
            pattern = PATTERN_FORMAT_ADDRESS_ELEMENT[int(l)]
            for x in pattern:
                label, regex, repl = x
                if label == l:
                    text = re.sub(regex, repl, text, flags=re.IGNORECASE)
            text = text.strip()
            text = re.sub('\s+', " ", text)
        return text

    @classmethod
    def clear_name(cls, text):
        text = unicodedata.normalize('NFC', text)
        text = text.lower()
        text = cls.homo_glyph(text)
        text = cls.vietnamese_tone_normalize(text)
        text = cls.normalize_text(text)
        text = cls.remove_emojis(text)
        text = cls.fix_missing_space(text)
        text = cls.resolve_abbr(text)
        text = cls.format_date_address(text)
        text = re.sub("(\/)+", "/", text)
        text = re.sub("\s*\/\s*", "/", text)
        text = re.sub(r"\s+", " ", text)

        match = re.search(
            '(?<!lô\s)([^\w\+]p|[^\w\+]q|kp|đ|tl|quận|huyện|phường|thị xã|khu phố|đường|dương|tổ|ấp|thôn|xóm)(\d+)',
            text)
        if match:
            # print(match.group())
            text = re.sub(match.group(), match.group(1) + ' ' + match.group(2), text)

        match_2 = re.search('(?<!lô\s)((ph|f)\s*\.?\s*)\d+', text, flags=re.IGNORECASE)
        if match_2:
            text = re.sub(match_2.group(1), 'p ', text)

        # 123/đường nguyễn trãi --> 123 nguyễn trãi
        match_3 = re.search("(\d+)\s*\/\s*(đường|đ\.?\s*|d\s)", text, flags=re.IGNORECASE)
        if match_3:
            text = re.sub(r"(\d+)\s*\/\s*(đường|đ\.?\s*|d\s)", match_3.group(1) + " đường ", text, flags=re.IGNORECASE)

        # 123 xec 45 --> 123/45
        match_4 = re.search('(\d+\w*\s*\,?)(x[oọ][eẹ]t|x[eẹ]c|sẹc)(\s*\d+)', text, flags=re.IGNORECASE)
        if match_4:
            text = re.sub(r'(\d+\w*\s*\,?\s*)(x[oọ][eẹ]t|x[eẹ]c|sẹc)(\s*\d+)',
                          match_4.group(1).strip() + '/' + match_4.group(3).strip(), text)

        # 134 trên 12 trên 456 --> 123/12/456
        match_5 = re.search(r'(\w?\d+\w?)(\strên\s)(\w?\d+\w?)', text, flags=re.IGNORECASE)
        if match_5:
            text = re.sub(match_5.group(2), '/', text)

        # số 123 ngách 12 14 15 hạ hồi -> ố 123 ngách 12/14/15 hạ hồi
        match_6 = re.search('(ngh?[aá]ch|ng[õỏo]|h[eẻ]m|ki[eêệ]t)\s(\d+\s\d+(\s\d+)+)', text, flags=re.IGNORECASE)
        if match_6:
            text = re.sub(match_6.group(2), re.sub('\s', '/', match_6.group(2)), text)

        # ct 2a -> ct2a:
        match_7 = re.search('(ct)\s*(\d+\w)', text, flags=re.IGNORECASE)
        if match_7:
            text = re.sub(match_7.group(), re.sub('\s', '', match_7.group()), text, flags=re.IGNORECASE)

        # 124/224/khu đô thi resco -> 124/224 khu đô thi resco
        match_8 = re.search('\d+\w?(\/)(\D{2,})*\s', text, flags=re.IGNORECASE)
        if match_8:
            text = re.sub(match_8.group(), re.sub(match_8.group(1), " ", match_8.group()), text, flags=re.IGNORECASE)

        # đương2/4 --> đường 2/4
        match_9 = re.search('(đương)(\d+)', text, flags=re.IGNORECASE)
        if match_9:
            text = re.sub(match_9.group(), re.sub(match_9.group(1), match_9.group(1) + " ", match_9.group()), text,
                          flags=re.IGNORECASE)
        # tổ_5khu --> tổ 5 khu
        match_10 = re.search('(\d+)(khu|t[ổoô]|ấp|buôn|bản|làng)', text, flags=re.IGNORECASE)
        if match_10:
            text = re.sub(match_10.group(), re.sub(match_10.group(1), match_10.group(1) + " ", match_10.group()), text,
                          flags=re.IGNORECASE)

        # 549, sẹc 45, sẹc 26A - Đường Xô Viết Nghệ Tĩnh --> 549/45/26a - đường xô viết nghệ
        match_11 = re.search('(\d+\w?)(\,?\s?(s[eéẹ]c|xo[eẹ]t|trên|phần)\s?\w?\d+\w?)+', text, flags=re.IGNORECASE)
        if match_11:
            text = re.sub(match_11.group(), re.sub('\,?\s?(s[eéẹ]c|xo[eẹ]t|trên|phần)\s?', '/', match_11.group()), text,
                          flags=re.IGNORECASE)

        # match_12 = re.search(r'\b(p(\s|\.))\s?([^\d\W])+', text, flags=re.IGNORECASE)
        # if match_12:
        #     text = re.sub(match_12.group(), re.sub(match_12.group(1), ", ", match_12.group()), text)

        # p_long_bửu,/phường long bình/quận 9 --> p_long_bửu, phường long bình quận 9
        match_13 = re.finditer('(,|\.|\s)([^\d\W])*\s*\/s*(,|\.|\s)?([^\d\W])*', text)
        for x in match_13:
            text = re.sub(x.group(), re.sub('\s*\/\s*', " ", x.group()), text)

        # 122 3 tháng 2 --> 122 đường 3 tháng 2
        match_14 = re.search('(?<!ph[ốôo]\s)((đ[uưừù][ơoờò]ng|đ|đg)(\s|\s*\.\s*))?(\d+\s*th[áa]ng)', text,
                             flags=re.IGNORECASE)
        if match_14:
            text = re.sub(match_14.group(), re.sub(match_14.group(), ' đường ' + match_14.group(4), match_14.group()),
                          text,
                          flags=re.IGNORECASE)
        match_15 = re.search('(s|r)\d+\s*\.\s*\d+', text)
        if match_15:
            text = re.sub(match_15.group(), re.sub('\s*', "", match_15.group()), text)

        # / 21 a --> /21a; / a 21 --> /a21
        match_16 = re.search(r'(\b[a-eg-or-z](\s)\d+)|(\b\d+(\s)[a-eg-or-z]\b)', text, flags=re.IGNORECASE)
        if match_16:
            # print('match_16', match_16.group())
            text = re.sub(match_16.group(), re.sub(' ', '', match_16.group()), text)

        text = re.sub('(\s*\,\s*)?ngách', ', ngách', text)
        text = re.sub(r'(\s*)\|(\s*)', r"\/", text)
        text = re.sub(r' \/', r'\/', text)
        text = re.sub(r"\/?\d{7,12}", "", text)
        text = re.sub("_", "", text)
        # Remove leading zero
        text = re.sub(r"(?<!(\d|\.))0+(\d|\s)", r"\2", text)
        text = re.sub(r"\s+", " ", text)
        text = unicodedata.normalize('NFC', text)
        text = text.strip()
        return text


if __name__ == '__main__':
    # s = 'Căn hộ B3.3 chung cư Rubyland, - Đường Lê Quát'
    p = "oà"
    s = 'vietinbank'
    # s = re.sub(f'{p}(\s|\,|\.|$)', 'òa ', s)
    # match_14 = re.search('((đ[uưừù][ơoờò]ng|đ|đg)(\s|\s*\.\s*))?(\d+\s*th[áa]ng)', s, flags=re.IGNORECASE)
    # if match_14:
    #     s = re.sub(match_14.group(), re.sub(match_14.group(), ' đường ' + match_14.group(4), match_14.group()), s,
    #                flags=re.IGNORECASE)
    print(Normalize.clear_name(s))
