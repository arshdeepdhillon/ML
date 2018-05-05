#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(C=1.0, gamma = 1.0, kernel='linear')
clf = SVC(C=10000.0, kernel='rbf')

# smaller training set (sliced data set)
# These lines effectively slice the training dataset down to 1% of its original size,
#  tossing out 99% of the training data.
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print "accuracy = ", accuracy_score(labels_test, pred)

print "element 10", pred[10]
print "element 26", pred[26]
print "element 50", pred[50]

#only counts the first class in this 1 which is chris
#print sum(pred)

# count 
from collections import Counter
print(Counter(pred))

#running on the full data set and not sliced the Output:
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 96.156 s
#predicting time: 11.053 s
#accuracy =  0.9908987485779295
#element 10 1
#element 26 0
#element 50 1
#Counter({0: 881, 1: 877})

#########################################################


