import os
import numpy as np
import pandas as pd

# Import and clean dataset
current_directory = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_directory, "Iris.csv")
iris = pd.read_csv(file_path)
iris = iris.drop('Id',axis=1)
print(iris.head())