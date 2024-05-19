import pandas as pd

df = pd.read_csv('file.csv', delimiter='|', dtype=str)

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x, axis=1)

duplicated_groups = df[df.groupby('id').transform('nunique').sum(axis=1) > df.shape[1] - 1]

duplicated_groups.to_csv('different_data_records.csv', index=False, sep='|')

print("Разные записи с одинаковыми id сохранены в 'different_data_records.csv'")




# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998 |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972 |457865234-3431
"""