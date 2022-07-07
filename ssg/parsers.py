from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions : List[str] = []
    #why is this like this?
    
    def valid_extension(self, extension):
        return (extension in self.extensions)
            
    def parse(self, path : Path, source : Path, dest : Path):
        raise NotImplementedError
        
    def read(self, path):
        with open(path, 'r') as file:
            return file.read()
            
    def write(self, path, dest, content, ext = ".html"):
        full_path = dest/path.with_suffix(ext).name #why not self.?
        with open(full_path) as file:
            content.write(file)
            
    def copy(self, path, source, dest):
        copy2(path, dest/path.relative_to(source))
        
        
    class ResourceParser:
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]
        
        def parse(self, path : Path, source : Path, dest : Path):
            copy(path, source, dest)