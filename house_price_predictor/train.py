import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# --------------------------
# Load Dataset
# --------------------------

data = pd.read_csv("dataset.csv")

print("\nDataset Preview:")
print(data.head())

# --------------------------
# Features and Target
# --------------------------

X = data[["area", "bedrooms", "bathrooms", "age"]]

y = data[["price"]]

# --------------------------
# Normalize Features
# --------------------------

feature_scaler = MinMaxScaler()

X_scaled = feature_scaler.fit_transform(X)

# --------------------------
# Normalize Target
# --------------------------

price_scaler = MinMaxScaler()

y_scaled = price_scaler.fit_transform(y)

# --------------------------
# Train Test Split
# --------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_scaled,
    test_size=0.2,
    random_state=42
)

# --------------------------
# Build Neural Network
# --------------------------

model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1)
])

# --------------------------
# Compile Model
# --------------------------

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# --------------------------
# Model Summary
# --------------------------

print("\nModel Summary:")
model.summary()

# --------------------------
# Train Model
# --------------------------

history = model.fit(
    X_train,
    y_train,
    epochs=200,
    verbose=1
)

# --------------------------
# Evaluate Model
# --------------------------

loss, mae = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nMean Absolute Error (Normalized):", round(mae, 4))

# --------------------------
# Predict New House
# --------------------------

new_house = pd.DataFrame(
    [[2100, 3, 3, 3]],
    columns=["area", "bedrooms", "bathrooms", "age"]
)

new_house_scaled = feature_scaler.transform(
    new_house
)

predicted_price_scaled = model.predict(
    new_house_scaled,
    verbose=0
)

predicted_price = price_scaler.inverse_transform(
    predicted_price_scaled
)

print("\nNew House Details:")
print("Area:", 2100)
print("Bedrooms:", 3)
print("Bathrooms:", 3)
print("Age:", 3)

print("\nPredicted House Price:")
print(f"${predicted_price[0][0]:,.2f}")

# --------------------------
# Save Model
# --------------------------

os.makedirs(
    "saved_model",
    exist_ok=True
)

model.save(
    "saved_model/house_price_model.keras"
)

print("\nModel saved successfully!")