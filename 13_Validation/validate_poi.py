#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

sort_keys = '../tools/python2_lesson13_keys.pkl'
data = featureFormat(data_dict, features_list, sort_keys)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

clf = DecisionTreeClassifier()
clf.fit(features, labels)
pred = clf.predict(features)
print "accuracy = ", accuracy_score(labels, pred)
#accuracy =  0.9894736842105263


features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.30, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "accuracy = ", accuracy_score(labels_test, pred)
# accuracy =  0.7241379310344828













