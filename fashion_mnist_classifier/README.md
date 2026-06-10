Project: Fashion-MNIST Clothing Classifier

Objective:
Build a neural network capable of recognizing clothing items from grayscale images in the Fashion-MNIST dataset.

Problem Type:
Multi-Class Classification

The goal is to classify an image into one of 10 clothing categories.

Dataset:
Fashion-MNIST Dataset

Training Images:
60,000

Testing Images:
10,000

Image Size:
28 × 28 pixels

Total Input Features:
784 pixels (after flattening)

Classes:
0 - T-shirt/Top
1 - Trouser
2 - Pullover
3 - Dress
4 - Coat
5 - Sandal
6 - Shirt
7 - Sneaker
8 - Bag
9 - Ankle Boot

Project Workflow:

1. Load Dataset
- Loaded Fashion-MNIST using TensorFlow/Keras.
- Retrieved training and testing image sets.

2. Data Preprocessing

Image Normalization:
- Pixel values originally ranged from 0 to 255.
- Converted values into the range 0 to 1.

Purpose:
- Faster convergence
- More stable neural network training

Label Encoding:
- Converted integer labels into one-hot encoded vectors.

Example:
Class 7 (Sneaker)

Original:
7

One-Hot Encoded:
[0,0,0,0,0,0,0,1,0,0]

3. Neural Network Architecture

Input Layer:
- 28 × 28 image
- Flattened into 784 input features

Architecture:

784 Inputs
      ↓
Dense(128, ReLU)
      ↓
Dense(64, ReLU)
      ↓
Dense(10, Softmax)

Layer Details:

Flatten Layer:
- Converts 28×28 image into a 784-element vector.

Hidden Layer 1:
- 128 neurons
- ReLU activation
- Learns basic visual features such as edges and curves.

Hidden Layer 2:
- 64 neurons
- ReLU activation
- Learns higher-level clothing patterns and shapes.

Output Layer:
- 10 neurons
- Softmax activation
- Produces probabilities for all clothing categories.

4. Activation Functions

ReLU:
Formula:
ReLU(x) = max(0, x)

Purpose:
- Introduces non-linearity
- Enables learning of complex visual patterns

Softmax:
Purpose:
- Converts outputs into probabilities
- Ensures all probabilities sum to 1

Example Output:
T-shirt  = 0.01
Trouser  = 0.02
Dress    = 0.90
Bag      = 0.01

Prediction:
Dress

5. Model Compilation

Optimizer:
Adam

Purpose:
- Efficient weight updates
- Faster convergence

Loss Function:
Categorical Crossentropy

Purpose:
- Measures prediction error for multi-class classification

Metric:
Accuracy

Purpose:
- Tracks percentage of correctly classified images

6. Training Process

For each batch:

Image
  ↓
Forward Propagation
  ↓
Prediction
  ↓
Cross-Entropy Loss
  ↓
Backpropagation
  ↓
Weight Update

Training Parameters:
- Epochs: 5
- Batch Size: 32
- Validation Split: 10%

7. Evaluation

Evaluated model on:
10,000 unseen test images

Measured:
- Test Accuracy

Typical Result:
88%–92% Accuracy

Fashion-MNIST is harder than handwritten digit recognition because many clothing categories have similar visual characteristics.

Examples:
- Shirt vs T-shirt
- Coat vs Pullover
- Sneaker vs Sandal

8. Prediction

Selected a random test image.

Steps:
- Feed image into network
- Generate probability scores
- Select class with highest probability

Example:

Actual:
Sneaker

Predicted:
Sneaker

9. Visualization

Displayed:
- Test image
- Actual class label
- Predicted class label

Purpose:
- Verify model predictions visually

10. Model Saving

Saved trained model as:

saved_model/fashion_mnist_model.keras

Purpose:
- Reuse trained model later
- Avoid retraining every time

Concepts Learned:
- Multi-Class Classification
- Image Classification
- Fashion-MNIST Dataset
- Data Normalization
- One-Hot Encoding
- Dense Neural Networks
- ReLU Activation
- Softmax Activation
- Cross-Entropy Loss
- Adam Optimizer
- Forward Propagation
- Backpropagation
- Model Evaluation
- Prediction Pipeline
- Model Persistence

Outcome:
Successfully built, trained, evaluated, and deployed a neural network that classifies clothing items from grayscale images. The model learned visual patterns from Fashion-MNIST and achieved strong accuracy on previously unseen images while demonstrating the complete workflow of an image classification project.