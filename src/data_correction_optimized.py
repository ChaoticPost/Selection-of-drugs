import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import gc

# Загрузка предобработанных данных
print("Загрузка предобработанных данных...")
train_data = pd.read_csv('data/train_preprocessed.csv')
test_data = pd.read_csv('data/test_preprocessed.csv')

# Объединение данных для правильного разделения
print("Объединение данных для правильного разделения...")
all_data = pd.concat([train_data, test_data], axis=0)
all_data = all_data.reset_index(drop=True)

# Создание признаков с помощью TF-IDF (с меньшим количеством признаков для оптимизации)
print("Создание признаков с помощью TF-IDF...")
tfidf_vectorizer = TfidfVectorizer(max_features=3000)
tfidf_all = tfidf_vectorizer.fit_transform(all_data['clean_review'])

# Преобразование разреженных матриц в DataFrame
print("Преобразование разреженных матриц в DataFrame...")
tfidf_all_df = pd.DataFrame(tfidf_all.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Освобождение памяти
del tfidf_all
gc.collect()

# Добавление дополнительных признаков (без рейтинга, чтобы избежать утечки)
print("Добавление дополнительных признаков...")
condition_dummies = pd.get_dummies(all_data['condition'], prefix='condition')
all_features = pd.concat([tfidf_all_df, condition_dummies], axis=1)

# Освобождение памяти
del tfidf_all_df, condition_dummies
gc.collect()

# Целевая переменная
all_target = all_data['effective']

# Разделение на обучающую и тестовую выборки
print("Разделение на обучающую и тестовую выборки...")
X_train, X_test, y_train, y_test = train_test_split(
    all_features, all_target, test_size=0.2, random_state=42, stratify=all_target
)

# Сохранение скорректированных признаков и целевых переменных
print("Сохранение скорректированных признаков и целевых переменных...")
X_train.to_csv('data/train_features_corrected.csv', index=False)
X_test.to_csv('data/test_features_corrected.csv', index=False)
y_train.to_csv('data/train_target_corrected.csv', index=False)
y_test.to_csv('data/test_target_corrected.csv', index=False)

print("Оптимизированная корректировка данных завершена!")
