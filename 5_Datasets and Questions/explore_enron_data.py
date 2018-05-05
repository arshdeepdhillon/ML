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

#unfilled featres are labelled as 'NaN'

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#count the number of POIs
poiNames = open("../final_project/poi_names.txt").read().split("\n")
#poiT = [record for record in poiNameRec if "(y)" in record or "(n)" in record]
#print "poiT Total number of POIs:\n", len(poiT), "\n"

poi = 0
poiTotal = 0
nknownEmails = 0
totalNonPayments = 0
nQualifiedSalary = 0
totalNonPaymentsOfPOI = 0

for x in enron_data:
    if enron_data[x]["poi"]:
        poi += 1
        if enron_data[x]["total_payments"] == "NaN":
            totalNonPaymentsOfPOI += 1
        
    if enron_data[x]["salary"] != "NaN":
        nQualifiedSalary += 1
    if enron_data[x]["email_address"] != "NaN":
        nknownEmails += 1
    if enron_data[x]["total_payments"] == "NaN":
        totalNonPayments += 1
        
for y in poiNames:
    if "(y)" in y or "(n)" in y:
        poiTotal += 1

print "How many data points (people) are in the dataset?:\n", len(enron_data), "\n"
print "For each person, how many features are available?:\n",len(enron_data[enron_data.keys()[0]]), "\n"        
print "How many POIs are there in the E+F dataset?:\n", poi, "\n"
print "How many POIs were there total?:\n", poiTotal, "\n"
print "What is the total value of the stock belonging to James Prentice?:\n", enron_data["PRENTICE JAMES"]["total_stock_value"], "\n"
print "How many email messages do we have from Wesley Colwell to persons of interest?:\n", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"], "\n"
print "What is the value of stock options exercised by Jeffrey K Skilling?:\n", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"], "\n"
print "How many persons have quantified salary?:\n", nQualifiedSalary, "\n"
print "How many persons have quantified salary?:\n", nQualifiedSalary, "\n"
print "How many persons have known email address?:\n", nknownEmails, "\n"
print "Home many people in the E+F daaset have 'NaN' for their total payments?:\n", totalNonPayments, "\n"
print "What percentage of people in this dataset as a whole is this?:\n", 100 * (float(totalNonPayments)/len(enron_data)), "\n"
print "What percentage of POIs in the E+F dataset have 'NaN' for their total paymentes?:\n", 100 * (float(totalNonPaymentsOfPOI)/poi), "\n"
