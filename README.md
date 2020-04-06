# COVID-19
Curve fitting for Covid-19 Cases and Death

This script takes data downloaded from the WHO and fits a curve to the number of cases and the number of deaths in several countries. 

A polynomial of the 10th degree is chosen on the basis of test scores and RMSE in the "Choosing a Best Fit" portion of the script using a training and testing dataset about the number of US cases. 

This curve fitting process is based on a post by Tirthajyoti Sarkar at https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49.


Then, the 10th degree polynomial is fit to all of the data for a single country and the results are plotted. That country must be specified as the Country_Id. For example, Country_Id="US".

The Excel file contains the data downloaded from the who. There are two column for date: DateRep, which contains the original dates from the WHO and "Dates." The "Dates" colun was reformatted to remove the timestamp.  
