# Disease-Prediction-Visualization

----- TABLE OF CONTENTS -----------

- Description
- Installation / Usage
- Code comments & explanation
- Output & Screenshot examples

This is a simple project for disease prediction and visualization made with python.
The purpose of this project is to demonstrate / give a sample of my work with python.

------ Description --------

The project uses two .csv files as input with test and train data, the training data .csv file consists of 4920 rows of symptoms, and the prediction of the disease.
They will be used to train the model and predict the "prediction" outcome of the test data.

------ Installation / Usage --------

- Clone the repository to your local machine running "git clone "rep_url" in locally in the terminal/cmd of the folder where you wish your project to be placed.
- Run the command "pip install pandas numpy matplotlib seaborn scikit-learn" in order to install all the requirements.
- Run the code with the command "python main.py" in your terminal/cmd


------ Code comments & explanation --------

 - Lines 1 - 11  --> Import the required libraries to analyze the data
 - Lines 15 - 21 --> Read and Load the .csv files into variables
 - Lines 23 - 30 --> Split the test & train data into predictions and results
 - Lines 33 - 37 --> Training the RandomForestClassifier using the training data
 - Lines 41 - 47 --> Define the function to be executed and produce the Heatmap Confusion
 - Lines 51 - 71 --> Define the function to be executed and produce the Feature Importances plot
 - Lines 74 - 81 --> Define the function to be executed and produce the Scatter plot
 - Lines 89 - 110 --> Code for the UI, buttons and functionality


------ Output & Screenshot examples --------

We have three options of visualizing the data output

1) Heatmap Confusion:
 <img width="401" alt="image" src="https://github.com/ktsolakidis/Disease-Prediction-Visualization/assets/106263061/51f75af7-dad3-48e2-a164-062038530cb0">
 
2) Features Importance plot:
 <img width="879" alt="image" src="https://github.com/ktsolakidis/Disease-Prediction-Visualization/assets/106263061/50a3f0a1-29e4-4649-aea9-20093dd6f8cd">

3) Scatter plot
<img width="366" alt="image" src="https://github.com/ktsolakidis/Disease-Prediction-Visualization/assets/106263061/5ac97c4b-58fb-4c0f-bb3a-713df276ff05">





