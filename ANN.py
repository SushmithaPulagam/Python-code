# Artificial Neural Network


# Part 1 - Data Preprocessing

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset
df=pd.read_csv("C:\\Users\\VIAAN\\Desktop\\Deeplearning\\Churn_Modelling.csv")
print(df.describe())
print(df.head())

# Creating independant and dependant data sets
#X is independant dataset
#Y is dependant dataset
X = df.iloc[: , 3:13]
Y = df.iloc[: , 13]

#Geography and Gender are categorical columns and need to create dummy variables using get_dummies()
Geo = pd.get_dummies(X["Geography"])    
Gen = pd.get_dummies(X["Gender"])

#Concatenate the datasets
X = pd.concat([X,Geo,Gen],axis=1)

#Drop the unnecessary columns Geography and Gender
X=X.drop(["Geography","Gender"],axis=1)

#Splitting the dataset into Train and Test data set.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X , Y , test_size = 0.2, random_state=0)

#Feature Scaling - We are doing feature scaling because to make allthe units in the same magnitude.
# If all the features are in the same magnitude,it will be easy for the calculation and back propagation
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#******************************Building ANN model using Keras****************************
#Import all Keras packages and libraries
import keras
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import Dense

# Initialising the empty ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init = 'he_uniform',activation='relu',input_dim = 13))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'he_uniform',activation='relu'))
# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'glorot_uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Fitting the ANN to the Training set
model_history=classifier.fit(X_train, Y_train,validation_split=0.33, batch_size = 10, nb_epoch = 100)

# list all data in history

print(model_history.history.keys())
# summarize history for accuracy
plt.plot(model_history.history['accuracy'])
plt.plot(model_history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

