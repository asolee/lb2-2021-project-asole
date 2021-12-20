#modules for the svm train and save
from sklearn import svm
import pickle, gzip
import sys
import numpy as np
import ast
print("STEP1")

#import the input files

X = (sys.argv[1])
model = (sys.argv[2])
out = (sys.argv[3])
print("STEP2")

#load file X as np.array
X_m = np.loadtxt(X, dtype="float64")
print(X_m.shape)

#load model
mySVC = pickle.load(gzip.open(model,"r"))

#prediction
pred = mySVC.predict(X_m)

print(pred)
pred = np.asarray(pred)
np.savetxt((sys.argv[3]), pred, fmt='%d')
