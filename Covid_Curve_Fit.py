import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt




df_covid=pd.read_excel(r'Covid_Cases_Deaths_from_the_WHO.xlsx',index_col=0)



US_covid = df_covid.loc[df_covid['GeoId'] == "US"]

CN_covid = df_covid.loc[df_covid['GeoId'] == "CN"]

FR_covid = df_covid.loc[df_covid['GeoId'] == "FR"]

IT_covid = df_covid.loc[df_covid['GeoId'] == "IT"]

ES_covid = df_covid.loc[df_covid['GeoId'] == "ES"]

DE_covid = df_covid.loc[df_covid['GeoId'] == "DE"] 



# Dates are the same for all countries
Dates = US_covid.loc[:,'Date'].values
Dates=np.flip(Dates)




#######################################
######### Choosing a Best Fit #########
#######################################

Country_Id="US"
#################################################### 

Country_covid = df_covid.loc[df_covid['GeoId'] == Country_Id]
Day_Number_np=Country_covid['Day_Number'].values
# Cases- get values
Cases_np=Country_covid['Cases'].values
X_transpose=Day_Number_np
y_transpose=Cases_np

# Min and max degree of polynomials features to consider
degree_min = 2
degree_max = 20

# Test/train split
test_set_fraction=.3
X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(X_transpose,y_transpose,test_size=test_set_fraction)
X_train = X_train_trans.reshape(-1,1)
X_test = X_test_trans.reshape(-1,1)
y_train = y_train_trans.reshape(-1,1)
y_test = y_test_trans.reshape(-1,1)
    
Test_Scores=np.array([])
RMSEs=np.array([])
Degrees=np.arange(degree_min,degree_max+1)
Data=np.zeros([Degrees.shape[0],3])
# Make a pipeline model with polynomial transformation and Linear regression, run it for increasing degree of polynomial (complexity of the model)
for degree in range(degree_min,degree_max+1):
    model = make_pipeline(PolynomialFeatures(degree, interaction_only=False), LinearRegression())
    model.fit(X_train,y_train)
    test_pred = np.array(model.predict(X_test))
    RMSE=np.sqrt(np.sum(np.square(test_pred-y_test)))
    test_score = model.score(X_test,y_test)
    Test_Scores=np.append(Test_Scores,test_score)
    RMSEs=np.append(RMSEs,RMSE)
    print("for degree=",degree,"test_score=",test_score)
    print("for degree=",degree,"RMSE=",RMSE)

Data[:,0]=Degrees
Data[:,1]=Test_Scores
Data[:,2]=RMSEs




############################################################
######### Plotting Cases and Death for Some Country #########
############################################################

# Country ID Options:
#   United States Country ID: "US"
#   China Country ID:"CN"
#   France Country ID:"FR"
#   Italy Country ID: "IT"
#   Spain Country ID: "ES"
#   Germany Country ID:"DE"


# Choose Country ID
Country_Id="US"
####################################################

Country_covid = df_covid.loc[df_covid['GeoId'] == Country_Id]
Day_Number_np=Country_covid['Day_Number'].values
# Cases- get values
Cases_np=Country_covid['Cases'].values
X_transpose=Day_Number_np
y_transpose=Cases_np
# Deaths- get values
Deaths_np=Country_covid['Deaths'].values
y_D_transpose=Deaths_np

# Say we choose degree = 10
chosen_degree = 10

X_All = X_transpose.reshape(-1,1)
y_All = y_transpose.reshape(-1,1)
y_D_All = y_D_transpose.reshape(-1,1)

model = make_pipeline(PolynomialFeatures(chosen_degree, interaction_only=False), LinearRegression())
MODEL_C=model.fit(X_All,y_All)
YMODEL_C=model.predict(X_All)

MODEL_D=model.fit(X_All,y_D_All)
YMODEL_D=model.predict(X_All)


#### Make Figure
fig, ax = plt.subplots()
fig= plt.scatter(X_All, y_D_All,  color='gray')
fig= plt.plot(X_All, YMODEL_D, color='red', linewidth=3)
fig= plt.scatter(X_All, y_All,  color='black')
fig= plt.plot(X_All, YMODEL_C, color='blue', linewidth=3)

for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    plt.xticks(range(len(Dates)), Dates, fontsize=9)
    n = 5  # Keeps every nth label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]
plt.yticks(())
ax.set_ylabel("Covid-19 Cases")
ax.set_xlabel("Day")
ax.set_title("US Covid-19 Cases")

plt.show()










