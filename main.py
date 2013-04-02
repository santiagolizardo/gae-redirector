
import webapp2
import config

routes = [ webapp2.Route( r'/<:.*>', webapp2.RedirectHandler, defaults = { '_uri': config.REDIRECTION_URL, '_permanent': config.REDIRECTION_IS_PERMANENT } ) ]
app = webapp2.WSGIApplication( routes, debug = False )

