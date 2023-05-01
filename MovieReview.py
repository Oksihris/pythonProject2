import tensorflow as tf
from keras.optimizers import RMSprop
from keras import layers
from keras import Model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import tensorflow_datasets as tfds
import numpy as np


imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)

train_data, test_data = imdb['train'], imdb['test']

training_sentences =[]
training_labels =[]

testing_sentences =[]
testing_labels =[]

for s,l in train_data:
    training_sentences.append(s.numpy().decode('utf8'))
    training_labels.append(l.numpy())

for s,l in test_data:
    testing_sentences.append(s.numpy().decode('utf8'))
    testing_labels.append(l.numpy())

training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)

oov_tok = "<OOV>"
vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type = 'post'

tokenizer = Tokenizer(num_words= vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences, max_len =max_length, truncating=trunc_type)

testing_sequences= tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, max_len=max_length)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

num_epochs=10
model.fit(padded, training_labels_final,  epochs=num_epochs, validation_data=(testing_padded, testing_labels_final))

e = model.layers[0]
weights=e.get_weights()[0]
print(weights.shape)