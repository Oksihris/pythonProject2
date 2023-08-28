from tensorflow import keras
import numpy as np
import tensorflow as tf
def house_model():
    # Define input and output tensors with the values for houses with 1 up to 6 bedrooms

    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    ys = np.array([100.0, 150.0, 200.0, 250.0, 300.0, 350.0], dtype=float)

    # Define your model (should be a model with 1 dense layer and 1 unit)
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    # Set the optimizer to Stochastic Gradient Descent
    # and use Mean Squared Error as the loss function
    model.compile(optimizer='sgd', loss='mean_squared_error')

    # Train your model for 1000 epochs by feeding the i/o tensors
    model.fit(xs, ys, epochs=1000)

    return model

model = house_model()

new_x = 7.0
prediction = model.predict([new_x])[0]
print(prediction)