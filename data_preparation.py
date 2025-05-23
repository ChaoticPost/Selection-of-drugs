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