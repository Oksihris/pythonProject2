from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.optimizers import RMSprop
from keras import layers
from keras import Model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences



sentences =[
    'I love my dog',
    'I love my cat',
    'You love my dog!',
    'Do you think my dog is amazing?'
]
tokenizer = Tokenizer(num_words= 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

test_data = [
    'i really love my dog',
    'my dog loves manatee'
]

test_seq = tokenizer.texts_to_sequences(test_data)

padded = pad_sequences(sequences, padding= 'post', truncating='post')
print(test_seq)
print("\nWord index = ", word_index)
print("\nSequence = ", sequences)
print("\nPadded Sequences: ")
print(padded.shape)
print(padded)
