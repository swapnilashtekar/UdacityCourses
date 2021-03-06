#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn.preprocessing import MinMaxScaler




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)



#Max and Min of Exercised Stock Options

exercised_stock_options_list = []
for key, value in data_dict.iteritems():
    if(value['exercised_stock_options'] != 'NaN'):
        exercised_stock_options_list.append(value['exercised_stock_options'])

print "Exercised stock options : Minimum %s     Maximum %s" %(min(exercised_stock_options_list),max(exercised_stock_options_list))


'''
#Find maximum
max_exercised_stock_options = 0

for person_name in data_dict:
    value = data_dict[person_name]['exercised_stock_options']
    if(value != 'NaN'):
        if(max_exercised_stock_options < value):
            max_exercised_stock_options = value

#Find minimum
min_exercised_stock_options = max_exercised_stock_options

for person_name in data_dict:
    value = data_dict[person_name]['exercised_stock_options']
    if(value != 'NaN'):
        if(min_exercised_stock_options > value):
            min_exercised_stock_options = value


print "Exercised stock options : Minimum %s     Maximum %s" %(min_exercised_stock_options,max_exercised_stock_options)
'''

#Max and Min of Salary


salary_list = []
for key, value in data_dict.iteritems():
    if(value['salary'] != 'NaN'):
        salary_list.append(value['salary'])

print "Salary : Minimum %s     Maximum %s" %(min(salary_list),max(salary_list))

'''
#Find maximum
max_salary = 0

for person_name in data_dict:
    value = data_dict[person_name]['salary']
    if(value != 'NaN'):
        if(max_salary < value):
            max_salary = value

#Find minimum
min_salary = max_salary

for person_name in data_dict:
    value = data_dict[person_name]['salary']
    if(value != 'NaN'):
        if(min_salary > value):
            min_salary = value

print "Salary : Minimum %s     Maximum %s" %(min_salary,max_salary)
'''

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
#MinMaxScaler(data)
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
clf = KMeans(n_clusters=2)
clf.fit(finance_features)
pred = clf.predict(finance_features)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
