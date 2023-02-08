import cherrypy
from mako.template import Template
import os

#app.config['TEMPLATES_AUTO_RELOAD'] = True # Flask

class index(object):
    @cherrypy.expose
    def index(self):
        template = Template(filename='templates/index.html')
        return template.render()

if __name__ == '__main__':

    cherrypy.config.update({

        'server.socket_host': '0.0.0.0',
        'server.socket_port': os.getenv("PORT", 8080),
        
    })

    PATH = os.path.abspath(os.path.dirname(__file__))

    cherrypy.quickstart(index(), "/", {
        
        "/css": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{PATH}/static/css/"
        }, 

        "/img": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{PATH}/static/img/"
        }
    })

    #app.run(port=os.getenv("PORT", default=5000), host=os.getenv("HOST")) #FLASK
    #serve(app, host=os.getenv("HOST", default='127.0.0.1'), port=os.getenv("PORT", default=5000)) #UVICORN WAITRESS

