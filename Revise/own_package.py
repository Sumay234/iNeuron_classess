import logging
logging.basicConfig(filename="own_packa.log", level=logging.DEBUG,format="%(asctime)s %(levelname)   %(message)s")

logging.info("this is my info log")
logging.warning("this is my warning log")
logging.debug("this is my debug log")
logging.error("this is my error log")


class oops_task:
    
    def __init__ (self,it_is_list,a_tuple,dictionary):
        self.it_is_list=it_is_list
        self.a_tuple=a_tuple
        self.dictionary=dictionary
        
    def get_list(self):
        try:
            if type(it_is_list) == list:
                logging.debug("Its is a list: ",self.it_is_list)
        except Exception as e:
            logging.exception("Pls enter dictionary",e)
                
    def get_tuple(self):
        try:
            if type(a_tuple) == tuple:
                logging.debug("its a tuple: ",self.a_tuple)
        except Exception as e:
            logging.exception("pls enter a tuple",e)
            
    def get_dictionary(self):
        try:
            if type(dictionary) == dict:
                logging.info("its a dictionary: ",self.dictionary)
        except Exception as e:
            logging.exception("Pls give a dictonary",e)