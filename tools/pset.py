import numpy as np
import pandas as pd

from mr_clean import outlierIQRCapping

testdf = pd.DataFrame(np.random.randn(5250, 3), columns=list("ABC"))
testdf.insert(len(testdf.columns), "category", "Category A")

testdf.loc[3000:4499, ["category"]] = "Category B"
testdf.loc[4500:5250, ["category"]] = "Cat C"

testdf.insert(
    len(testdf.columns),
    "Date",
    np.random.choice(pd.date_range("2022-10-01", "2024-11-30"), len(testdf)),
)

testdf.at[0, "A"] = 11
testdf.at[4, "A"] = 19
print(testdf)
outlierIQRCapping(testdf, "A")
print(testdf)
