def method_1(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    p = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            p += 1
    return int(p / len(str1) * 100)


def method_2(str1, str2):
    from fuzzywuzzy import fuzz
    import statistics as st
    sentences = str1.split(), str2.split()
    l2 = []
    for w1, w2 in zip(sentences[0], sentences[1]):
        l2.append(fuzz.ratio(w1, w2))
    return st.mean(l2)


def method_3(str1, str2):
    import Levenshtein
    import statistics as st
    sentences = str1.split(), str2.split()
    l = []
    for w1, w2 in zip(sentences[0], sentences[1]):
        l.append(Levenshtein.ratio(w1, w2))
    return st.mean(l)


def method_4(str1, str2):
    import Levenshtein
    import statistics as st
    sentences = str1.split(), str2.split()
    l3 = []
    for w1, w2 in zip(sentences[0], sentences[1]):
        l3.append(Levenshtein.jaro_winkler(w1, w2))
    return st.mean(l3)


def method_5(str1, str2):
    from difflib import SequenceMatcher
    s = SequenceMatcher(str1, str2)
    return s.ratio()


def method_6(str1, str2):
    from diff_match_patch import diff_match_patch
    dmp = diff_match_patch()
    patches = dmp.patch_make(str1, str2)
    diff = dmp.patch_toText(patches)
    return diff


# perf_counter_ns | perf_counter | process_time_ns | process_time
# 1 - 33321800    | 0.034033     | 0               | 0.0
# 6 - 35326400    | 0.0357944    | 0               | 0.0
# 5 - 33186400    | 0.0358235    | 0               | 0.0
# 4 - 59397100    | 0.0646537    | 31250000        | 0.03125
# 3 - 62783300    | 0.0687129    | 31250000        | 0.03125
# 2 - 77180100    | 0.0720935    | 46875000        | 0.046875
def main():
    import time
    t_start = time.process_time()
    print(method_1('Подготовка и утверждение документов территориального планирования городских',
             'Подготовка и утверждение документов территориального планирования городских муниципалитетов'))
    print("Time elapsed: ", time.process_time() - t_start)


if __name__ == '__main__':
    main()
