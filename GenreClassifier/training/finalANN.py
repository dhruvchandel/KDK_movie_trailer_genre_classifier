import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import pandas as pd
import numpy as np
import random
from keras.optimizers import Adam
import os

newadam = Adam(lr = 0.00001, amsgrad = True)
class_weight ={0:1.4,1:1,2:1.9,3:2.0}

dataframe = pd.read_csv("C:\\users\\karti\\desktop\\GenreClassifier\\training\\final_results.csv")
X_train = dataframe.iloc[:,1:-1].values
Y_train = dataframe.iloc[:,-1].values

combined = list(zip(X_train,Y_train))
random.shuffle(combined)
X_train , Y_train = zip(*combined)
X_train, Y_train = np.array(X_train), np.array(Y_train)


Y_train = np_utils.to_categorical(Y_train)

model = Sequential()
model.add(Dense(16, activation = 'relu', input_dim = (12)))
model.add(Dense(32,activation="relu"))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(4, activation = 'softmax'))
model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = newadam, metrics = ['accuracy'])

hist = model.fit(X_train, Y_train, epochs = 500,shuffle = True ,validation_split = 0.10, batch_size = 32, class_weight= class_weight)
model.save('C:\\Users\\karti\\Desktop\\GenreClassifier\\finalANNmodel_3Layer_5.h5')

import matplotlib.pyplot as plt

plt.plot(hist.history['loss'],'g', label = 'loss')
plt.plot(hist.history['val_loss'],'b', label = 'val_loss')
plt.plot(hist.history['acc'], 'r', label = 'accuracy')
plt.plot(hist.history['val_acc'], 'orange', label = 'val_accuracy')
plt.legend()
plt.show()