import os
import zipfile
import PyPDF2
# Создаем папку "ресурсы", если её нет
os.makedirs('tst', exist_ok=True)

def test_create_sample_files():
    # Просто создаем пустые файлы нужных форматов
    open('sample.pdf', 'wb').close()
    open('sample.xlsx', 'wb').close()
    open('sample.csv', 'wb').close()

def test_create_zip_archive():
    with zipfile.ZipFile('tst/sample_files.zip', 'w') as zipf:
        zipf.write('sample.pdf')
        zipf.write('sample.xlsx')
        zipf.write('sample.csv')

def test_check_files_in_archive():
    required_files = {'sample.pdf', 'sample.xlsx', 'sample.csv'}

    with zipfile.ZipFile('tst/sample_files.zip', 'r') as zipf:
        # Получаем список файлов в архиве
        files_in_archive = set(zipf.namelist())

        # Проверяем, все ли нужные файлы есть
        missing_files = required_files - files_in_archive
        extra_files = files_in_archive - required_files

        if not missing_files and not extra_files:
            print("Все нужные файлы присутствуют в архиве!")