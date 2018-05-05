#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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

# import the module
from sklearn.naive_bayes import GaussianNB

# create the classifier
clf = GaussianNB()

# fit it using training features and training labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


# create a pred vector by passing in the features to predict
t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"


from sklearn.metrics import accuracy_score
# get the accuracy by of our pred
# accuracy_score(true_labels, our_predicted_labels)
print accuracy_score(labels_test, pred)


#########################################################


