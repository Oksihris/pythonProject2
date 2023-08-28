from tensorflow import keras
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from myCallback import myCallback


callbacks = myCallback()
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

index = 1
np.set_printoptions(linewidth=320)

print(f'LABEL: {train_labels[index]}')
print(f'\nIMAGE PIXEL ARRAY:\n {train_images[index]}')

#plt.imshow(train_images[index], cmap='Greys')

train_images = train_images/255.0
test_images = test_images/255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation= tf.nn.relu),
    tf.keras.layers.Dense(10, activation= tf.nn.softmax)
])

inputs = np.array([[1.0,3.0,4.0,2.0]])
inputs = tf.convert_to_tensor(inputs)
print(f'input to softmax function: {inputs.numpy()}')

outputs= tf.keras.activations.softmax(inputs)
print(f'output of soft max function: {outputs.numpy()}')

sum = tf.reduce_sum(outputs)
print(f'sum of outputs: {sum}')

prediction =np.argmax(outputs)
print(f'class with highest probability: {prediction}')

model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, callbacks=[callbacks])

model.evaluate(test_images, test_labels)