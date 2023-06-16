import sys
import os
import numpy as np
import pandas as pd
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb")as file_obj:
            dill.dump(obj,file_obj)
    except:
        raise CustomException(e,sys)
        
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in Python Script name [{0}],line number [{1}] error message [{2}]".format()


