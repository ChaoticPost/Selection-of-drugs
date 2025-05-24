import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
import os

warnings.filterwarnings('ignore')

# Создание директории для визуализаций, если она не существует
os.makedirs('../data/visualization', exist_ok=True)

# Загрузка разделенных данных
print("Загрузка разделенных данных...")
train_data = pd.read_csv('../data/train_preprocessed.csv')
test_data = pd.read_csv('../data/test_preprocessed.csv')
print(f"Размер обучающей выборки: {train_data.shape}")
print(f"Размер тестовой выборки: {test_data.shape}")

# Проверка корреляции между признаками и целевой переменной
print("\nПроверка корреляции между признаками и целевой переменной...")
numeric_columns = ['rating', 'effective']
correlation = train_data[numeric_columns].corr()
print("Матрица корреляции:")
print(correlation)

# Визуализация корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Корреляция между признаками и целевой переменной')
plt.savefig('../data/visualization/correlation_heatmap.png')
plt.close()

# Проверка связи между рейтингом и эффективностью
print("\nПроверка связи между рейтингом и эффективностью...")
plt.figure(figsize=(10, 6))
sns.boxplot(x='effective', y='rating', data=train_data)
plt.title('Связь между рейтингом и эффективностью')
plt.savefig('../data/visualization/rating_vs_effective.png')
plt.close()

# Проверка определения эффективности
print("\nПроверка определения эффективности...")
print("Правило определения эффективности: effective = 1 if rating >= 7 else 0")
print("Распределение рейтингов и эффективности:")
rating_effective = pd.crosstab(train_data['rating'], train_data['effective'])
print(rating_effective)

# Проверка на утечку данных - сравнение определения эффективности в train и test
print("\nПроверка на утечку данных - сравнение определения эффективности в train и test...")
# Пересчитываем эффективность на основе рейтинга
train_data['recalculated_effective'] = train_data['rating'].apply(lambda x: 1 if x >= 7 else 0)
test_data['recalculated_effective'] = test_data['rating'].apply(lambda x: 1 if x >= 7 else 0)

# Сравниваем с существующей эффективностью
train_match = (train_data['effective'] == train_data['recalculated_effective']).mean()
test_match = (test_data['effective'] == test_data['recalculated_effective']).mean()
print(f"Доля совпадений в train: {train_match:.4f}")
print(f"Доля совпадений в test: {test_match:.4f}")

# Если совпадение 100%, то эффективность напрямую вычисляется из рейтинга
if train_match > 0.99 and test_match > 0.99:
    print("\nВЫЯВЛЕНА ПРОБЛЕМА: Целевая переменная 'effective' напрямую вычисляется из признака 'rating'!")
    print("Это объясняет идеальные метрики моделей, так как они просто 'запоминают' правило.")

# Проверка на дублирование данных между train и test
print("\nПроверка на дублирование данных между train и test...")
# Создаем уникальные идентификаторы для каждой строки
train_data['row_id'] = train_data['drugName'] + '_' + train_data['condition'] + '_' + train_data['rating'].astype(str)
test_data['row_id'] = test_data['drugName'] + '_' + test_data['condition'] + '_' + test_data['rating'].astype(str)

# Проверяем пересечение
train_ids = set(train_data['row_id'])
test_ids = set(test_data['row_id'])
intersection = train_ids.intersection(test_ids)
print(f"Количество дублирующихся строк между train и test: {len(intersection)}")
print(f"Процент дублирования: {len(intersection) / len(test_ids):.4%}")

# Рекомендации по исправлению
print("\nРекомендации по исправлению проблем:")
if train_match > 0.99 and test_match > 0.99:
    print("1. Удалить признак 'rating' из обучающих данных, так как он напрямую определяет целевую переменную")
    print("2. Создать новую целевую переменную, которая не будет напрямую вычисляться из признаков")
    print("3. Использовать другие признаки, такие как текст отзыва, для предсказания эффективности")

if len(intersection) > 0:
    print("4. Обеспечить полное разделение данных между обучающей и тестовой выборками")
    print("5. Использовать стратификацию по другим признакам, не связанным напрямую с целевой переменной")

print("\nВалидация модели завершена!")
