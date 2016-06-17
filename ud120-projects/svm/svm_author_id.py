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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()

#Adding below two lines to slice the training data, so that training time
# will be reduced, but we are trading the accuracy here.
'''
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
'''

clf.fit(features_train, labels_train)
print "Training time :" ,round(time() - t0, 3), "s"

t1 = time()
labels_predicted = clf.predict(features_test)
print "Training time :" ,round(time() - t1, 3), "s"

print(accuracy_score(labels_predicted,labels_test))

# This tells 10th, 26th and 50th labels from predicted labels
print(labels_predicted[10])
print(labels_predicted[26])
print(labels_predicted[50])

#Count tells the labels predicted as 1 which is for Chris
count = 0
for i in labels_predicted :
	if i == 1:
		count += 1



print(count)

#########################################################


