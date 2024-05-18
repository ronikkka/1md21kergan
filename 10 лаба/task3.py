with open('en-ru.txt', 'r') as f_in, open('ru-en.txt', 'w') as f_out:

en_ru = {}
for line in f_in:
    en, ru = line.strip().split(' - ')
    en_ru[en] = ru

ru_en = {}
for en, ru in en_ru.items():
    ru_en[ru] = en

sorted_ru_en = sorted(ru_en.items())

for ru, en in sorted_ru_en:
    f_out.write(f"{ru} - {en}n")