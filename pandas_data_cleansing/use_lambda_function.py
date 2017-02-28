

# cleaning big data using python - LOOK AT IT - VERY IMPORTANT!
# http://stackoverflow.com/questions/13867294/cleaning-big-data-using-python

import os
import sys
from tabulate import tabulate

import pandas as pd
import numpy as np

import config

def main1():
    project_directory_path = os.path.dirname(sys.argv[0])  

    data_begin_path = os.path.join(project_directory_path, config.DATA_BEGIN)  
#     NaN - stands for Not A Number, and this is not equal to 0.
    
    data_end_path = os.path.join(project_directory_path, config.DATA_END)  

    df_data = pd.read_csv(data_begin_path, sep=",") 
    df_data = df_data.iloc[:,:]
        
#     Python supports the creation of anonymous functions 
#     (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda"
#     df_data["Sales"] = df_data["Sales"].apply(lambda x: int(x) if str.isdigit(x) else np.NaN)    
    df_data["Sales"] = df_data["Sales"].apply(lambda x: float(x) if str.isdecimal(x) else 0.0)  
    
    print(tabulate(df_data, headers='keys', tablefmt='rst'))
     
    print(df_data.info())
    
    df_data.to_csv(data_end_path)

if __name__ == '__main__':
    main1()