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

# Визуализация распределения рейтингов
plt.figure(figsize=(10, 6))
sns.histplot(train_data['rating'], bins=10, kde=True)
plt.title('Распределение рейтингов лекарств')
plt.xlabel('Рейтинг')
plt.ylabel('Количество')
plt.savefig('data/visualization/rating_distribution.png')
plt.close()

# Визуализация распределения эффективности
plt.figure(figsize=(10, 6))
sns.countplot(x='effective', data=train_data)
plt.title('Распределение эффективности лекарств')
plt.xlabel('Эффективность (0 - неэффективно, 1 - эффективно)')
plt.ylabel('Количество')
plt.savefig('data/visualization/effectiveness_distribution.png')
plt.close()

# Топ-10 заболеваний
plt.figure(figsize=(12, 8))
train_data['condition'].value_counts().head(10).plot(kind='bar')
plt.title('Топ-10 наиболее часто встречающихся заболеваний')
plt.xlabel('Заболевание')
plt.ylabel('Количество')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('data/visualization/top_conditions.png')
plt.close()

# Сохранение обработанных данных
print("Сохранение предобработанных данных...")
train_data.to_csv('data/train_preprocessed.csv', index=False)
test_data.to_csv('data/test_preprocessed.csv', index=False)

print("Предобработка данных завершена!")
