import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Загрузка предобработанных данных
print("Загрузка предобработанных данных...")
train_data = pd.read_csv('data/train_preprocessed.csv')
test_data = pd.read_csv('data/test_preprocessed.csv')

# Создание признаков с помощью TF-IDF
print("Создание признаков с помощью TF-IDF...")
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
tfidf_train = tfidf_vectorizer.fit_transform(train_data['clean_review'])
tfidf_test = tfidf_vectorizer.transform(test_data['clean_review'])

# Преобразование разреженных матриц в DataFrame
tfidf_train_df = pd.DataFrame(tfidf_train.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
tfidf_test_df = pd.DataFrame(tfidf_test.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Добавление дополнительных признаков
train_features = pd.concat([
    tfidf_train_df,
    pd.get_dummies(train_data['condition'], prefix='condition'),
    train_data[['rating']]
], axis=1)

test_features = pd.concat([
    tfidf_test_df,
    pd.get_dummies(test_data['condition'], prefix='condition'),
    test_data[['rating']]
], axis=1)

# Целевая переменная
train_target = train_data['effective']
test_target = test_data['effective']

# Сохранение признаков и целевых переменных
print("Сохранение признаков и целевых переменных...")
train_features.to_csv('data/train_features.csv', index=False)
test_features.to_csv('data/test_features.csv', index=False)
train_target.to_csv('data/train_target.csv', index=False)
test_target.to_csv('data/test_target.csv', index=False)

print("Разделение данных завершено!")
