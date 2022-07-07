from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions = List[str]
    
    def valid_extension(self, extension):
        extension in self.extensions
        
    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        
        raise NotImplementedError
        
    def read(self, path):
        with open(self.path) as file:
            return read(file)
            
    def write(self, path, dest, content, ext = ".html"):
        full_path = self.dest/path.with_suffix(self.ext).name
        with open(full_path) as file:
            self.content.write(file)
            
    def copy(self, path, source, dest):
        copy2(self.path, self.dest/self.path.relative_to(self.source))
        
        
    class ResourceParser:
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]
        
        def parse(self, path, source, dest):
            self.path = Path(path)
            self.source = Path(source)
            self.dest = Path(dest)
            copy(path, source, dest)