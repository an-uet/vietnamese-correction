MAP_DICT_UNICODE = {'à': u'à', 'á': u'á', 'ả': u'ả', 'ã': u'ã', 'ạ': u'ạ', 'ằ': u'ằ', 'ắ': u'ắ', 'ẳ': u'ẳ',
                    'ẵ': u'ẵ', 'ặ': u'ặ', 'ầ': u'ầ',
                    'ấ': u'ấ', 'ẩ': u'ẩ', 'ẫ': u'ẫ', 'ậ': u'ậ', 'è': u'è', 'é': u'é', 'ẻ': u'ẻ', 'ẽ': u'ẽ',
                    'ẹ': u'ẹ', 'ề': u'ề', 'ế': u'ế', 'ể': u'ể', 'ễ': u'ễ',
                    'ệ': u'ệ', 'ò': u'ò', 'ó': u'ó', 'ỏ': u'ỏ', 'õ': u'õ', 'ọ': u'ọ', 'ồ': u'ồ', 'ố': u'ố',
                    'ổ': u'ổ', 'ỗ': u'ỗ', 'ộ': u'ộ', 'ờ': u'ờ', 'ớ': u'ớ',
                    'ở': u'ở', 'ỡ': u'ỡ', 'ợ': u'ợ', 'ù': u'ù', 'ú': u'ú', 'ủ': u'ủ', 'ũ': u'ũ', 'ụ': u'ụ',
                    'ừ': u'ừ', 'ứ': u'ứ', 'ử': u'ử', 'ữ': u'ữ', 'ự': u'ự',
                    'ì': u'ì', 'í': u'í', 'ỉ': u'ỉ', 'ĩ': u'ĩ', 'ị': u'ị', 'ỳ': u'ỳ', 'ý': u'ý', 'ỷ': u'ỷ',
                    'ỹ': u'ỹ', 'ỵ': u'ỵ'}

# Normalize unicode
standard_variations = {
    "a": "[ɑαаａäå𝐚]",
    "A": "[ΑᎪＡÄÅА]",
    "Ă": "Ǎ",
    "Ấ": "Ấ",
    "ạ": "ạ",
    "à": "à",
    "á": "á",
    "ả": "ả",
    "ấ": "ấ",
    "ă": "ǎ",
    "ắ": "ắ",
    "ằ": "ằ",
    "ặ": "ặ",
    "ầ": "ầ",
    "ẩ": "ẩ",
    "ậ": "ậ",
    "b": "[Ьｂ]",
    "B": "[ßʙΒβВᏴᛒＢ]",
    "c": "[ϲсⅽｃ]",
    "C": "[ϹСᏟⅭＣČ]",
    "d": "[ďԁժḍⅾｄ]",
    "D": "[ĎᎠⅮＤ]",
    "đ": "[ð]",
    'Đ': "[ÐƉ]",
    "e": "[ËëĒēĔĕĖėĘĚěΕЕеᎬＥｅ𝐞]",
    "E": "[ËëĒēĔĕĖėĘĚěΕЕеᎬＥｅ]",
    "ẻ": "ẻ",
    "ề": "ề",
    "ế": "ế",
    "ễ": "ễ",
    "ệ": "ệ",
    "f": "[ｆ]",
    "F": "[ϜＦ]",
    "g": "[ɡｇ]",
    "G": "[ɢԌնᏀＧ]",
    "h": "[һｈ]",
    "H": "[ʜΗНᎻＨн]",
    "i": "[ɩіاᎥᛁⅰｉï𝐢]",
    "I": "[ΙІⅠＩ]",
    "ị": "(ị|[į])",
    "í": "í",
    "ì": "ì",
    "ĩ": "ĩ",
    "j": "[ϳјյｊ]",
    "J": "[ЈᎫＪ]",
    "k": "[κｋ]",
    "K": "[ΚКᏦᛕKＫ]",
    "l": "[ιاⅼｌ]",
    "L": "[ʟᏞⅬＬ]",
    "m": "[ⅿｍ]",
    "M": "[ΜϺМᎷᛖⅯＭ𝐌]",
    "n": "[ｎñ]",
    "N": "[ɴΝＮ𝐧]",
    "o": "[οоｏ𝐨ö]",
    "O": "[ΟОՕＯ]",
    "ọ": "ọ",
    "ó": "ó",
    "ò": "ò",
    "õ": "õ",
    "ộ": "ộ",
    "ố": "(ố|ố)",
    "ồ": "ồ",
    "ờ": "(ờ|ờ)",
    "ớ": "(ớ|ớ́)",
    "ợ": "ợ",
    "p": "[ρрｐ]",
    "P": "[ΡРᏢＰ]",
    "q": "[ႭႳＱ𝐪]",
    "Q": "[ｑ]",
    "r": "[Իｒ]",
    "R": "[ʀᏒᚱＲ]",
    "s": "[ѕｓ𝐬]",
    "S": "[ЅՏႽᏚＳ]",
    "t": "[ｔ𝐭]",
    "T": "[ΤτТᎢＴ]",
    "u": "[μυｕü𝐮]",
    "U": "[ԱՍ⋃Ｕ]",
    "ú": "(ú|ű)",
    "ủ": "ủ",
    "ụ": "ụ",
    "ừ": "ừ",
    "ữ": "ữ",
    "v": "[νѵⅴｖ]",
    "V": "[ѴᏙⅤＶ]",
    "w": "[ѡｗ]",
    "W": "[ᎳＷ]",
    "x": "[χхⅹｘ×]",
    "X": "[ΧХⅩＸ]",
    "y": "[ʏγуｙ𝐲]",
    "Y": "[ΥҮＹ]",
    "ỳ": "ỳ",
    "ỹ": "ỹ",
    "z": "[ｚ]",
    "Z": "[ΖᏃＺ]"
}

MAP_DICT_UNICODE_UPPER = {'À': u'À', 'Á': u'Á', 'Ả': u'Ả', 'Ã': u'Ã', 'Ạ': u'Ạ', 'Ằ': u'Ằ', 'Ắ': u'Ắ',
                          'Ẳ': u'Ẳ', 'Ẵ': u'Ẵ', 'Ặ': u'Ặ',
                          'Ầ': u'Ầ', 'Ấ': u'Ấ', 'Ẩ': u'Ẩ', 'Ẫ': u'Ẫ', 'Ậ': u'Ậ', 'È': u'È', 'É': u'É',
                          'Ẻ': u'Ẻ', 'Ẽ': u'Ẽ', 'Ẹ': u'Ẹ', 'Ề': u'Ề', 'Ế': u'Ế',
                          'Ể': u'Ể', 'Ễ': u'Ễ', 'Ệ': u'Ệ', 'Ò': u'Ò', 'Ó': u'Ó', 'Ỏ': u'Ỏ', 'Õ': u'Õ',
                          'Ọ': u'Ọ', 'Ồ': u'Ồ', 'Ố': u'Ố', 'Ổ': u'Ổ', 'Ỗ': u'Ỗ',
                          'Ộ': u'Ộ', 'Ờ': u'Ờ', 'Ớ': u'Ớ', 'Ở': u'Ở', 'Ỡ': u'Ỡ', 'Ợ': u'Ợ', 'Ù': u'Ù',
                          'Ú': u'Ú', 'Ủ': u'Ủ', 'Ũ': u'Ũ', 'Ụ': u'Ụ', 'Ừ': u'Ừ',
                          'Ứ': u'Ứ', 'Ử': u'Ử', 'Ữ': u'Ữ', 'Ự': u'Ự', 'Ì': u'Ì', 'Í': u'Í', 'Ỉ': u'Ỉ',
                          'Ĩ': u'Ĩ', 'Ị': u'Ị', 'Ỳ': u'Ỳ', 'Ý': u'Ý', 'Ỷ': u'Ỷ',
                          'Ỹ': u'Ỹ', 'Ỵ': u'Ỵ'}

VIETNAMESE_TONE_NORMALIZATION = {
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
    'oàn': "òan"
}

PATTERN_FORMAT_ADDRESS_ELEMENT = {
    1: [
        [1, r'^(t|tinh)\s(\.\s*)?', 'tỉnh '],
        [1, '^(tp|th[aà]nh\s?ph[oôố]|tph[ôốo])\s(\.\s*)?', 'thành phố '],
        [1, 'hcm|hồ cm|ho cho i minh|h([oòóõọỏôốồổỗộơớờởỡợ]|oo)\s?ch[[iìíĩỉịyỳỵỷỹý]\s?m[iìíĩỉịyỳỵỷỹý]nh', 'hồ chí minh'],
        [1, 'hn|h[aàáảãạâầấẩẫậăằắẳặ]\s?n[òóõọỏôốồổỗộơớờởỡợo]i', 'hà nội']
    ], 2: [
        [2, '^(q|qu[aậ]n|quaan)\s(\.\s*)?', 'quận '],
        [2, '^(h|huy[eê]n|huyeen)\s(\.\s*)?', 'huyện '],
        [2, '^(tx|thi xa|t[\s\.]x[ãa])\s(\.\s*)?', 'thị xã ']
    ],
    3: [
        [3, '^(x|xa)\s(\.\s*)?', 'xã '],
        [3, '^(p|f|[fp]h?[uưừ][ơoờ]n[gh]|p[hg]|phừng|puon)\s(\.\s*)?', 'phường '],
        [3, '^(tt|ttr[aâấ]n|thi tr[âa]n)\s(\.\s*)?', 'thị trấn '],
        [3, 'f?t[aàáảãạâầấẩẫậăằắẳặ]n\s?th?([oòóõọỏôốồổỗộơớờởỡợ]is?|u?[eèéẻẽẹêềếểễệ]|ai|ái) h[oò]a?',
         'tân thới hòa']],
    4: [
        [4, '^(k(hu)?\s*[đđ]t|kh[uùúũụủưứừửữựu]\s*[đd]([oòóõọỏôốồổỗộơớờởỡợ]|oo)\s*th[iìíĩỉịyỳỵỷỹý]) ', 'khu đô thị '],
        [4, '^(k(hu)\s*dân\s*cư|k(hu )dc|kh[uùúũụủưứừửữựu]\s?[đd][aàáảãạâầấẩẫậăằắẳặ]n\s?c[uùúũụủưứừửữựu]) ', 'khu dân cư '],
        [4, '^(k(hu )?ch)|kh[uùúũụủưứừửữựu]\s?c[aàáảãạâầấẩẫậăằắẳặ]n\s?h([oòóõọỏôốồổỗộơớờởỡợ]|oo)', 'khu căn hộ '],
        [4,
         '^(k(hu )?t[dđ]c|khu tái\s?[đd]c)|kh[uùúũụủưứừửữựu]\s?t[aàáảãạâầấẩẫậăằắẳặ][iìíĩỉịyỳỵỷỹý]\s?[đd][iìíĩỉịyỳỵỷỹý]nh\s?c[uùúũụủưứừửữựu]',
         'khu tái định cư '],
        [4, '^(k(hu )?tt)|kh[uùúũụủưứừửữựu]\s?t[aàáảãạâầấẩẫậăằắẳặ]p\s?th[eèéẻẽẹêềếểễệ]', 'khu tập thể '],
        [4, '^(k(hu )?bt)|kh[uùúũụủưứừửữựu]\s?b[iìíĩỉịyỳỵỷỹý][eèéẻẽẹêềếểễệ]t\s?th[uùúũụủưứừửữựu]', 'khu biệt thự '],
        [4, '^(cc|c\s?cư)|c[th][uùúũụủưứừửữựu]ng\s?c[uùúũụủưứừửữựu]', 'chung cư ']
    ], 5: [
        [5, '(kcn|khu\s?cn|kh[uùúũụủưứừửữựu]\s?c([oòóõọỏôốồổỗộơớờởỡợ]|oo)ng\s?ngh?[iìíĩỉị][eèéẻẽẹêềếểễệ]p)',
         ' khu công nghiệp '],
        [5, '(kcx|kh[uùúũụủưứừửữựu]cx|kh[uùúũụủưứừửữựu]\s?ch[eèéẻẽẹêềếểễệ]\s[xs][uùúũụủưứừửữựu][aàáảãạâầấẩẫậăằắẳặ]t)',
         'khu chế xuất ']
    ], 6: [
        [6, 'kontum', 'kon tum'],
        [6, '^(đg|dg|đ|đuonwfg|đươg|đương|dduongww) ', " đường "],
        [6, '(l[uũư](y|ng)|liễu|lĩ|lý)\s*b[aáảàạảấằ]ng?\s*b?[ií][cn]h', " lũy bán bích "],
        [6, '(l)*[ưu][ơo]ng\s*m[íi]nh\s*ng[ụu][ỵy]?[ệeẹ]t', " lương minh nguyệt "],
        [6, 'ng([ũu][ỹy][ê ễẽe]n|\.)?\s*v[ăaâ ắấ]n\s*y[êếe]n', ' nguyễn văn yến '],
        [6, "b[ùúũụủưứừửữựu][iì]\s*c[aàáãạảăắằẳẵặâấầẩẫậ]m\s*h[òóõọỏôốồổỗộơớờởỡợo]",
         ' bùi cẩm hổ '],
        [6, 'kinh tân hóa', ' kênh tân hóa '],
        [6, 'phan ann', ' phan anh '],
        [6, 'l[iìíĩỉịyỳỵỷỹý] thán[hg] tông?|ly thanh tog', ' lý thánh tông '],
        [6, 'b?[li]?ươn[gh] th(ế|ới) vinh', ' lương thế vinh '],
        [6, 'lương đắ bằng', ' lương đắc bằng '],
        [6, '(((d|đ|đg)?tr?|ch)?[uư][oơ][wnm][gh]|trg|trươg|tr) đ[iị]n[gh]', ' trương định ']
    ],
    9: [
        [9, 'ng([oòóõọỏôốồổỗộơớờởỡợ] |oo |\.|ox)', 'ngõ ']
    ],

    10: [
        [10, 'ngh?[aàáảãạâầấẩẫậăằắẳặ]ch|ngh\.', 'ngách ']
    ],

    14: [
        [14, '^(cc|c\s?cư)|c[th][uùúũụủưứừửữựu]ng c[uùúũụủưứừửữựu]', 'chung cư '],
        [14, 'cty', 'công ty']
    ]

}




RESOLVE_ABBR = [[r"([\s\,\.]|^)k\s*p([\s\,\.]|$)|ķp|khu phö", " khu phố "],
                [
                    r"([\s\,\.]|^)(t\sp|t\s*ph[ôố]?|t hành phố)([\s\,\.]|$)|[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆiIìÌỉỈĩĩĨíÍịỊoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰ]t hành phố",
                    " thành phố "],
                [r"([\s\,\.]|^)phườg([\s\,\.]|$)|phơờng|phuòng|phươ ̀ng|phườn(g)?", " phường "],
                [r"([\s\,\.]|^)q lộ\s", " quốc lộ "],
                [
                    r"([\s\,\.]|^)(đg|đương|đg\.)([\s\,\.]|$)|dûong|[₫đ][ưuừ][oơờ]ng|dùöng|đùong|ďuong|đ\s*\.|đuonwfg|đươg|đươgng|đươmgf|đuòng",
                    " đường "],
                [r"tphcm", " tphcm "],
                [r"tp\s*\.?\s*h[oôồ]\s*ch[ií]\s*minh|tphcm", "tp hồ chí minh"],
                ['h[aà]\sn[ôo]i|hà noiij|hnoi|hà nôuj|hanoi|hànoij|hà nôị', ' hà nội '],
                [r'c[oô]o?ng ngh[iỉị][êeẹệ]p', ' công nghiệp '],
                ['ďog nai', ' đồng nai '],
                [r"[đd][uư][oơờ]ng cach mang thang 8", "đường cách mạng tháng 8"],
                [r"(tỗ\s*)(\d+\w*)", fr"tổ \2"],
                [r'(([đd]([uưừ][ờoơ]n)?g([\s\.])*)?\b(ttn|tx|tml|ht|tth|ta|btt|bt[dđ]|xtt|đht|tch|tx)\s*)(\d+)',
                 r'đường \5\6'],
                ['quanj|q uận', ' quận '],
                [r'\bx\s*\.\s*', 'xã '],
                [r'\bh\s*\.\s*', 'huyện '],
                [r'\bt\s*\.\s*', 'tỉnh '],
                [r"\btx[aã]\s*(\.\s*)?", 'thị xã '],
                ["s[oôốó]\s*nh[aà]|sö nhà", "số nhà"],
                [r"(tx|q|p|x|tt|tp|xã|phường|thị trấn|quận|huyện|thị xã|thành phố|tỉnh)\s*\.\s*", r" \1 "],
                [r"ủy ban nd", "ubnd"],
                [r"(\.|\,|\;|\s|^)ệnh viện", "bệnh viện"],
                [r"(\.|\,|\;|\s|^)ệnh xá", "bệnh xá"],
                ['(\.|\,|\;|\s|^)ửa hàng|của hàng', 'cửa hàng'],
                ['(^ẻm|hẽm|hẻm)(\s*số)?', ' hẻm '],
                [r'ngxo|ngỏ|\bng\s*\.|ngõ số', ' ngõ '],
                ['(ng[oõ]o?)(\d+)', r' ngõ \2'],
                ['ngh?[áa]ch|ngh\s*\.|(\,\s*)?ngách|ngách số', ' ngách '],
                ['(ngõ\W|ngách|hẻm|kiệt|số nhà|đường|\Wấp|buôn|bản\W|sóc|xóm|làng|khu\W|tổ\W|khối|khóm|đội|thôn\W)',
                 r' \1 '],
                ['(\,|\.|\;|\s|^)(ấp\s*|ấps\s*)+', " ấp "],
                ['thhoon', ' thôn '],
                ['bìh dươg', 'bình dương'],
                ['thin trấn', "thị trấn"],
                ['buôn mê thuộc', 'buôn mê thuột'],
                ['trườg', 'trường'],
                ['t[ổôo]\s?d[âa]n\s?ph[ốôo]', ' tổ dân phố '],
                ['ngi', 'nghi'],
                ['gò vấ', " gò vấp "],
                ['(\s|\,|\.)guyễn', ' nguyễn '],
                ['qlộ', ' quốc lộ '],
                ['sôố', ' số '],
                ['(s|x)[oôốó]\s*nh[aà]|sö nhà', ' số nhà '],
                # ['\(([\w\s\d\W])*\)', ''],
                ['địa chỉ\s*\:?|số điện thoại|sđt|gần|đối diện', " "],
                [r'\bkbt\b', ' khu biệt thự '],
                [r'\bkđth\b|\bkđt\b', ' khu đô thị '],
                ['ng[ụu][ỵy] như kon tum', 'ngụy như kontum'],
                ["\d+ cái", ""],
                ['₫c|₫[iị]a ch[iỉ]|₫/c|₫t|^(\s*(ỉ|ố|ề|ềc|ến)\s*)|₫c', " "],
                [
                    '[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆ fFgGhHiIìÌỉỈĩĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTu UùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ\-\,\.\;\/\|\s0-9ûėā’\+\.]',
                    " "],
                ["ć", "c"],
                ["ï", "ĩ"],
                ["ð", "đ"],
                ["ä", "ắ"],
                ["ü", "ư"],
                ["ö", "ư"],
                ["ư´", "ứ"],
                ["ö", "ô"],
                ["₫₫", "đ"],
                ["₫", "đ"],
                ["ö", "ơ"],
                ["ó’", "ó"],
                ["ö", "ờ"],
                ["ő", "ố"],
                ["mỷ", "mỹ"],
                ["nguỹene", 'nguyễn']
                ]

PREFIX = {"(?<!lô\s)kp": "khu phố",
          # "(?<!lô\s)p": "phường",
          # "(?<!lô\s)q": "quận",
          "quận": "quận",
          "quan": "quan",
          "phường": "phường",
          "phuong": "phuong",
          "xom": "xom",
          "đường": "đường",
          "duong": "duong",
          "số nhà": "số nhà",
          "snhà": "số nhà",
          "tổ": "tổ",
          "to": "to",
          "khu": "khu",
          "ấp": "ấp",
          "ap": "ap",
          "khóm": "khóm",
          "ngõ": "ngõ",
          "ngo": "ngo",
          "số": "số",
          "so": "so",
          "sn": "số nhà",
          "ql": "quốc lộ",
          "đg": "đường",
          "lô": "lô",
          "đội": "đội",
          "doi": "doi",
          "tdp": "tổ dân phố",
          "tk": "tiểu khu"}

VOWEL = ['[aàáảãạâầấẩẫậăằắẳặ]','[eèéẻẽẹêềếểễệ]','[iìíĩỉịyỳỵỷỹý]','([oòóõọỏôốồổỗộơớờởỡợ]|oo)','[uùúũụủưứừửữựu]', '[đd]']

STREET = ['lương minh nguyệt', 'lũy bán bích', 'nguyễn văn yến', 'bùi cẩm hổ', 'trần văn cẩn', 'tô hiệu','lương thế vinh', 'lê quát','lý thánh tông', 'kênh tân hóa', 'lương đắc bằng', 'phan anh', 'hòa bình', 'nguyễn trọng quyền', 'đô đốc long',
          'trương định', 'nguyễn cảnh dị']
