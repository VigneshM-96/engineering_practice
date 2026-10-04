import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('real_estate_prices.csv')

#separate features and target
X = df.drop(columns=['property_id', 'price_lakhs'])
y = df['price_lakhs']

#split the train and test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#initialize the model
model = LinearRegression()

#train the model
model.fit(X_train, y_train)

#make predictions
y_pred = model.predict(X_test)

#evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

new_property = pd.DataFrame({
    "area_sqft": [650],
    "bedrooms": [1],
    "property_age": [12],
    "distance_city_km": [14],
    "floor": [2]
})

predicted_price = model.predict(new_property)[0]

print(f"Predicted Price: ₹{predicted_price:.2f} lakhs")