# filter down warnings in Jupyter notebooks and maybe py files
import warnings
warnings.filterwarnings("ignore")

# setup to access files on Google Drive for Colab
from google.cloud import drive
drtive.mount('/content/drive/') 


# a function for text preprocessing
def lower_replace(series):
    # output = series.str.lower()
    output = series.str.replace(r'\[.*?\]', '', regex=True)
    output = output.str.replace(r'[^\w\s]', '', regex=True)
    output = output.str.lower()
    return output
