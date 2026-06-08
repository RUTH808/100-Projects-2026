XOR Neural Network From Scratch (NumPy)

Goal:
Learn the XOR logic function using a neural network built entirely from scratch without TensorFlow or PyTorch.

Dataset:
Input  Output
0,0    0
0,1    1
1,0    1
1,1    0

Why XOR?
- AND, OR, and NAND can be solved by a single perceptron because they are linearly separable.
- XOR cannot be solved by a single perceptron because no single straight line can separate its classes.
- XOR requires at least one hidden layer, making it the classic problem for understanding neural networks.

Network Architecture:
2 Input Neurons
        ↓
4 Hidden Neurons (Sigmoid)
        ↓
1 Output Neuron (Sigmoid)

Components:

1. Inputs
   - x1 and x2 are fed into the network.

2. Weights
   - Connections between neurons.
   - Determine the importance of each input.

3. Biases
   - Additional adjustable values.
   - Help shift decision boundaries.

4. Activation Function (Sigmoid)
   Formula:
   sigmoid(x) = 1 / (1 + e^(-x))

   Purpose:
   - Converts values into the range 0 to 1.
   - Introduces non-linearity.

5. Forward Propagation
   Input
      ↓
   Hidden Layer
      ↓
   Output Layer
      ↓
   Prediction

   Hidden Layer:
   z1 = X·W1 + b1
   a1 = sigmoid(z1)

   Output Layer:
   z2 = a1·W2 + b2
   prediction = sigmoid(z2)

6. Loss Function
   Mean Squared Error (MSE)

   Loss = (Actual - Predicted)^2

   Purpose:
   - Measures prediction error.
   - Lower loss means better predictions.

7. Backpropagation
   Purpose:
   - Determine which weights caused the error.
   - Compute how much each weight should change.

   Steps:
   Output Error
        ↓
   Output Delta
        ↓
   Hidden Error
        ↓
   Hidden Delta

8. Gradient Descent
   Purpose:
   - Update weights to reduce loss.

   Formula:
   new_weight =
   old_weight - learning_rate × gradient

9. Training Loop
   Repeat thousands of times:

   Forward Propagation
           ↓
   Calculate Loss
           ↓
   Backpropagation
           ↓
   Update Weights

10. Epoch
    One complete pass through all XOR examples.

Expected Learning Process:

Initially:
00 → 0.52
01 → 0.49
10 → 0.54
11 → 0.50

After Training:
00 → 0.03
01 → 0.98
10 → 0.97
11 → 0.04

Code Flow:

1. Create XOR dataset
2. Initialize random weights and biases
3. Define sigmoid function
4. Define sigmoid derivative
5. Perform forward propagation
6. Calculate loss
7. Perform backpropagation
8. Update weights and biases
9. Repeat for many epochs
10. Print final predictions

Key Learning Outcomes:
- Understand neurons, weights, and biases.
- Understand matrix multiplication in neural networks.
- Understand activation functions.
- Understand forward propagation.
- Understand loss functions.
- Understand backpropagation.
- Understand gradient descent.
- Understand why hidden layers are needed.
- Understand why XOR is historically important in neural network research.

Project Summary:
A neural network starts with random weights, makes predictions on XOR inputs, measures its mistakes using a loss function, sends error information backward through the network using backpropagation, updates weights through gradient descent, and gradually learns the XOR pattern that a single perceptron cannot represent.