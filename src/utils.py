import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured in Python Script name [{0}],line number [{1}] error message [{2}]".format()


