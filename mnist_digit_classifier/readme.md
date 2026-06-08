Project: MNIST Handwritten Digit Classifier

Objective:
Build a neural network that can recognize handwritten digits (0–9) from images in the MNIST dataset.

Dataset:
- MNIST dataset
- 60,000 training images
- 10,000 testing images
- Each image is 28×28 pixels
- Each image belongs to one of 10 classes (digits 0–9)

Data Preprocessing:
1. Loaded the MNIST dataset using TensorFlow/Keras.
2. Normalized pixel values from 0–255 to 0–1.
3. Converted digit labels into one-hot encoded vectors.

Neural Network Architecture:
Input Layer:
- 28×28 image
- Flattened into 784 input features

Hidden Layer 1:
- 128 neurons
- ReLU activation

Hidden Layer 2:
- 64 neurons
- ReLU activation

Output Layer:
- 10 neurons
- Softmax activation
- Produces probability scores for digits 0–9

Training Configuration:
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metric: Accuracy
- Epochs: 5
- Batch Size: 32
- Validation Split: 10%

Training Process:
1. Forward propagation generates predictions.
2. Cross-entropy loss measures prediction error.
3. Backpropagation computes gradients.
4. Adam optimizer updates weights.
5. Process repeats for multiple epochs until the model learns digit patterns.

Evaluation:
- Tested on 10,000 unseen images.
- Achieved approximately 97–99% accuracy.
- Verified predictions by comparing predicted digits with actual labels.

Output:
- Model predicts handwritten digits from image inputs.
- Displays prediction probabilities using Softmax.
- Saves the trained model as mnist_model.keras for future use.

Concepts Learned:
- Neural Networks
- Dense Layers
- ReLU Activation
- Softmax Activation
- Image Classification
- Data Normalization
- One-Hot Encoding
- Forward Propagation
- Backpropagation
- Cross-Entropy Loss
- Adam Optimizer
- Model Evaluation
- Model Saving and Inference

Outcome:
Successfully built, trained, evaluated, and deployed a neural network capable of recognizing handwritten digits from images with high accuracy.
