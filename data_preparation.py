import pandas as pd

# Пример обработки
df = pd.read_csv('data/drugsComTrain_raw.csv')
df.dropna(inplace=True)
df.to_csv('data/train_features_corrected.csv', index=False)
print("Предобработка завершена")
