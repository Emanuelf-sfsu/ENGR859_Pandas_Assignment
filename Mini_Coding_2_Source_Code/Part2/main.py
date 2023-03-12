import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt

import tensorflow as tf

def main():
    print("Starting ...")
    """
    Prepare the Dataset 
    """
    # Downloading the fashion MNIST data
    fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist
    X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
    X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

    class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                   "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    # This code will show you the image.
    # extra code

    plt.imshow(X_train[0], cmap="binary")
    plt.axis('off')
    plt.show()

    """
    Creating the model using the Sequential API
    """
    tf.random.set_seed(42)
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(300, activation="relu"))
    model.add(tf.keras.layers.Dense(100, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))

    print(model.summary())

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])





    """
    Training and evaluating the model
    """
    history = model.fit(X_train, y_train, epochs=30,
                        validation_data=(X_valid, y_valid))
    return










if __name__ == "__main__":
    main()