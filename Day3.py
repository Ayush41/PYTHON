# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Function to import the dataset
def importdata():
	balance_data = pd.read_csv(
		'balance-scanle.data',
		sep=',', header=None)

	# Displaying dataset information
	print("Dataset Length: ", len(balance_data))
	print("Dataset Shape: ", balance_data.shape)
	print("Dataset: ", balance_data.head())
	
	return balance_data

def train_using_gini(X_train, X_test, y_train):

	# Creating the classifier object
	clf_gini = DecisionTreeClassifier(criterion="gini",
									random_state=100, max_depth=3, min_samples_leaf=5)

	# Performing training
	clf_gini.fit(X_train, y_train)
	return clf_gini

def tarin_using_entropy(X_train, X_test, y_train):

	# Decision tree with entropy
	clf_entropy = DecisionTreeClassifier(
		criterion="entropy", random_state=100,
		max_depth=3, min_samples_leaf=5)

	# Performing training
	clf_entropy.fit(X_train, y_train)
	return clf_entropy















# Deepanshu Chauhan
# 22011138

# Aditya Dobhal
# 22041272
# B1
# 8750371991