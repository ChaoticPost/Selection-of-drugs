# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка ресурсов для токенизации и стоп-слов
nltk.download('punkt')
nltk.download('stopwords')

# Загрузка обучающей и тестовой выборки
print("Загрузка данных...")
train_data = pd.read_csv('data/drugsComTrain_raw.csv')
test_data = pd.read_csv('data/drugsComTest_raw.csv')

print(f"Размер обучающей выборки: {train_data.shape}")
print(f"Размер тестовой выборки: {test_data.shape}")

# Загрузка обучающей и тестовой выборки
print("Загрузка данных...")
train_data = pd.read_csv('data/drugsComTrain_raw.csv')
test_data = pd.read_csv('data/drugsComTest_raw.csv')

print(f"Размер обучающей выборки: {train_data.shape}")
print(f"Размер тестовой выборки: {test_data.shape}")

# Функция для очистки текстов отзывов
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'<.*?>', '', text)  # Удаление HTML
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Удаление спецсимволов
        text = text.lower()  # Приведение к нижнему регистру
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        text = ' '.join([w for w in word_tokens if w not in stop_words])
        return text
    return ''

# Применение очистки к текстам
train_data['clean_review'] = train_data['review'].apply(clean_text)
test_data['clean_review'] = test_data['review'].apply(clean_text)

# Создание целевой переменной: 1 если рейтинг >= 7, иначе 0
train_data['effective'] = (train_data['rating'] >= 7).astype(int)
test_data['effective'] = (test_data['rating'] >= 7).astype(int)
