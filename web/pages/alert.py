__author__ = 'Oshri&Yaacov'

from google.appengine.ext.webapp import template
import webapp2

class AlertHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/alert.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/alert', AlertHandler)
], debug=True)