from pyramid.view import view_config

class MainViews(object):
    def __init__(self, request):
        self.request = request
        self.matchdict = request.matchdict
    
    @view_config(route_name='main', renderer='main.mako')
    def main(self):
        return {'title':'Main'}