import Path from pathlib

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
    
    def create_dir(self, path):
        directory = dest/relative_to(source)
        directory.mkdir(parents = True, exists_ok = True)
        
    def build():
        self.dest.mkdir(parents = True, exists_ok = True)
        for path in self.source.rglob("*"):
            if path.isdir():
                create_dir(path)