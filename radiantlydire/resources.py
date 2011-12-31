from pyramid.security import Allow, Everyone

class Site(object):
    __acl__ = [(Allow, Everyone, 'everyone')]

    def __init__(self, request):
        pass