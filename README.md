# python-astm
medical equipment communication ASTM protocol\
it is copy of a python package by Alexander Shorin\
It adds one working example of his package\

 I have tried it for Erba XL-640 biochemistry analyser\
Adapt it to your need\

create a folder 'erba' in /usr/lib/python3.7/astm/astm \
there will be two files in the /usr/lib/python3.7/astm/astm/erba folder\

root@debian:/usr/lib/python3.7/astm/astm# ls erba -l\
total 8\
-rw-r--r-- 1 root root 975 Nov 3 22:02 erbaserver.py\
-rw-r--r-- 1 root root 26 Nov 3 11:40 __init__.py\

==== __init__.py ========
```
from . import erbaserver
```
==== erbaserver.py ======
```
from .. import server
print (dir(server))

class Dispatcher(server.BaseRecordsDispatcher):
    sample_id=''
    def __init__(self, encoding=None):
        server.BaseRecordsDispatcher.__init__(self, encoding=None)
        
    def on_result(self, record):
        print('RESULT:',record)
        print ('update examination set result=\''+record[3]+'\' where code=\''+record[2][3]+'\' and sample_id=\''+self.sample_id+'\'')
    def on_header(self, record):
        print('HEADER:',record)

    def on_comment(self, record):
        print('COMMENT:',record)

    def on_patient(self, record):
        print('PATIENT:',record)

    def on_order(self, record):
        print('ORDER:',record)
        self.sample_id=record[2]
        
    def on_terminator(self, record):
        print('TERMINATOR:',record)
        self.sample_id=''	#to ensure that next result is preceded by non-zero sample_id in order record

    def on_unknown(self, record):
        print('UNKNOWN:',record)
```
=========================
In this way we have extended BaseRecordsDispatcher class for our own use\

Lastly create following file at any place (change ip and port)\

======myserver.py===========
```
#!/usr/bin/python3.7
import astm.astm.erba
s=astm.astm.server.Server(host='192.168.56.1', port=15200,
                 request=None, dispatcher=astm.astm.erba.erbaserver.Dispatcher,
                 timeout=None, encoding=None)
s.serve_forever()
```
=======Run server============
chmod +x myserver.py\
./myserver.py\

use appropriate python version declaration in each file\
Connect client machine with appropriate id and port\
Result and Query from erba XL-640 will be printed in terminal\
This package is unidirectional only.\
I am planning to convert it to bidirectional package\
email:biochemistrygmcs@gmail.com\
