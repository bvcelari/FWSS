from wsgiref.simple_server import WSGIServer, WSGIRequestHandler

def echo(environ, start_response):
        #N_REG_IN is a File containing an integer... 
        f = open('N_REG_IN', 'r+')
        lNumreg=f.read()
        iNumreg=int(lNumreg.split('\n')[0])
        print("Last:" + str(iNumreg) )
        f.close()
        #Nasty, but empty the file
        f = open('N_REG_IN', 'w')
        iNewreg=iNumreg+1
        res=f.write(str(iNewreg)+"\n")
        print("New :" + str(iNewreg) )
        f.close()
        status = "200 OK"
        headers = [("Content-type", "text/xml")]
        start_response(status, headers)

        return ["""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
</soapenv:Body>
</soapenv:Envelope>
    """ ]

httpd = WSGIServer(('0.0.0.0', 8081), WSGIRequestHandler)
httpd.set_app(echo)
httpd.serve_forever()
