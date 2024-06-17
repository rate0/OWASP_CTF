import os
import time

# Время жизни файлов в секундах (например, 10 минут)
FILE_LIFETIME = 600

def process_update(filename):
    # ВНИМАНИЕ: Небезопасное выполнение команды, симуляция уязвимости
    os.system(f'unzip uploads/{filename} -d uploads/')
    # Демонстрация выполнения произвольного кода через командную строку
    os.system(f'cat uploads/{filename} > /dev/null')

def cleanup_old_files(upload_folder):
    while True:
        now = time.time()
        for filename in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, filename)
            if os.path.isfile(file_path):
                file_age = now - os.path.getmtime(file_path)
                if file_age > FILE_LIFETIME:
                    os.remove(file_path)
                    print(f"Deleted old file: {filename}")
        time.sleep(60)  # Проверка каждые 60 секунд
