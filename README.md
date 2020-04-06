# COVID-19
Curve fitting for Covid-19 Cases and Death

This script takes data downloaded from the WHO and fits a curve to the number of cases and the number of deaths in several countries. 

A polynomial of the 10th degree is chosen on the basis of test score and RMSE in the "choosing a beft fit" portion of the script using a training and testing dataset.


Then, the 10th degree polynomial is fit to all of the data and the results are plotted.


The Excel file contains the data downloaded from the who. There are two column for date: DateRep, which contains the original dates from the WHO and "Dates." The "Dates" colun was reformatted to remove the timestamp.  
