import typer
import Site from ssg.site

def function(source = "content", dest = "dist"):
    config = {"source":source, "dest":dest}
    s1 = Site(**config)
    s1.build()
    
typer.run(main)