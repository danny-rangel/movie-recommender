import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
from change_data import transform_data, group_movies_by_viewer, count_columns


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
    DONT NEED TO RUN THIS CODE ANYMORE UNLESS WE DELETE THE NEW GROUPED DATA
    PLS DONT RUN
    PLS
"""

# transform_data("data/combined_data_1.txt", "new_data/new_data_1.txt")
# transform_data("data/combined_data_2.txt", "new_data/new_data_2.txt")
# transform_data("data/combined_data_3.txt", "new_data/new_data_3.txt")
# transform_data("data/combined_data_4.txt", "new_data/new_data_4.txt")


# group_movies_by_viewer("new_data/new_data_1.txt", "new_data/grouped_data_1.csv")
# group_movies_by_viewer("new_data/new_data_2.txt", "new_data/grouped_data_2.csv")
# group_movies_by_viewer("new_data/new_data_3.txt", "new_data/grouped_data_3.csv")
# group_movies_by_viewer("new_data/new_data_4.txt", "new_data/grouped_data_4.csv")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


columns = count_columns("new_data/test.csv")

dataset = pd.read_csv(
    "new_data/test.csv", sep=",", header=None, names=list(range(0, columns))
)

print(dataset)

transactions = []
for i in range(0, len(dataset)):
    transactions.append(list(dataset.iloc[i, :].values))

rules = apriori(transactions, min_support=0.1, min_confidence=0.1, min_lift=4)

results = list(rules)
print(results)
