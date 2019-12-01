from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plot


class SentimentAnalysis:

    def __init__(self):
        self.model = None
        self.graph = tf.get_default_graph()

    def prepare_model(self):
        df = pd.read_csv('data_set/train_data.csv', encoding='latin-1')
        print(df.head())
        sentences = df['comment'].values
        y = df['sentiment'].values
        # tokenizing data
        tokenizer = Tokenizer(num_words=2000)
        tokenizer.fit_on_texts(sentences)
        # getting the vocabulary of data
        sentences = tokenizer.texts_to_matrix(sentences)

        le = preprocessing.LabelEncoder()
        y = le.fit_transform(y)
        X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

        # Number of features
        # print(input_dim)
        self.model = Sequential()
        self.model.add(layers.Dense(56, input_dim=2000, activation='relu'))
        self.model.add(layers.Dense(3, activation='sigmoid'))
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
        history = self.model.fit(X_train, y_train, epochs=20, verbose=True, validation_data=(X_test, y_test),
                                 batch_size=256)
        plot.plot(history.history['loss'])
        plot.title('model loss')
        plot.ylabel('loss')
        plot.xlabel('epoch')
        plot.legend(['train', 'test'], loc='upper left')
        plot.show()

    def predict_outcome(self, input_message):
        a = np.array([input_message])
        tokenizer = Tokenizer(num_words=2000)
        tokenizer.fit_on_texts(a)
        sentences = tokenizer.texts_to_matrix(a)
        with self.graph.as_default():
            return self.model.predict_classes(sentences)

    def predict_outcome_list(self, input_message_list):
        a = np.array(input_message_list)
        tokenizer = Tokenizer(num_words=2000)
        tokenizer.fit_on_texts(a)
        sentences = tokenizer.texts_to_matrix(a)
        with self.graph.as_default():
            return self.model.predict_classes(sentences)
