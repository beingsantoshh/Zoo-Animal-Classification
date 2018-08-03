#from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import math

data = pd.read_csv("zoo.csv")
data.head(5)

from sklearn.model_selection import train_test_split
all_x = data.iloc[:, 1:17]
all_y = data.iloc[:, 17]
print(all_x)
print(all_y)

#clf = svm.SVC()
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train,y_train)

clf.score(X_test,y_test)

clf.predict(X_test[20:25])

y_test[20:25]   #model predict correctly with accuracy of 88% using SVM but using decison tree clasifier the accurary 100% 
