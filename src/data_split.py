import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Создание директории для визуализаций, если она не существует
os.makedirs('../data/visualization', exist_ok=True)

# Загрузка предобработанных данных
print("Загрузка предобработанных данных...")
train_data = pd.read_csv('../data/train_preprocessed.csv')
test_data = pd.read_csv('../data/test_preprocessed.csv')

# Проверка наличия колонки clean_review
if 'clean_review' not in train_data.columns or 'clean_review' not in test_data.columns:
    print("ОШИБКА: Колонка 'clean_review' отсутствует. Запустите сначала data_preparation.py")
    exit(1)

# Создание признаков с помощью TF-IDF
print("Создание признаков с помощью TF-IDF...")
tfidf_vectorizer = TfidfVectorizer(max_features=1000)  # Уменьшено для ускорения обработки
tfidf_train = tfidf_vectorizer.fit_transform(train_data['clean_review'])
tfidf_test = tfidf_vectorizer.transform(test_data['clean_review'])

# Преобразование разреженных матриц в DataFrame
print("Преобразование TF-IDF матриц в DataFrame...")
tfidf_train_df = pd.DataFrame(tfidf_train.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
tfidf_test_df = pd.DataFrame(tfidf_test.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Кодирование категориальных признаков
print("Кодирование категориальных признаков...")
le_condition = LabelEncoder()
train_data['condition_encoded'] = le_condition.fit_transform(train_data['condition'])
test_data['condition_encoded'] = le_condition.transform(test_data['condition'])

# Добавление дополнительных признаков
print("Формирование финальных наборов признаков...")
train_features = pd.concat([
    tfidf_train_df,
    pd.DataFrame(train_data['condition_encoded'], columns=['condition_encoded']),
    train_data[['rating']]
], axis=1)

test_features = pd.concat([
    tfidf_test_df,
    pd.DataFrame(test_data['condition_encoded'], columns=['condition_encoded']),
    test_data[['rating']]
], axis=1)

# Целевая переменная
train_target = train_data['effective']
test_target = test_data['effective']

# Визуализация распределения классов
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='effective', data=train_data)
plt.title('Распределение классов в обучающей выборке')
plt.xlabel('Эффективность (0 - нет, 1 - да)')
plt.ylabel('Количество')

plt.subplot(1, 2, 2)
sns.countplot(x='effective', data=test_data)
plt.title('Распределение классов в тестовой выборке')
plt.xlabel('Эффективность (0 - нет, 1 - да)')
plt.ylabel('Количество')
plt.tight_layout()
plt.savefig('../data/visualization/class_distribution.png')
plt.close()

# Сохранение признаков и целевых переменных
print("Сохранение признаков и целевых переменных...")
train_features.to_csv('../data/train_features_corrected.csv', index=False)
test_features.to_csv('../data/test_features_corrected.csv', index=False)
train_target.to_csv('../data/train_target_corrected.csv', index=False)
test_target.to_csv('../data/test_target_corrected.csv', index=False)

# Сохранение словарей для кодирования/декодирования
condition_mapping = dict(zip(le_condition.classes_, le_condition.transform(le_condition.classes_)))
pd.DataFrame({
    'condition': list(condition_mapping.keys()),
    'encoded': list(condition_mapping.values())
}).to_csv('../data/condition_mapping.csv', index=False)

print("Разделение данных завершено!")
print(f"Размер обучающей выборки признаков: {train_features.shape}")
print(f"Размер тестовой выборки признаков: {test_features.shape}")
