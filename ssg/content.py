import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
    
    
    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader = FullLoader)
        return cls(metadata, content)
        
    Content(metadata, content)
    
    def __init__(self, data):
        self.data = Content.metadata    
        self.data = [content : "content"]
    
    @property   
    def body(self):
        return self.data["content"]
    
    @property    
    def type(self):
        for type in self.data:
            if type = "type"
                return self.data["type"]
            else:
                return None
                
    @setter
    @property.type() = self.data["type"]
    
    def __iter__(self):
        iter(self.data)
        
    def __len__(self):
        return len(self.data)
        
    def __repr__(self):
        data = []
        return str(data)
        
for key, value in self.data.items():
    if key != "content":
        data[key] = value
        
    
    