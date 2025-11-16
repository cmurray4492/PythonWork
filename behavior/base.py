# base file for behavoral data science book. Just imports a few libraries
# and some reuseable functions 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols

print("Hello, World!")


def boot_CI_fun(dat_df, metric_fun, B = 20, conf_level = 9/10):
    
    coeff_boot =  []

    # Calculate coeff of interest for each simulation 
    for b in range(B):
        print("beginning iteration number " + str(b) + "\n")
        boot_df = dat_df.groupby("rep ID").sample(n=1200, replace=True)
        coeff = metric_fun(boot_df)
        coeff_boot.append(coeff)

    # Extract confidence interval 
    coeff_boot.sort()
    

