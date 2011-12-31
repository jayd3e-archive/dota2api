from pyramid.config import Configurator
from radiantlydire.resources import Site

def main(global_config, **settings):
        config = Configurator(settings=settings,
                              root_factory=Site)
                          
        config.scan('d2')
        return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5010")
