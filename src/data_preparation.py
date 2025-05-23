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