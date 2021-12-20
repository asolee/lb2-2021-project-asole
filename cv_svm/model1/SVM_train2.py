#modules for the svm train and save
from sklearn import svm
import pickle, gzip
import sys
import numpy as np
print("STEP1")

#import the input files
X = (sys.argv[1])
Y = (sys.argv[2])
print("STEP2")

#load file X as np.array
X_m = np.loadtxt(X, dtype="float64")
print(X_m.shape)
print(X_m)

#load file Y as np.array
Y_m = np.loadtxt(Y, dtype="int64")
print(Y_m.shape)
print(Y_m)
print("STEP3")

#create the model
mySVC = svm.SVC(C=2.0, kernel="rbf", gamma=2.0)
mySVC.fit(X_m,Y_m)
print("STEP4")

# Save the model to file ‘myModel.pkl’ using pickle
pickle.dump(mySVC, gzip.open("myModel2.pkl.gz", "w"))
print("STEP5")
