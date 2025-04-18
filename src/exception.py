import sys 
import logging

def error_message_details(error, error_details:sys):
    _,_,exc_tab = error_details.exc_info()
    
    file_name = exc_tab.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format(
    
    file_name,exc_tab.tb_lineno, str(error))
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)
    
    def __str__(self):
        return self.error_message   


if __name__== "__main__":
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Devide by zero")
        raise CustomException(e,sys)
        
    