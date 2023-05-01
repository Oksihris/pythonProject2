import tensorflow as tf
from keras.optimizers import RMSprop
from keras import layers
from keras import Model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import tensorflow_datasets as tfds
import numpy as np

imdb_plaintext, info_plaintext = tfds.load("imdb_reviews", with_info=True, as_supervised=True)

imdb, info = tfds.load("imdb_reviews/subwords8k", with_info=True, as_supervised=True)

train_data, test_data = imdb['train'], imdb['test']

info_plaintext.features

tokenizer = info.features['text'].encoder
for example in imdb_plaintext['train'].take(2):
  print(example[0].numpy())

info.features

for example in imdb['train'].take(2):
  print(example)

for example in imdb['train'].take(2):
  print(tokenizer.decode(example[0]))
print(tokenizer.subwords)

# Get the train set
train_data = imdb_plaintext['train']

# Initialize sentences list
training_sentences = []

# Loop over all training examples and save to the list
for s,_ in train_data:
  training_sentences.append(s.numpy().decode('utf8'))

vocab_size = 10000
oov_tok = '<OOV>'

# Initialize the Tokenizer class
tokenizer_plaintext = Tokenizer(num_words = 10000, oov_token=oov_tok)

# Generate the word index dictionary for the training sentences
tokenizer_plaintext.fit_on_texts(training_sentences)

# Generate the training sequences
sequences = tokenizer_plaintext.texts_to_sequences(training_sentences)

tokenized_string = tokenizer.encode(training_sentences[0])
for ts in tokenized_string:
  print ('{} ----> {}'.format(ts, tokenizer.decode([ts])))

embedding_dim = 64

tokenized_string = tokenizer.encode(training_sentences[0])
print(tokenized_string)

# Decode the sequence
original_string = tokenizer.decode(tokenized_string)

# Print the result
print (original_string)

BUFFER_SIZE = 10000
BATCH_SIZE = 64

# Shuffle the training data
train_dataset = train_data.shuffle(BUFFER_SIZE)

# Batch and pad the datasets to the maximum length of the sequences
train_dataset = train_dataset.padded_batch(BATCH_SIZE)
test_dataset = test_data.padded_batch(BATCH_SIZE)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, embedding_dim),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Print the model summary
model.summary()

num_epochs = 10

# Set the training parameters
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

# Start training
history = model.fit(train_dataset, epochs=num_epochs, validation_data=test_dataset)