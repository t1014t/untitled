import OS
from mutiprocessing import process
def run_proc(name):
    print  'Child process %s (%s) Runing...' % (name,os.getpid())
if _name_=='_main_':
    print 'Prant process %s.'%os.getpid()
    for i in range(5):
        p=Process(targe=run_proc,arg=(str(i),))
        print  'Process will start.'
        p.start()
        p.join()
        print 'process endr'