import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

#Load the dataset
df = pd.read_csv('healthcare_dataset.csv')

#separate features and target
X = df.drop(columns=['patient_id', 'diabetes'])
y = df['diabetes']

#encoding categorical variables
X = pd.get_dummies(
    X,
    columns=['physical_activity'],
    drop_first=True
)

#split the dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#create model
model = LogisticRegression()

#train model
model.fit(X_train_scaled, y_train)

#predict
y_pred = model.predict(X_test_scaled)

#probability
y_probability = model.predict_proba(X_test_scaled)[:, 1]

#evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

#display prediction
result = X_test.copy()
result['actual'] = y_test
result['predicted'] = y_pred
result['probability'] = y_probability

print("\nPredictions:")
print(result)