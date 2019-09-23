#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import http.server
import ssl

server_address = ('localhost', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="cetificate.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()


# In[ ]:




