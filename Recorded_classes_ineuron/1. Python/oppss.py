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
    
    
class dect_parser_1:
    
    def __init__(self,dic):
        if type(dic) != dict:
            raise Exception ("You have to give dictonary ")
        else:
            self.dic = dic
    
    def get_key_1(self):
        return self.dic.keys()
    
    def get_values_1(self):
        return self.dic.values()
    
    def take_input_1(self):
        a=input("Enter key ")
        b=input("Enter value ")
        self.dic[a] = b
        return "input accepted"
        
    def insert_key_value_pair_1(self,key,value):
        show = self.dic[key] = value
        print(show)
        return ("value_inserted")
    
class dect_parser_2:
    
    def __init__(self,dic):
        if type(dic) != dict:
            raise Exception ("You have to give dictonary ")
        else:
            self.dic = dic
    
    def get_key_2(self):
        return self.dic.keys()
    
    def get_values_2(self):
        return self.dic.values()
    
    def take_input_2(self):
        a=input("Enter key ")
        b=input("Enter value ")
        self.dic[a] = b
        return "input accepted"
        
    def insert_key_value_pair_2(self,key,value):
        show = self.dic[key] = value
        print(show)
        return ("value_inserted")
    
    
class dect_parser_3:
    
    def __init__(self,dic):
        if type(dic) != dict:
            raise Exception ("You have to give dictonary ")
        else:
            self.dic = dic
    
    def get_key_3(self):
        return self.dic.keys()
    
    def get_values_3(self):
        return self.dic.values()
    
    def take_input_3(self):
        a=input("Enter key ")
        b=input("Enter value ")
        self.dic[a] = b
        return "input accepted"
        
    def insert_key_value_pair_3(self,key,value):
        show = self.dic[key] = value
        print(show)
        return ("value_inserted")