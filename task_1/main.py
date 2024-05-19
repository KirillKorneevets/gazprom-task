import pandas as pd

df = pd.read_csv('file.csv', delimiter='|', dtype=str)

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x, axis=1)

duplicated_groups = df[df.groupby('id').transform('nunique').sum(axis=1) > df.shape[1] - 1]

duplicated_groups.to_csv('different_data_records.csv', index=False, sep='|')

print("Разные записи с одинаковыми id сохранены в 'different_data_records.csv'")
