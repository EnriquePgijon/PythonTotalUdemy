import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matriz, plot_confusion_matrix
from sklearn import tree

from google.colab import drive
drive.mount('/content/gdrive')

df= pd.read_csv('titanic.csv')
df.head()

X= df.drop('Sobreviviente',axis=1)
y=df.Sobreviviente

X.head()
y.head()

arbol= DecisionTreeClassifier(max_depth=2,random_state=42)

arbol.fit(X,y)

pred_y= arbol.predict(X)

print("Precision: ", accuracy_score(pred_y,y))

confusion_matrix(y,pred_y)

plot_confusion_matrix(arbol,X,y,cmap="plt.cm.Blues",values_format='.0f')

plot_confusion_matrix(arbol,X,y,cmap="plt.cm.Blues",values_format='.2f',normalize=true)

plt.figure(figsize=(10,8))
tree.plot_tree(arbol,filled=True,feature_names=X.columns)
plt.show()

importancias= arbol.feature_importances_
columnas=X.columns

sns.barplot(columnas,importancias)
plt.title('Importancia de cada atributo')
plt.show()