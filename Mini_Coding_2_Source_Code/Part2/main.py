import matplotlib.pyplot as plt
import tensorflow as tf
import keras_tuner as kt

"""
Building model and Fine-Tuning Neural Network Hyperparameters 
"""
def build_model(hp):
    n_hidden = hp.Int("n_hidden", min_value=0, max_value=8, default=2)
    n_neurons = hp.Int("n_neurons", min_value=16, max_value=256)
    learning_rate = hp.Float("learning_rate", min_value=1e-4, max_value=1e-2,
                             sampling="log")
    optimizer = hp.Choice("optimizer", values=["sgd", "adam"])
    if optimizer == "sgd":
        optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
    else:
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten())
    for _ in range(n_hidden):
        model.add(tf.keras.layers.Dense(n_neurons, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer,
                  metrics=["accuracy"])
    return model

def main():
    print("Starting ...")
    """
    Downloading the fashion MNIST data    
    """
    fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
    (X_train_full, y_train_full), (X_test, y_test) = fashion_mnist
    X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
    X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]


    random_search_tuner = kt.RandomSearch(
        build_model, objective="val_accuracy", max_trials=5, overwrite=True,
        directory="my_fashion_mnist", project_name="my_rnd_search", seed=42)
    random_search_tuner.search(X_train, y_train, epochs=10,
                               validation_data=(X_valid, y_valid))
    return










if __name__ == "__main__":
    main()