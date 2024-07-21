import json
from src.interface.storage import IStorage
from typing import Union, Dict, Any

class aws_s3(IStorage):

    def __init__(self):
        print('aws3')
    
    def put(self,path:str,name:str,object:Union[str,Dict[str,Any]]):
        if isinstance(object,str):
            with open(object,'r') as file:
                content = file.read()
        elif isinstance(object,dict):
            content = json.dumps(object,indent=4)
        
        return content
        


