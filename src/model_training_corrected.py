import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pickle
import time

# Загрузка скорректированных данных
print("Загрузка скорректированных данных...")
X_train = pd.read_csv('data/train_features_corrected.csv')
X_test = pd.read_csv('data/test_features_corrected.csv')
y_train = pd.read_csv('data/train_target_corrected.csv').values.ravel()
y_test = pd.read_csv('data/test_target_corrected.csv').values.ravel()

# Функция для оценки модели
def evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    start_time = time.time()
    
    # Обучение модели
    print(f"Обучение модели {model_name}...")
    model.fit(X_train, y_train)
    
    # Предсказания
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Метрики качества
    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    test_precision = precision_score(y_test, y_pred_test)
    test_recall = recall_score(y_test, y_pred_test)
    test_f1 = f1_score(y_test, y_pred_test)
    
    # Матрица ошибок
    cm = confusion_matrix(y_test, y_pred_test)
    
    # Визуализация матрицы ошибок
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Матрица ошибок для {model_name}')
    plt.xlabel('Предсказанные значения')
    plt.ylabel('Истинные значения')
    plt.savefig(f'data/visualization/confusion_matrix_{model_name}.png')
    plt.close()
    
    # Сохранение модели
    with open(f'data/{model_name}_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    end_time = time.time()
    training_time = end_time - start_time
    
    # Вывод результатов
    print(f"\nРезультаты для модели {model_name}:")
    print(f"Время обучения: {training_time:.2f} секунд")
    print(f"Accuracy на обучающей выборке: {train_accuracy:.4f}")
    print(f"Accuracy на тестовой выборке: {test_accuracy:.4f}")
    print(f"Precision на тестовой выборке: {test_precision:.4f}")
    print(f"Recall на тестовой выборке: {test_recall:.4f}")
    print(f"F1-score на тестовой выборке: {test_f1:.4f}")
    print("\nОтчет по классификации:")
    print(classification_report(y_test, y_pred_test))
    
    return {
        'model_name': model_name,
        'training_time': training_time,
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'test_precision': test_precision,
        'test_recall': test_recall,
        'test_f1': test_f1
    }

# Обучение и оценка моделей
models = [
    (LogisticRegression(max_iter=1000, random_state=42), 'lr'),
    (RandomForestClassifier(n_estimators=100, random_state=42), 'rf'),
    # (SVC(kernel='linear', random_state=42), 'svm')  # Закомментировано для экономии времени
]

results = []
for model, name in models:
    result = evaluate_model(model, X_train, X_test, y_train, y_test, name)
    results.append(result)

# Сравнение моделей
results_df = pd.DataFrame(results)
print("\nСравнение моделей:")
print(results_df)

# Визуализация сравнения моделей
plt.figure(figsize=(12, 8))
metrics = ['test_accuracy', 'test_precision', 'test_recall', 'test_f1']
for i, metric in enumerate(metrics):
    plt.subplot(2, 2, i+1)
    sns.barplot(x='model_name', y=metric, data=results_df)
    plt.title(f'{metric}')
    plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('data/visualization/model_comparison.png')
plt.close()

# Выбор лучшей модели по F1-score
best_model_idx = results_df['test_f1'].idxmax()
best_model_name = results_df.loc[best_model_idx, 'model_name']
print(f"\nЛучшая модель по F1-score: {best_model_name}")

# Копирование лучшей модели в best_model.pkl
with open(f'data/{best_model_name}_model.pkl', 'rb') as f:
    best_model = pickle.load(f)
with open('data/best_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)

print("Обучение и оценка моделей завершены!")
