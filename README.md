# MNIST-CNN

The goal of this project was to create a model for the MNIST data set and also create a simple python app to test the model in real time.
The model can be tested by downloading `digits_v2.py` and `digit_recognizer_model`. The model can also be created from scratch by running `digit_recognition_model.ipynb`.

## CNN Model

A Convolutional Neural Network was used for model. The structure and the training graphs are shown below. 

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/my_model.png" alt="alt text" width=500 height=1000>

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/accuracy_loss.png" alt="alt text" width=500 height=400>

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/accuracy_val_accuracy.png" alt="alt text" width=500 height=400>

## Draw and Predict App 

Tkinter was used for a canvas to draw numbers on and to display the predictions. Examples are shown below. The model is able to predict the correct letter more than 99% of the time including pretty poorly written numbers. 

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/Demo1.png" alt="alt text" width=250 height=250>

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/Demo2.png" alt="alt text" width=250 height=250>

<img src="https://github.com/Ryusei97/MNIST-CNN/blob/main/Demo3.png" alt="alt text" width=250 height=250>

