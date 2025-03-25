import random
from ast import literal_eval
import string
from nltk.tokenize import word_tokenize
import numpy as np
import re
import unidecode
import nltk
import json
import os

nltk.download('punkt')


class SynthesizeData():
    """
    Uitils class to create artificial miss-spelled words
    Args:
        vocab_path: path to vocab file. Vocab file is expected to be a set of words, separate by ' ', no newline charactor.
    """

    def __init__(self):

        CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

        self.word_couples_path = os.path.join(CURRENT_PATH, 'noising_resources/kieu_go_dau_cu_moi.txt')
        self.homowords_path = os.path.join(CURRENT_PATH, "noising_resources/confusion_set.json")
        self.attack_confusion_set_path = os.path.join(CURRENT_PATH, "noising_resources/attack_confusion_set.json")
        self.homo_leters_dict_path = os.path.join(CURRENT_PATH, "noising_resources/homo_leter.json")
        self.typo_path = os.path.join(CURRENT_PATH, "noising_resources/typo.json")

        self.vn_alphabet = ['a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'ô',
                            'ơ', 'p', 'q', 'r', 's', 't', 'u', 'ư', 'v', 'x', 'y']
        self.alphabet_len = len(self.vn_alphabet)
        self.word_couples = [pair.strip("\n").split(" ") for pair in open(
            self.word_couples_path, "r").readlines()]
        self.homowords = literal_eval(
            open(self.homowords_path, "r").read())

        self.attack_confusion_set = literal_eval(
            open(self.attack_confusion_set_path, "r").read())

        self.homo_leters_dict = literal_eval(
            open(self.homo_leters_dict_path, "r").read())

        self.typo = json.load(open(self.typo_path, "r"))
        self.all_char_candidates = self.get_all_char_candidates()
        self.all_word_candidates = self.get_all_word_candidates()

    def replace_char_candidate(self, char):
        """
        return a homophone char/subword of the input char. (s/x, tr/ch)
        """
        return np.random.choice(self.homo_leters_dict[char])

    def replace_attacked_candidate(self, word):
        """
        Return a attacked word of input for example: thành -> thành or thuở -> thửo
        """
        capital_flag = word[0].isupper()
        word = word.lower()

        choices = [x for x in [0, 1] if len(self.attack_confusion_set[word][x]) > 0]
        if len(choices) == 2:
            coin = np.random.choice(choices, p=[0.3, 0.7])
        elif len(choices) == 1:
            coin = np.random.choice(choices)

        candidates = self.attack_confusion_set[word][coin]

        candidate = np.random.choice(candidates)
        if capital_flag:
            return candidate.capitalize()
        return candidate

    def replace_from_confusion_set(self, word):
        """
        Return a homo word of the input word from confusionset that contain within 2 edit distance word
        """
        capital_flag = word[0].isupper()
        word = word.lower()

        def choose_candidates_set_mixed():
            choices = [x for x in [0, 1] if len(self.homowords[word]["mixed"][x]) > 0]
            if len(choices) == 2:
                coin = np.random.choice(choices, p=[0.8, 0.2])
            elif len(choices) == 1:
                coin = np.random.choice(choices)

            candidates = self.homowords[word]["mixed"][coin]
            return candidates

        def choose_candidates_set_consonant():
            choices = [x for x in [0, 1] if len(self.homowords[word]["consonant"][x]) > 0]
            if len(choices) == 2:
                coin = np.random.choice(choices, p=[0.8, 0.2])
            elif len(choices) == 1:
                coin = np.random.choice(choices)

            candidates = self.homowords[word]["consonant"][coin]
            return candidates

        choices_consonant = [x for x in [0, 1] if len(self.homowords[word]["consonant"][x]) > 0]
        choices_mixed = [x for x in [0, 1] if len(self.homowords[word]["mixed"][x]) > 0]
        if len(choices_mixed) != 0 and len(choices_consonant) != 0:
            candidate_type = np.random.choice(["consonant", "mixed"], p=[0.2, 0.8])
            if candidate_type == "consonnant":
                candidates = choose_candidates_set_consonant()
            else:
                candidates = choose_candidates_set_mixed()
        elif len(choices_mixed) == 0:
            candidates = choose_candidates_set_consonant()
        elif len(choices_consonant) == 0:
            candidates = choose_candidates_set_mixed()

        candidate = np.random.choice(candidates)
        if capital_flag:
            return candidate.capitalize()
        return candidate

    def replace_char_candidate_typo(self, char):
        """
        return a homophone char/subword of the input char (x/s, tr/ch)
        """
        candidates = self.typo[char]
        num_lower_priority = len(candidates) - 1
        round_flag = 10 * num_lower_priority

        return np.random.choice(candidates, p=[0.7, *[3 / round_flag for i in range(num_lower_priority)]])

    def get_all_char_candidates(self):

        return list(self.homo_leters_dict.keys())

    def get_all_word_candidates(self):

        all_word_candidates = []
        for couple in self.word_couples:
            all_word_candidates.extend(couple)
        return all_word_candidates

    def remove_diacritics(self, text, onehot_label):
        """
        Replace word which has diacritics with the same word without diacritics for example: nước -> nuoc, thành -> thanh, khuyến -> khuyen
        """

        if len(text) == len(' '.join(text).split()):
            its_me = True
        else:
            its_me = False

        idx = np.random.randint(0, len(onehot_label))
        prevent_loop = 0
        noised_token = unidecode.unidecode(text[idx])
        # while onehot_label[idx] != 0 or not self.vocab.exist(text[idx]) or text[idx] in string.punctuation or text[
        #     idx] == noised_token:
        #     idx = np.random.randint(0, len(onehot_label))
        #     noised_token = unidecode.unidecode(text[idx])
        #     prevent_loop += 1
        #     if prevent_loop > 10:
        #         return False, text, onehot_label

        onehot_label[idx] = 1
        token = text[idx]
        text[idx] = unidecode.unidecode(text[idx])

        if (len(text) != len(' '.join(text).split())) and its_me:
            print("ERROR:")
            print("text: ", text)
            print("replaced token: ", text[idx])
            print("org token: ", token)

        return True, text, onehot_label

    def replace_with_random_letter(self, text, onehot_label):
        """
        Replace, add (or remove) a random letter in a random chosen word with a random letter
        """

        if len(text) == len(' '.join(text).split()):
            its_me = True
        else:
            its_me = False

        idx = np.random.randint(0, len(onehot_label))
        prevent_loop = 0
        # while onehot_label[idx] != 0 or not self.vocab.exist(text[idx]) or len(text[idx]) < 3:
        #     idx = np.random.randint(0, len(onehot_label))
        #     prevent_loop += 1
        #     if prevent_loop > 10:
        #         return False, text, onehot_label

        # replace, add or remove? 0 is replace, 1 is add, 2 is remove
        # 0.8 1 edits, 0.2 2 edits
        num_edit = np.random.choice([1, 2], p=[0.8, 0.2])
        coin = np.random.choice([0, 1, 2])

        for i in range(num_edit):
            token = list(text[idx])
            if coin == 0:
                chosen_idx = np.random.randint(0, len(token))
                replace_candidate = self.vn_alphabet[np.random.randint(
                    0, self.alphabet_len)]
                token[chosen_idx] = replace_candidate
                text[idx] = "".join(token)
            elif coin == 1:
                chosen_idx = np.random.randint(0, len(token) + 1)
                if chosen_idx == len(token):
                    added_chars = self.vn_alphabet[np.random.randint(0, self.alphabet_len)] + \
                                  token[0]
                    chosen_idx = 0
                else:
                    added_chars = token[chosen_idx] + \
                                  self.vn_alphabet[np.random.randint(
                                      0, self.alphabet_len)]

                token[chosen_idx] = added_chars
                text[idx] = "".join(token)
            else:
                chosen_idx = np.random.randint(0, len(token))
                token[chosen_idx] = ""
                text[idx] = "".join(token)

        onehot_label[idx] = 1

        if (len(text) != len(' '.join(text).split())) and its_me:
            print("ERROR:")
            print("text: ", text)
            print("replaced token: ", text[idx])
            print("org token: ", token)
            print("coin: ", coin)
            return False, text, onehot_label

        return True, text, onehot_label

    def replace_with_homophone_word(self, text, onehot_label, strategy="normal"):
        """
        Replace a candidate word (if exist in the word_couple) with its homophone. if successful, return True, else False
        """

        if len(text) == len(' '.join(text).split()):
            its_me = True
        else:
            its_me = False

        candidates = []
        for i in range(len(text)):
            if text[i].lower() in self.homowords and strategy == "normal":
                candidates.append((i, text[i]))
            if text[i].lower() in self.attack_confusion_set and strategy == "attack":
                candidates.append((i, text[i]))

        if len(candidates) == 0:
            return False, text, onehot_label

        idx = np.random.randint(0, len(candidates))
        prevent_loop = 0
        # while onehot_label[candidates[idx][0]] != 0 or not self.vocab.exist(candidates[idx][1]):
        #     idx = np.random.choice(np.arange(0, len(candidates)))
        #     prevent_loop += 1
        #     if prevent_loop > 10:
        #         return False, text, onehot_label
        if strategy == "normal":
            text[candidates[idx][0]] = self.replace_from_confusion_set(
                candidates[idx][1])
        elif strategy == "attack":
            text[candidates[idx][0]] = self.replace_attacked_candidate(
                candidates[idx][1])

        if (len(text) != len(' '.join(text).split())) and its_me:
            print("ERROR:")
            print("text: ", text)
            print("replaced token: ", text[candidates[idx][0]])
            print("org token: ", candidates[idx][1])
            return False, text, onehot_label

        onehot_label[candidates[idx][0]] = 1
        return True, text, onehot_label

    def replace_with_homophone_letter(self, text, onehot_label):
        """
        Replace a subword/letter with its homophones. (s, x -> ch, tr)
        """

        if len(text) == len(' '.join(text).split()):
            its_me = True
        else:
            its_me = False

        candidates = []
        for i in range(len(text)):
            for char in self.all_char_candidates:
                if re.search("^" + char, text[i]) is not None:
                    candidates.append((i, char, "^" + char))
                if re.search(char + "$", text[i]) is not None:
                    candidates.append((i, char, char + "$"))

        if len(candidates) == 0:

            return False, text, onehot_label

        else:
            idx = np.random.randint(0, len(candidates))
            # prevent_loop = 0
            # while onehot_label[candidates[idx][0]] != 0 or not self.vocab.exist(text[candidates[idx][0]]) or len(
            #         text[candidates[idx][0]]) < 2:
            #     idx = np.random.randint(0, len(candidates))
            #     prevent_loop += 1
            #     if prevent_loop > 10:
            #         return False, text, onehot_label

            replaced = self.replace_char_candidate(candidates[idx][1])
            # 0.15% remove the candidate. cát -> cá
            coin = np.random.choice([0, 1], p=[0.8, 0.2])
            text_to_replace = text[candidates[idx][0]]
            result = re.sub(candidates[idx][2], replaced if coin == 0 else "",
                            text_to_replace)
            if result == "":
                result = re.sub(candidates[idx][2], replaced,
                                text_to_replace)

            text[candidates[idx][0]] = result

            if (len(text) != len(' '.join(text).split())) and its_me:
                print("ERROR:")
                print("text: ", text)
                print("replaced token: ", text[candidates[idx][0]])
                print("letter: ", candidates[idx][1])
                print("replaced letter: ", replaced)

            onehot_label[candidates[idx][0]] = 1
            return True, text, onehot_label

    def replace_with_typo_letter(self, text, onehot_label):
        """
        Replace a word with original typo vni or telex. nước -> nuwowc
        """

        if len(text) == len(' '.join(text).split()):
            its_me = True
        else:
            its_me = False

        # find index noise
        idx = np.random.randint(0, len(onehot_label))
        prevent_loop = 0
        # while onehot_label[idx] != 0 or not self.vocab.exist(text[idx]):
        #     idx = np.random.randint(0, len(onehot_label))
        #     prevent_loop += 1
        #     if prevent_loop > 10:
        #         return False, text, onehot_label

        index_noise = idx
        onehot_label[index_noise] = 1

        org_word = text[index_noise]
        word_noise = text[index_noise]

        pattern = "(" + "|".join(self.typo.keys()) + "){1}"
        candidates = re.findall(pattern, word_noise)
        if len(candidates) == 0:
            return False, text, onehot_label
        accent_pattern = "(s|f|r|x|j|1|2|3|4|5){1}"
        for candidate in candidates:
            replaced = self.replace_char_candidate_typo(candidate)
            # Move accent to the end of text
            result = re.findall(accent_pattern, replaced)
            if len(result) != 0:
                word_noise = re.sub(candidate, replaced[0:-1], word_noise)
                word_noise += replaced[-1]
            else:
                word_noise = re.sub(candidate, replaced, word_noise)

        text[index_noise] = word_noise

        if len(word_noise) < 3:
            return True, text, onehot_label
        # Introduce one or two edit on text
        num_edits = np.random.choice([0, 1, 2], p=[0.5, 0.35, 0.15])

        for i in range(num_edits):
            coin = np.random.choice([0, 1, 2, 3])
            word_noise = list(text[index_noise])
            start_char = word_noise.pop(0)

            if coin == 0:
                chosen_idx = np.random.randint(0, len(word_noise))
                word_noise[chosen_idx] = self.vn_alphabet[np.random.randint(
                    0, self.alphabet_len)]
                text[index_noise] = start_char + "".join(word_noise)
            elif coin == 1:
                chosen_idx = np.random.randint(0, len(word_noise))
                word_noise[chosen_idx] += self.vn_alphabet[np.random.randint(
                    0, self.alphabet_len)]
                text[index_noise] = start_char + "".join(word_noise)
            elif coin == 2:
                if len(word_noise) < 2:
                    continue
                chosen_idxs = np.random.choice(range(len(word_noise)), size=2)
                word_noise[chosen_idxs[0]], word_noise[chosen_idxs[1]] = \
                    word_noise[chosen_idxs[1]], word_noise[chosen_idxs[0]]
                text[index_noise] = start_char + "".join(word_noise)
            else:
                chosen_idx = np.random.randint(0, len(word_noise))
                word_noise[chosen_idx] = ""
                text[index_noise] = start_char + "".join(word_noise)

        return True, text, onehot_label

    def split_word(self, text, onehot_label):
        """
        Introduce split word error. Example: nước -> nư ớc, khuyên -> khu y ên
        """
        # find index noise
        idx = np.random.randint(0, len(onehot_label))
        prevent_loop = 0
        while onehot_label[idx] not in [0, 1] or len(text[idx]) < 3 or text[
            idx] in r'''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~''':
            idx = np.random.randint(0, len(onehot_label))
            prevent_loop += 1
            if prevent_loop > 10:
                return False, text, onehot_label

        org_word = text[idx]
        new_text = text[:idx]
        new_onehot = onehot_label[:idx]

        index_split = np.random.randint(1, len(org_word))

        new_text.extend([org_word[:index_split], org_word[index_split:]])
        new_onehot.extend([2, 2])

        if idx < len(text) - 1:
            new_text.extend(text[idx + 1:])
            new_onehot.extend(onehot_label[idx + 1:])

        return True, new_text, new_onehot

    def merge_word(self, text, onehot_label):
        """
        Introduce merge word error. Example: thành công -> thànhcông or giao hàng tiết kiệm -> giaohàngtiếtkiệm
        """
        length = len(onehot_label)
        if length < 2:
            return False, text, onehot_label

        def validate_len(idx, size):
            while idx + size > length:
                if idx > 0:
                    idx -= 1
                else:
                    size -= 1
            return idx, size

        def validate_value(idx, size):
            for i in range(idx, idx + size):
                if onehot_label[i] not in [0, 1] or text[i] in r'''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~''':
                    return False
            return True

        # find index noise
        min_words = 2
        max_words = 3 if length > 3 else length
        num_words = np.random.randint(min_words, max_words + 1)
        idx = np.random.randint(0, length)
        prevent_loop = 0
        idx, num_words = validate_len(idx, num_words)
        while not validate_value(idx, num_words):
            prevent_loop += 1
            if prevent_loop > 10:
                return False, text, onehot_label
            idx = np.random.randint(0, length)
            num_words = np.random.randint(min_words, max_words + 1)
            idx, num_words = validate_len(idx, num_words)

        new_text = text[:idx]
        new_onehot = onehot_label[:idx]
        new_text.append(''.join(text[idx:idx + num_words]))

        new_onehot.append(-num_words + 1)

        if idx + num_words < length:
            new_text.extend(text[idx + num_words:])
            new_onehot.extend(onehot_label[idx + num_words:])

        return True, new_text, new_onehot

    def add_normal_noise(self, sentence, percent_err=0.2, num_type_err=5):
        """
        Top function level to corupt sequence with word errors only (not include whitespace errors)
        """
        tokens = sentence.split()

        if len(tokens) <= 0:
            print(f"SOMETHING WROONG - sent: {sentence}")

        onehot_label = [0] * len(tokens)

        num_wrong = int(np.ceil(percent_err * len(tokens)))
        num_wrong = np.random.randint(1, num_wrong + 1)
        if np.random.rand() < 0.05:
            num_wrong = 0

        prevent_loop = 0

        for i in range(0, num_wrong):

            err = np.random.choice(
                range(num_type_err + 1), p=[0.1, 0.1, 0.15, 0.2, 0.1, 0.35])

            if err == 0:
                _, tokens, onehot_label = self.remove_diacritics(
                    tokens, onehot_label)

            elif err == 1:
                _, tokens, onehot_label = self.replace_with_typo_letter(
                    tokens, onehot_label)

            elif err == 2:
                _, tokens, onehot_label = self.replace_with_random_letter(
                    tokens, onehot_label)

            elif err == 3:
                _, tokens, onehot_label = self.replace_with_homophone_letter(
                    tokens, onehot_label)

            elif err == 4:
                _, tokens, onehot_label = self.replace_with_homophone_word(
                    tokens, onehot_label, strategy="attack")

            else:
                _, tokens, onehot_label = self.replace_with_homophone_word(
                    tokens, onehot_label)

            prevent_loop += 1

            if prevent_loop > 10:
                return ' '.join(tokens), ' '.join([str(i) for i in onehot_label])

            # print(tokens)

            self.verify(tokens, sentence)

        return ' '.join(tokens), ' '.join([str(i) for i in onehot_label])

    def add_split_merge_noise(self, sentence, percent_err=0.15, num_type_err=2, percent_normal_err=0.15,
                              return_all=False):
        """
        Top function level to corupt sequence with both whitespace error and word errors
        """

        def count_zero_one(onehot_label):
            return sum([1 if onehot in [0, 1] else 0 for onehot in onehot_label])

        # Introduce normal noise before split merge
        normal_noise, normal_onehot = self.add_normal_noise(
            sentence, percent_err=percent_normal_err)

        tokens = normal_noise.split()
        length = len(tokens)

        onehot_label = [int(x) for x in normal_onehot.split(" ")]

        num_wrong = int(np.ceil(percent_err * length))
        num_wrong = np.random.randint(1, num_wrong + 1)
        if np.random.rand() < 0.05:
            num_wrong = 0

        min_zeroes = length - num_wrong
        zero_one_num = length
        prevent_loop = 0
        while zero_one_num > min_zeroes:

            err = np.random.randint(0, num_type_err)

            if err == 0:
                _, tokens, onehot_label = self.split_word(
                    tokens, onehot_label)

            else:
                _, tokens, onehot_label = self.merge_word(
                    tokens, onehot_label)

            prevent_loop += 1

            if prevent_loop > 10:
                if return_all:
                    return ' '.join(tokens), ' '.join([str(i) for i in onehot_label]), normal_noise
                else:
                    return ' '.join(tokens), ' '.join([str(i) for i in onehot_label])

            zero_one_num = count_zero_one(onehot_label)

        if return_all:
            return ' '.join(tokens), ' '.join([str(i) for i in onehot_label]), normal_noise
        return ' '.join(tokens), ' '.join([str(i) for i in onehot_label])

    def verify(self, noised_tokens, sentence):
        if len(noised_tokens) != len(' '.join(noised_tokens).split()):
            print("ERROR:")
            print("TEXT  : ", sentence)
            print("TOKENS: ", ' '.join(noised_tokens))
            exit()

        return True


    def create_noise_frefix(self, text):
        PREFIX_ERROR = {
        'ngõ': ['ngo', 'ngox', 'ng.'],
        'ngách': ['nagchs', 'ngh.', 'nghach', 'nghach'],
        'thành phố': ['tp', 'tpho', 't phố'],
        'Hồ Chí Minh': ['hcm'],
        'Hà Nội': ['hn'],
        'quận': ['q', 'q.'],
        'huyện': ['h', 'h.'],
        'thị xã': ['tx', 'tx.'],
        'phường': ['p', 'p.'],
        'thị trấn': ['tt', 'tt.'],
        'xã': ['x', 'x.'],
        'khu đô thị': ['kdt', 'kđt'],
        'khu dân cư': ['kdc', 'khu dc'],
        'khu chung cư': ['khu cc', 'kcc'],
        'khu tái định cư': ['khu tđc'],
        'khu tập thể': ['ktt', 'khu tt'],
        'khu biệt thự': ['khu bt', 'kbt'],
        'chung cư': ['cc', 'cc.'],
        'khu công nghiệp': ['kcn', 'khu cn'],
        'khu chế xuất': ['kcx', 'khu cx'],
        'đường': ['đg', 'đ.', 'đương'],
        'số nhà': ['sn', 'so nha'],
        'công ty': ['cty', 'ct'],
        'trường': ['tg'],
        'tổ dân phố': ['tdp']
    }


        for key in PREFIX_ERROR.keys():
            pattern = PREFIX_ERROR[key]
            if re.search(key, text, flags=re.IGNORECASE):
                index = 0
                if len(pattern) > 1:
                    index = random.random(0, len(pattern) -1 )
                text = re.sub(key, pattern[index], text, flags=re.IGNORECASE)
                return text
        return text


if __name__ == "__main__":
    text = "đ/c số, 124 âu cơ"
    noiser = SynthesizeData()
    noised_text, onehot_label = noiser.add_split_merge_noise(text, percent_err=0.5)
    print(noised_text)
    print(noiser.create_noise_frefix('tổ dân phố xuân đỉnh'))

