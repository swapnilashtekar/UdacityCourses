#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
poiCount = 0
nQuantifiedSalary = 0
nKnownEmailIds = 0
tpCount = 0
tpCountPoi = 0
totalRecords = 0
for person_name in enron_data:
	#Total number of person of interest (POI)
	if(enron_data[person_name]["poi"]==1):
		poiCount += 1
		#Percentage of people in dataset with total payment as NaN
		if(enron_data[person_name]['total_payments'] == 'NaN'):
			tpCountPoi += 1

	if(person_name == 'COLWELL WESLEY'):
		print "From Wesley Colwell to PoI" ,enron_data[person_name]['from_this_person_to_poi']

		#print person_name
		
	#To find number of attributes or parameters in each name
	#print len(enron_data.get(person_name))

	#Print James Prentice's total stock value
	if(person_name == 'PRENTICE JAMES'):
		print "Total stock value of" ,person_name ,"is" ,enron_data[person_name]['total_stock_value']

	#Stock options of Jeffrey Skilling
	if(person_name == 'SKILLING JEFFREY K'):
		print "Exercised stock options" ,person_name ,"are" ,enron_data[person_name]['exercised_stock_options']
		#print "Stock options from Jeffrey Skilling" ,enron_data

	#To know the total payments taken by these people
	if((person_name == 'SKILLING JEFFREY K') | (person_name == 'LAY KENNETH L') | (person_name == 'FASTOW ANDREW S')):
		print "Total payments for" ,person_name ,"is" ,enron_data[person_name]['total_payments']

	#To find quntified salary and known email id
	if(enron_data[person_name]['salary'] != 'NaN'):
		nQuantifiedSalary += 1
	if(enron_data[person_name]['email_address'] != 'NaN'):
		nKnownEmailIds += 1

	#Percentage of people in dataset with total payment as NaN
	if(enron_data[person_name]['total_payments'] == 'NaN'):
		tpCount += 1

	totalRecords += 1

print "Number of PoIs are" ,poiCount
print "Number of people with quantified salary are" ,nQuantifiedSalary
print "Number of people with known email ids are" ,nKnownEmailIds

print "Percentage of people in the dataset have \"NaN\" for their total payement" ,(tpCount*100/totalRecords)
print "Percentage of PoIs in the dataset have \"NaN\" for their total payement" ,(tpCountPoi*100/poiCount)
print len(enron_data)

