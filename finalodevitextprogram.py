# -*- coding: utf-8 -*-
"""FinalOdeviTextProgram.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aMN8AdM-6mlegK_s2ZZAxGhKpoPXCtva
"""

# Abdullah Kılıçaslan  2018280085
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
import numpy as np
import pandas as pd

# Verileri oku ve numpy dizisine dönüştür
data= pd.read_csv("/Final-data.csv")

# Encoder kullanarak verileri normalize et
# StandardScaler: Verileri ortalama ve standart sapma değerlerine göre normalize eder
# RobustScaler: Verileri Q1 ve Q3 değerlerine göre normalize eder (outlier değerleri etkilemez)
# MinMaxScaler: Verileri minimum ve maksimum değerlerine göre normalize eder
scaler = StandardScaler()
data = scaler.fit_transform(data)

# K Means kümeleme algoritmasını oluştur
kmeans = KMeans(n_clusters=3)

# Verileri kümelere ayır
labels = kmeans.fit_predict(data)

# Her verinin hangi kümeye ait olduğunu bul
for i, row in enumerate(data):
    cluster = kmeans.predict([row])[0]
    print("Veri {}: Küme {}".format(i, cluster))