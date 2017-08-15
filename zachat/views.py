from pyramid.view import view_config
import wxpy
from .wechat import wechat_init
@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'zachat'}

@view_config(route_name='send', renderer='templates/mytemplate.jinja2')
def send_message(request):
    bot = wxpy.bot
    if not bot.alive:
        bot = wechat_init()
    return {'project': bot}