import os
if __name__=='__name__':
    print 'current Process(%s) start ...'%(o.getpid())
    pid=os.fork()
if pid<0:
    print 'error in fork'
elif pid==1:
    print 'i am child  process (%s) and my parnt proces is (%s)',(os.getpid(),os.getppid())
else:
    print  'i(%s) created a child process(%s).',(os.getpid(),pid)