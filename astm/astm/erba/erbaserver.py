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
