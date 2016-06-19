#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





#########################################################
### your code goes here ###
clf = DecisionTreeClassifier(min_samples_split=40)
t0 = time()

clf.fit(features_train, labels_train)
print "Training time :" ,round(time() - t0, 3), "s"

t1 = time()
labels_predicted = clf.predict(features_test)
print "Training time :" ,round(time() - t1, 3), "s"

print(accuracy_score(labels_predicted,labels_test))

print "Training data number of rows :" ,len(features_train[0]) ,"Number of columns :" ,len(features_train[1])

#########################################################
#Follow up tasks

'''
Go into ../tools/email_preprocess.py, and find the line of code that looks like this:
selector = SelectPercentile(f_classif, percentile=10)
Change percentile from 10 to 1, and rerun dt_author_id.py. What’s the number of features now?
Also compute the accuracy when feature percentile is changed to 1 %
'''

#########################################################


