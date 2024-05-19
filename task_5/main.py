import os


def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip().lower() for line in file]
    return words

def generate_combinations(words):
    new_words = set()
    
    for word in words:
        for compare_word in words:
            if word != compare_word:
                max_overlap_len = min(len(word), len(compare_word)) - 1
                for overlap_len in range(2, max_overlap_len + 1):
                    if word.endswith(compare_word[:overlap_len]):
                        new_word = word + compare_word[overlap_len:]
                        new_words.add(new_word)
    
    return new_words

def write_words(file_path, words):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(f"{word}\n")

def main(input_file, output_file):
    words = read_words(input_file)
    new_words = generate_combinations(words)
    write_words(output_file, new_words)

if __name__ == "__main__":
    input_file = os.getcwd()+'\\task_5\\words.txt'  
    output_file = os.getcwd()+'\\task_5\\output.txt'  
    main(input_file, output_file)




"""
В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.
Задание:
Написать программу которая выводит список слов,
каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения
Например, текстовый файл содержит слова:
ласты
стык
стыковка
баласт
кабала
карась
Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка
Пользователь вводмт первое слово: кабала
Программа выводит:
кабаласты
кабаласт
Пользователь вводмт первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась
"""