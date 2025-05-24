import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

os.makedirs('../models', exist_ok=True)
os.makedirs('../data/visualization', exist_ok=True)

print("Загрузка данных...")
train_features = pd.read_csv('../data/train_features_corrected.csv')
test_features = pd.read_csv('../data/test_features_corrected.csv')
train_target = pd.read_csv('../data/train_target_corrected.csv')
test_target = pd.read_csv('../data/test_target_corrected.csv')

train_target = train_target.iloc[:, 0]
test_target = test_target.iloc[:, 0]

print(f"Размер обучающей выборки: {train_features.shape}")
print(f"Размер тестовой выборки: {test_features.shape}")

print("\nОбучение моделей...")

print("\n1. Логистическая регрессия")
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(train_features, train_target)
lr_train_pred = lr_model.predict(train_features)
lr_test_pred = lr_model.predict(test_features)

lr_train_accuracy = accuracy_score(train_target, lr_train_pred)
lr_test_accuracy = accuracy_score(test_target, lr_test_pred)
lr_test_precision = precision_score(test_target, lr_test_pred)
lr_test_recall = recall_score(test_target, lr_test_pred)
lr_test_f1 = f1_score(test_target, lr_test_pred)

print(f"Точность на обучающей выборке: {lr_train_accuracy:.4f}")
print(f"Точность на тестовой выборке: {lr_test_accuracy:.4f}")
print(f"Precision на тестовой выборке: {lr_test_precision:.4f}")
print(f"Recall на тестовой выборке: {lr_test_recall:.4f}")
print(f"F1-score на тестовой выборке: {lr_test_f1:.4f}")

joblib.dump(lr_model, '../models/logistic_regression_model.pkl')

print("\n2. Случайный лес")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(train_features, train_target)
rf_train_pred = rf_model.predict(train_features)
rf_test_pred = rf_model.predict(test_features)

rf_train_accuracy = accuracy_score(train_target, rf_train_pred)
rf_test_accuracy = accuracy_score(test_target, rf_test_pred)
rf_test_precision = precision_score(test_target, rf_test_pred)
rf_test_recall = recall_score(test_target, rf_test_pred)
rf_test_f1 = f1_score(test_target, rf_test_pred)

print(f"Точность на обучающей выборке: {rf_train_accuracy:.4f}")
print(f"Точность на тестовой выборке: {rf_test_accuracy:.4f}")
print(f"Precision на тестовой выборке: {rf_test_precision:.4f}")
print(f"Recall на тестовой выборке: {rf_test_recall:.4f}")
print(f"F1-score на тестовой выборке: {rf_test_f1:.4f}")

joblib.dump(rf_model, '../models/random_forest_model.pkl')

print("\n3. Support Vector Machine")
svm_model = SVC(probability=True, random_state=42)
svm_model.fit(train_features, train_target)
svm_train_pred = svm_model.predict(train_features)
svm_test_pred = svm_model.predict(test_features)

svm_train_accuracy = accuracy_score(train_target, svm_train_pred)
svm_test_accuracy = accuracy_score(test_target, svm_test_pred)
svm_test_precision = precision_score(test_target, svm_test_pred)
svm_test_recall = recall_score(test_target, svm_test_pred)
svm_test_f1 = f1_score(test_target, svm_test_pred)

print(f"Точность на обучающей выборке: {svm_train_accuracy:.4f}")
print(f"Точность на тестовой выборке: {svm_test_accuracy:.4f}")
print(f"Precision на тестовой выборке: {svm_test_precision:.4f}")
print(f"Recall на тестовой выборке: {svm_test_recall:.4f}")
print(f"F1-score на тестовой выборке: {svm_test_f1:.4f}")

joblib.dump(svm_model, '../models/svm_model.pkl')

print("\nВизуализация результатов...")

plt.figure(figsize=(10, 8))
cm = confusion_matrix(test_target, rf_test_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Матрица ошибок для модели случайного леса')
plt.xlabel('Предсказанные значения')
plt.ylabel('Истинные значения')
plt.savefig('../data/visualization/confusion_matrix.png')
plt.close()

models = ['Логистическая регрессия', 'Случайный лес', 'SVM']
accuracy = [lr_test_accuracy, rf_test_accuracy, svm_test_accuracy]
precision = [lr_test_precision, rf_test_precision, svm_test_precision]
recall = [lr_test_recall, rf_test_recall, svm_test_recall]
f1 = [lr_test_f1, rf_test_f1, svm_test_f1]

metrics_df = pd.DataFrame({
    'Модель': models,
    'Accuracy': accuracy,
    'Precision': precision,
    'Recall': recall,
    'F1-score': f1
})

metrics_df.to_csv('../data/model_metrics.csv', index=False)

plt.figure(figsize=(12, 8))
metrics_df.set_index('Модель')[['Accuracy', 'Precision', 'Recall', 'F1-score']].plot(kind='bar')
plt.title('Сравнение метрик для разных моделей')
plt.ylabel('Значение метрики')
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('../data/visualization/model_comparison.png')
plt.close()

print("\nОбучение и оценка моделей завершены!")
print(f"Лучшая модель: {models[np.argmax(f1)]} с F1-score: {max(f1):.4f}")
