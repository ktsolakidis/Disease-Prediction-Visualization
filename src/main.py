import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plts
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

import tkinter 

import os



current_dir = os.path.dirname(__file__)

train_data_path = os.path.join(current_dir,'../Symptoms & Disease Data/Training.csv')
test_data_path = os.path.join(current_dir,'../Symptoms & Disease Data/Testing.csv')

train_data = pd.read_csv(train_data_path)
test_data = pd.read_csv(test_data_path)

symptoms = test_data.keys()[:-1]

X_train = train_data[symptoms]
X_test = test_data[symptoms]


Y_train = train_data['prognosis']
Y_test = test_data['prognosis']


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)


Y_pred = model.predict(X_test)



def heatmap_confusion_matrix():
  cm = confusion_matrix(Y_test, Y_pred)
  
  sns.heatmap(cm, annot=True, fmt='d')
  plts.xlabel('Predicted')
  plts.ylabel('Actual')
  plts.show()



def feature_importances():
   
  feature_importances = model.feature_importances_

  feature_importance_df = pd.DataFrame({'Feature': symptoms, 'Importance': feature_importances})

  feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

  top_20_features = feature_importance_df.sort_values(by='Importance', ascending=False).head(20)
  
  plts.figure(figsize=(10, 20))

  sns.barplot(x='Importance', y='Feature', data=top_20_features)
  plts.yticks(range(len(top_20_features)), top_20_features['Feature'], fontsize=10)

  plts.xlabel('Top 20 Features Importance')
  plts.ylabel('Feature')
  plts.title('Feature Importance Plot')


  plts.show()


def scatter_plot():
  
    plts.figure(figsize=(10, 6))
    plts.scatter(Y_test, Y_pred, alpha=0.5)
    plts.xlabel('Actual Prognosis')
    plts.ylabel('Predicted Prognosis')
    plts.title('Actual vs. Predicted Prognosis')
    plts.show()







root = tkinter.Tk()
root.title("Disease prediction demo script & UI")

frame = tkinter.Frame(root)
frame.pack(side=tkinter.TOP)

label = tkinter.Label(frame, text='Please choose the graph you wish to display')
label.pack()

heatmap_button = tkinter.Button(frame, text='Heatmap of Confusion Matrix', command=heatmap_confusion_matrix,padx=5, pady=3)
features_importance_button = tkinter.Button(frame, text='Features Importance',command=feature_importances,padx=5,pady=3)
scatter_plot_button = tkinter.Button(frame, text='Scatter Plot',command=scatter_plot,padx=5,pady=3)


heatmap_button.pack(side=tkinter.LEFT)
features_importance_button.pack(side=tkinter.LEFT)
scatter_plot_button.pack(side=tkinter.LEFT)




root.mainloop()
