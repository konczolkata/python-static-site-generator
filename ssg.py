import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = {"source":self.source, "dest":self.dest}
    s1 = Site(**config)
    s1.build()
    
typer.run(main)