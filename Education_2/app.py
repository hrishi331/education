# Import libraries
import pandas as pd
import numpy as np
import pickle

# Import pickle model
with open("Pickles/reg.pkl","rb") as file:
    reg = pickle.load(file) 

# array(['Hours Studied', 'Previous Scores', 'Extracurricular Activities','Sleep Hours',
#        'Sample Question Papers Practiced'], dtype=object)

hs = int(input("Hours studied / day : "))
ps = float(input("Previous scores in % : "))
print("""Extracarricular activities : 
      1. Yes
      2. No""")
eca = input("Select option number : ")
sh = int(input("Sleep Hours /day : "))
sqp = int(input("Sample question papaer practiced : "))

input_dict = {'Hours Studied':[hs], 
              'Previous Scores':[ps], 
              'Extracurricular Activities':[eca],
              'Sleep Hours':[sh],
              'Sample Question Papers Practiced':[sqp]}

X_sample = pd.DataFrame(input_dict)

y_pred = reg.predict(X_sample)

print(f"Likely to get {y_pred}%")

