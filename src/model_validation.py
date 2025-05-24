import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Загрузка данных
print("Загрузка данных для валидации...")
train_features = pd.read_csv('data/train_features.csv')
test_features = pd.read_csv('data/test_features.csv')
train_target = pd.read_csv('data/train_target.csv')
test_target = pd.read_csv('data/test_target.csv')

# Проверка на утечку данных
print("Проверка на утечку данных...")

# Проверка корреляции между рейтингом и целевой переменной
train_data = pd.concat([train_features[['rating']], train_target], axis=1)
correlation = train_data.corr()
print(f"Корреляция между рейтингом и эффективностью: {correlation.iloc[0, 1]}")

# Визуализация корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Корреляция между рейтингом и эффективностью')
plt.savefig('data/visualization/correlation_heatmap.png')
plt.close()

# Визуализация зависимости между рейтингом и эффективностью
plt.figure(figsize=(10, 6))
sns.boxplot(x='effective', y='rating', data=train_data)
plt.title('Зависимость между рейтингом и эффективностью')
plt.xlabel('Эффективность (0 - неэффективно, 1 - эффективно)')
plt.ylabel('Рейтинг')
plt.savefig('data/visualization/rating_vs_effective.png')
plt.close()

# Проверка пересечения между обучающей и тестовой выборками
train_reviews = set(train_features.iloc[:, :5000].apply(lambda x: tuple(x), axis=1))
test_reviews = set(test_features.iloc[:, :5000].apply(lambda x: tuple(x), axis=1))
intersection = train_reviews.intersection(test_reviews)
print(f"Количество пересекающихся примеров: {len(intersection)}")
print(f"Процент пересечения: {len(intersection) / len(test_reviews) * 100:.2f}%")

print("Валидация модели завершена!")
