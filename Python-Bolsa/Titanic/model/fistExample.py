import numpy as np
import pandas as pd

#Print you can execute arbitrary python code
train = pd.read_csv("../input/train.csv", dtype={"Age": np.float64}, )
test = pd.read_csv("../input/test.csv", dtype={"Age": np.float64}, )

#Print to standard output, and see the results in the "log" section below after running your script
print("\n\nTop of the training data:")
#print(train.head())

print("\n\nSummary statistics of training data")
#print(train.describe())

# PassengerId (which can be sorted in any order), and Survived which contains your binary predictions: 1 for survived, 0 for did not.
df = train[['PassengerId','Survived']]
df = df[:418]
print(df.head())


#Any files you save will be available in the output tab below
df.to_csv('copy_of_the_training_data.csv', index=False)
