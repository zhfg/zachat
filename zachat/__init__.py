from pyramid.config import Configurator
from pyramid.events import ApplicationCreated

#from .wechat import *

# "config" below is assumed to be an instance of a
# pyramid.config.Configurator object




def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
#    config.add_subscriber(wechat_init, ApplicationCreated)
    config.add_route('home', '/')
#    config.add_route('send', '/send/{group}/{msg}')
    config.add_route('send', '/send')
    config.scan()
    return config.make_wsgi_app()
