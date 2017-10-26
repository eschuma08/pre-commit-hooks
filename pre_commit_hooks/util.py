from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
import shlex


class CalledProcessError(RuntimeError):
   pass


def added_files():
   #return set(cmd_output( 'git', 'diff', '--staged', '--name-only', '--diff-filter=A', ).splitlines())
   return set(cmd_output( 'git', 'diff', '--staged', '--name-only', ).splitlines())
def format_cpp( file_list, executable, args ):
   #cmd = [ str(executable), '--style=allman', '--dry-run']
   cmd = [ str(executable) ] + args
   files = ' '.join( file_list )
   #print('Checking files: {}'.format(file_list))
   #files = file_list[:2]
   print('Checking files: {}'.format(file_list))
   cmd.extend( file_list )
   #return set(cmd_output( 'Astyle.exe', '--style=allman', '--dry-run', shlex.split( files ), ).splitlines())   # '--quiet' 
   return cmd_output2( cmd )

def cmd_output(*cmd, **kwargs):
   retcode = kwargs.pop('retcode', 0)
   popen_kwargs = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
   popen_kwargs.update(kwargs)
   print( 'Command: {}'.format(cmd) )
   proc = subprocess.Popen(cmd, **popen_kwargs)
   print( 'Proc: {}'.format(proc) )
   stdout, stderr = proc.communicate()
   stdout = stdout.decode('UTF-8')
   if stderr is not None:
      stderr = stderr.decode('UTF-8')
   if retcode is not None and proc.returncode != retcode:
      raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
   return stdout
   
def cmd_output2( args ):
   proc = subprocess.Popen(args)
   return 0