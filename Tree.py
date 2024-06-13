from termcolor import cprint
from pathlib import Path

print_green = lambda x:cprint(x,'green')

class TreeElement:
    
    
    def __init__(self,data=None,parent=None,children=None):
        self.data = data
        self.children:list[TreeElement] = [] if children is None else children
        self.parent :TreeElement = parent
        if self.parent is not None:
            self.parent.append(self)
    
    
    def append(self,child):
        self.children.append(child)
    
    def getFullPath(self):
        if self.parent is None:
            if self.data is None:
                return ''
            return self.data
        path = self.parent.getFullPath()
        return path+self.data
    
    def display(self):
        print_green(self.getFullPath())
        # just in case        
        if len(self.children)==0:
            return
        for child in self.children:
            child.display()
    
    def create(self):
        # path = ''
        # if self.data is not None:
        #     path = self.data
        
        # create folder in current directory
        # makedirs(dirname(path), exist_ok=True)
        path = self.getFullPath()
        output_file = Path(path)
        if output_file.suffix=='':
            output_file.parent.mkdir(exist_ok=True, parents=True)
        else:
            try:
                output_file.parent.mkdir(exist_ok=True, parents=True)
                output_file.touch(exist_ok=True)
            except FileExistsError as e:
                print(f"File {path} already exists")
                
            # f=open(path,'w')
            # f.write('')
            # f.close()
        # # just in case        
        if len(self.children)==0:
            return
        
        for child in self.children:
            child.create()
            # if len(child.children)>0 :
            #     child.create()
        
        
    def getChildrenData(self):
        return [child.data for child in self.children]
    
    def isChildExist(self,child:str):
        return child in self.getChildrenData()
            
        
        