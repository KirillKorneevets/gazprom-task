import os
import datetime

def delete_files_older_than(folder_path, second):
    current_date = datetime.datetime.now()
    target_date = current_date - datetime.timedelta(seconds=second)

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_date < target_date:
                os.remove(file_path)
                print(f"Файл '{file_path}' удален.")

folder_path = "C:\\Users\\Lenovo\\Desktop\\test\\task_4\del\\"

second = 30

delete_files_older_than(folder_path, second)


"""
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней
"""