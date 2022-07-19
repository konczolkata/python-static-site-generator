from pathlib import Path
#how do these files link up?

class Site:
    def __init__(self, source, dest, parsers = None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []
    
    def create_dir(self, path):
        directory = self.dest/path.relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)
        
    def build(self):
        self.dest.mkdir(parents = True, exist_ok = True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
                #why self?
                
    def load_parser(self, extension):
        for parser in self.parsers:
            if valid_extension(extension):
                return parser
                 
    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, source, dest)
            #why isn't it Parser.parse()
        else:
            print("Not Implemented")