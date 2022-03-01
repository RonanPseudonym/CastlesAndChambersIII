from enum import Enum
# from dataclasses import dataclass

class DustType(Enum):
    STR  = 0
    NOUN = 100
    VERB = 101

class Dust:
    def __init__(self, data_type, content):
        self.content = str(content)
        
        if isinstance(data_type, str):
            data_type = DustType(vars(DustType)[data_type.upper()]) 
        self.data_type = data_type
    
    def __repr__(self):
        return f"{{{self.content} : {self.data_type.name}}}"
    
    def __str__(self):
        match self.data_type.name:
            case _:
                return self.__repr__()
    
class DustStr:
    def __init__(self, *args):
        self.inner = list(args)
                
    def __getitem__(self, indices):
        print(indices)
        
    def __repr__(self):
        return " ".join(map(lambda x: x if isinstance(x, str) else repr(x), self.inner))
    
    def __str__(self):
        return " ".join(map(str, self.inner))
    
    def __lshift__(self, x):
        if isinstance(x, Dust):
            self.inner.append(x)
        if isinstance(x, str):    
            inner = ""
            is_dust = False
            
            for i in x: # i really ought to use regexes here, but they're so scary like {08*[3^2l]}x2 shfiudjhsfdis what fuckin kill me now
                if i == "{":
                    if inner.strip():
                        self.inner.append(inner)
                        
                    inner = ""
                    is_dust = True
                    continue
                    
                if i == "}" and is_dust:
                    self.inner.append(Dust(*list(map(lambda x: x.strip(), inner.split("|")))))
                    inner = ""
                    continue   
                
                inner += i  
                        
        # elif isinstance(x, tuple):
        #     self.inner.append(Dust(x[0], x[1]))