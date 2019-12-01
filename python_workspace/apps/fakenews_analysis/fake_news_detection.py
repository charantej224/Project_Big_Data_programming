import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np


class FakeNewDetector:

    def __init__(self):
        self.tf_idf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        self.pac_model = None

    def prepare_model(self):
        df = pd.read_csv('data_set/news.csv', encoding='latin-1')
        df.head(10)
        x_train, x_test, y_train, y_test = train_test_split(df.text, df.label, test_size=0.2, random_state=7)
        tfidf_train = self.tf_idf_vectorizer.fit_transform(x_train)
        tfidf_test = self.tf_idf_vectorizer.transform(x_test)
        self.pac_model = PassiveAggressiveClassifier(max_iter=50)
        result = self.pac_model.fit(tfidf_train, y_train)
        print(result)
        y_pred = self.pac_model.predict(tfidf_test)
        score = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {round(score * 100, 2)}%')
        confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])

    def predict_outcome(self, input_message):
        test_array = np.array([input_message])
        tfidf_test = self.tf_idf_vectorizer.transform(test_array)
        return self.pac_model.predict(tfidf_test)

    def predict_outcome_list(self, input_message_list):
        test_array = np.array(input_message_list)
        tfidf_test = self.tf_idf_vectorizer.transform(test_array)
        return self.pac_model.predict(tfidf_test)
