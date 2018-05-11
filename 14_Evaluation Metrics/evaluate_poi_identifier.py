#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cross_validation import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.30, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "accuracy:\n", accuracy_score(labels_test, pred)

#0 -> not POI
#1 -> POI
print "number of POIs predicted:\n", sum(pred)

print "How many people are in your test set?:\n", len(pred)
count = 0
for i in pred:
    if i == 0.0:
        count += 1


print "If your identifier predicted 0, What would its accuracy be?:\n", float(count)/len(pred)
print(classification_report(labels_test, pred))
