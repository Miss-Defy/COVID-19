# COVID-19
Curve fitting for Covid-19 Cases and Death

This script takes data downloaded from the ECDC and fits a curve to the number of cases and the number of deaths in several countries. 

This data is available at :https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide


The Excel file contains the data downloaded from the ECDC. There are two column for date: DateRep, which contains the original dates from the ECDC and "Dates." The "Dates" colun was added and reformatted to remove the timestamp. The Day_Number column added as well and increases each day by one, starting from the first date provided by the WHO: 12/31/2019.


A polynomial of the 10th degree is chosen on the basis of test scores and RMSE in the "Choosing a Best Fit" portion of the script using a training and testing dataset about the number of US cases. 

This curve fitting process is based on a post by Tirthajyoti Sarkar at https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49.


Then, the 10th degree polynomial is fit to all of the data for a single country and the results are plotted. That country must be specified as the Country_Id. For example, Country_Id="US".

The Excel file contains the data downloaded from the ECDC. There are two column for date: DateRep, which contains the original dates from the ECDC and "Dates." The "Dates" colun was added and reformatted to remove the timestamp. The Day_Number column added as well and increases each day by one, starting from the first date provided by the ECDC: 12/31/2019.
