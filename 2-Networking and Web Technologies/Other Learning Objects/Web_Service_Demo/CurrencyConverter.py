import cherrypy

class CurrencyConverter:
    def currency_convert(self,convert=None):
        a=int(convert)
        print("Request received for conversion in web service is : ",convert,"$")
        output=convert,"$ in INR is "+str(a*62)
        return output
    currency_convert.exposed = True
    
cherrypy.config.update({'server.socket_host': '127.0.0.1','server.socket_port': 9999})    
cherrypy.quickstart(CurrencyConverter())

