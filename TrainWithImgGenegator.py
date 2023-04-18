from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.optimizers import RMSprop
import os
from keras import layers
from keras import Model
from keras.applications.inception_v3 import InceptionV3

local_weight_model = '/tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

pre_trained_model = InceptionV3(input_shape=(150,150,3),
                                include_top= False,
                                weights=None)
pre_trained_model.load_weights(local_weight_file)
last_layer = pre_trained_model.get_layer('mixed7')
last_output = last_layer.output

x = layers.Flatten()(last_output)
x= layers.Dense(1024, activation='relu')(x)
x= layers.Dense(1, activation='sigmoid')(x)

model = Model(pre_trained_model.input, x)
model.compile(optimizer= RMSprop(learning_rate=0.0001),
              loss = 'binary_crossentropy',
              metrics= ['acc'])

train_datagen = ImageDataGenerator(rescale = 1./255)