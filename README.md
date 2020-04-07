# COVID-19
Curve fitting for Covid-19 Cases and Deaths

This script takes data downloaded from the ECDC and fits a curve to the number of cases and the number of deaths in several countries. 

This data is available at :https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide


A polynomial of the 7th degree is chosen on the basis of test scores and RMSE in the "Choosing a Best Fit" portion of the script using a training and testing dataset about the number of US cases. Any country in the dataset may be chosen for fitting by specifying the Country_Id.

This curve fitting process is based on a post by Tirthajyoti Sarkar at https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49.


Then, the 7th degree polynomial is fit to all of the data for a single country and the results are plotted. That country must be specified as the Country_Id. For example, Country_Id="US". The chosen degree of the polnomial may be changed to any degree. 


The Excel file contains the data downloaded from the ECDC. There are two columns for date: "DateRep", which contains the original dates from the ECDC and "Date." The "Date" colun was added and reformatted to remove the timestamp. You need to do this yourself if you download a new ECDC datafile and want the dates to look readable in the plot. Look at the equation in the column of the Covid_Cases_Deaths_from_the_ECDC.xlsx file and copy it.


Please make sure the dataframe file name matches the ECDC Excel file. For example, this provided Excel file is called "COVID-19-geographic-disbtribution-worldwide-2020-04-06.xlsx". The dataframe is specified by "df_covid=pd.read_excel(r'COVID-19-geographic-disbtribution-worldwide-2020-04-06.xlsx',index_col=0)"

