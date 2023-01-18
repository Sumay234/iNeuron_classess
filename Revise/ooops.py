class dect_parser:
    
    def __init__(self,dic):
        if type(dic) != dict:
            raise Exception ("You have to give dictonary ")
        else:
            self.dic = dic
    
    def get_key(self):
        return self.dic.keys()
    
    def get_values(self):
        return self.dic.values()
    
    def take_input(self):
        a=input("Enter key ")
        b=input("Enter value ")
        self.dic[a] = b
        return "input accepted"
        
    def insert_key_value_pair(self,key,value):
        show = self.dic[key] = value
        print(show)
        return ("value_inserted")
    
    def add(self,a,b):
        print (a+b)
        
    def sub(self,a,b):
        return (a-b)