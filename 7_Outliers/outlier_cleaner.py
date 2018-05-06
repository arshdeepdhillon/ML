#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = [(actual - predicted)**2 for actual, predicted in zip(net_worths, predictions)]
    complete_data = zip(ages, net_worths, errors)
    
    # key=lambda t: t[2] -> this will sort based on the 2nd element in pair
    complete_data = sorted(complete_data, key=lambda t: t[2])    

    #keep only 81 points (90 * 0.9 = 81)
    slice_size = (int) (len(complete_data) * 0.9)
    cleaned_data = complete_data[:slice_size]
    
    
    return cleaned_data

