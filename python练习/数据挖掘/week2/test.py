import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("ex2price.csv")
data.plot.scatter(x="Date",y="Total number of applicants")

features = data['riqi'].values.reshape(-1, 1)
target = data['Total number of applicants'].values.reshape(-1, 1)
# features = StandardScaler().fit_transform(data['riqi'].values.reshape(-1, 1))
# target = StandardScaler().fit_transform(data['Total number of license issued'].values.reshape(-1, 1))
regression = LinearRegression()
model = regression.fit(features,target)
print(model.intercept_)
print(model.coef_)
re = model.predict(features)
plt.plot(features,re,c='orange')
plt.title("Regression-Total number of applicants")
plt.show()