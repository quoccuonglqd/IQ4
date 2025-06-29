import pandas as pd
from joblib import load, dump
# Load existing model
model = load('resources/model.pkl')
# Load data
df = pd.read_csv('resources/sample_data.csv')
X, y = df.drop('success', axis=1), df['success']
# Retrain
model.fit(X, y)
# Save updated model
dump(model, 'resources/new_model.pkl')
print('Training complete, model.pkl updated.')