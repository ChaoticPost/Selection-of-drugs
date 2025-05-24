# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Создание директории для визуализаций, если она не существует
os.makedirs('../data/visualization', exist_ok=True)

# Загрузка ресурсов для токенизации и стоп-слов
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Загрузка обучающей и тестовой выборки
print("Загрузка данных...")
train_data = pd.read_csv('../data/drugsComTrain_raw.csv')
test_data = pd.read_csv('../data/drugsComTest_raw.csv')
print(f"Размер обучающей выборки: {train_data.shape}")
print(f"Размер тестовой выборки: {test_data.shape}")

# Функция для очистки текстов отзывов
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'<.*?>', '', text)  # Удаление HTML
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Удаление спецсимволов
        text = text.lower()  # Приведение к нижнему регистру
        
        # Токенизация и удаление стоп-слов
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        
        # Лемматизация
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in word_tokens if word not in stop_words]
        
        return ' '.join(tokens)
    return ''

# Применение очистки текста к отзывам
print("Очистка текстов отзывов...")
train_data['clean_review'] = train_data['review'].apply(clean_text)
test_data['clean_review'] = test_data['review'].apply(clean_text)

# Создание бинарного признака эффективности лекарства
print("Создание бинарного признака эффективности...")
train_data['effective'] = train_data['rating'].apply(lambda x: 1 if x >= 7 else 0)
test_data['effective'] = test_data['rating'].apply(lambda x: 1 if x >= 7 else 0)

# Визуализация распределения рейтингов
plt.figure(figsize=(10, 6))
sns.histplot(train_data['rating'], bins=10, kde=True)
plt.title('Распределение рейтингов лекарств')
plt.xlabel('Рейтинг')
plt.ylabel('Количество')
plt.savefig('../data/visualization/rating_distribution.png')
plt.close()

# Визуализация распределения эффективности
plt.figure(figsize=(10, 6))
sns.countplot(x='effective', data=train_data)
plt.title('Распределение эффективности лекарств')
plt.xlabel('Эффективность (0 - неэффективно, 1 - эффективно)')
plt.ylabel('Количество')
plt.savefig('../data/visualization/effectiveness_distribution.png')
plt.close()

# Топ-10 заболеваний
plt.figure(figsize=(12, 8))
train_data['condition'].value_counts().head(10).plot(kind='bar')
plt.title('Топ-10 наиболее часто встречающихся заболеваний')
plt.xlabel('Заболевание')
plt.ylabel('Количество')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../data/visualization/top_conditions.png')
plt.close()

# Сохранение обработанных данных
print("Сохранение предобработанных данных...")
train_data.to_csv('../data/train_preprocessed.csv', index=False)
test_data.to_csv('../data/test_preprocessed.csv', index=False)
print("Предобработка данных завершена!")
