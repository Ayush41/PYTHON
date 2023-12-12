import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import warnings;
import seaborn as sb;
warnings.filterwarnings("ignore")
# Load the dataset

print("program initialized")
# dataset = pd.read_csv('bank.csv')

dataset = pd.read_csv('bank.csv')
print(dataset.head())
# Display the first few rows of the dataset
print(dataset.head())