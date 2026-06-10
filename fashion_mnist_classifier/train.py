import os
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Class Names
class_names = [
    "T-shirt/Top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot"
]

# Load Dataset
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

print("Training Images:", X_train.shape)
print("Testing Images:", X_test.shape)

# Normalize Images
X_train = X_train / 255.0
X_test = X_test / 255.0

# Store original labels for display
y_test_labels = y_test.copy()

# One-Hot Encode Labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build Model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Show Architecture
model.summary()

# Compile Model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)

# Evaluate Model
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy: {accuracy:.4f}")

# Predict Random Test Image
index = np.random.randint(0, len(X_test))

sample = X_test[index]

prediction = model.predict(
    sample.reshape(1, 28, 28),
    verbose=0
)

predicted_class = np.argmax(prediction)

print("\nActual:", class_names[y_test_labels[index]])
print("Predicted:", class_names[predicted_class])

# Show Image
plt.imshow(sample, cmap="gray")
plt.title(
    f"Actual: {class_names[y_test_labels[index]]}\n"
    f"Predicted: {class_names[predicted_class]}"
)
plt.axis("off")
plt.show()

# Save Model
os.makedirs(
    "saved_model",
    exist_ok=True
)

model.save(
    "saved_model/fashion_mnist_model.keras"
)

print("\nModel saved successfully!")