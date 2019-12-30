import pandas as pd
import numpy as np 
import pickle
import joblib

# Verinin Okunması #
column = ['yorum']
df = pd.read_csv('comments.csv',encoding = 'utf-8',sep = '"')
df.columns = column
df.info()
#Veri setindeki Türkçe Dolgu kelimlerinin kaldırılması 
def remove_stopwords(df_fon):
    stopwords = open('turkce-stop-words','r').read().split()
    df_fon['stopwords_removed'] = list(map(lambda doc:
        [word for word in doc if word not in stopwords],df_fon['yorum']))

remove_stopwords(df)
# Veri setinde Positivity adlı bir sütun oluşturalım ve başlangıçta tüm değerlere bir olarak atayalım  
df['Positivity'] = 1
df.Positivity.iloc[200:] = 0

# Şimdi, verileri "yorum" ve "Positivity" sütunlarını kullanarak rastgele eğitim ve test alt kümelerini bölüştürelim ve 
# ardından ilk girişi ve eğitim setinin şeklini yazalım
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(df['yorum'],df['Positivity'],test_size = 0.20 ,random_state = 0)

#CountVectorizer'ı başlatıyoruz ve eğitim verilerimizi uyguluyoruz
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(encoding ='iso-8859-9').fit(X_train)
feature_list = vect.get_feature_names()
joblib.dump(feature_list, 'vocabulary.pkl')
#X_Train'deki belgeleri bir belge terim matrisine dönüştürüyoruz
X_train_vectorizer = vect.transform(X_train)

#Bu özellik matrisi X_train_vectorizer'e dayanarak lojistik Regresyon sınıflandırıcını eğiteceğiz
from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(X_train_vectorizer , Y_train)

pickle.dump(regressor, open('model.pkl', 'wb'))  

#loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
from sklearn.metrics import roc_auc_score
predictions = model.predict(vect.transform(X_test))
print('"0,745" AUC: ', roc_auc_score(Y_test, predictions))







































