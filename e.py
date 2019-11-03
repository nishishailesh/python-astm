#!/usr/bin/python3.7
import astm.astm.erba
s=astm.astm.server.Server(host='192.168.56.1', port=15200,
                 request=None, dispatcher=astm.astm.erba.erbaserver.Dispatcher,
                 timeout=None, encoding=None)
s.serve_forever()
