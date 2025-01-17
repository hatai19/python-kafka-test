FROM python:3.12

WORKDIR /app

COPY requirements.txt ./src/requirements.txt

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Устанавливаем зависимости из requirements.txt
RUN pip install -r ./src/requirements.txt

# Копируем остальные файлы приложения
COPY . .

# Указываем команду для выполнения при запуске контейнера
CMD ["python", "src/main.py"]