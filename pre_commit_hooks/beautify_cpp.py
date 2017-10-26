import argparse
import os
from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import CalledProcessError

def check( filenames ):
   #files_to_check = set([ str( os.path.abspath( filename )) for filename in filenames ]) + (added_files)
   files_to_check = added_files() & set(filenames) 
   script_path = os.path.realpath(__file__)
   bin_bath = os.path.join( os.path.dirname( os.path.abspath(script_path) ), '..', 'bin' )
   #cfg_file = os.path.join( bin_bath, 'defaults.cfg' )
   #format_cpp( files_to_check, os.path.join( bin_bath, 'AStyle.exe'), ['--style=allman', '--dry-run'] )
   
   #    format_cpp( files_to_check, os.path.join( bin_bath, 'AStyle.exe'), ['--style=google', '--indent=spaces', '--delete-empty-lines', '--pad-oper', '--pad-comma', '--pad-paren', '--pad-header',  '--max-code-length=80', '--close-templates', '--break-after-logical', '--lineend=linux', '--suffix=none'] )
   
   #for root, dirs, files in os.walk( os.path.join( os.path.dirname( os.path.abspath(script_path) ), '..') ):
   #   path = root.split(os.sep)
   #   print((len(path) - 1) * '---', os.path.basename(root))
   #   for file in files:
   #      print(len(path) * '---', file)
   
   
   #format_cpp( files_to_check, os.path.join( bin_bath, 'uncrustify.exe'), ['-c', '{}'.format(cfg_file), '*.cpp' ] )
   exe = os.path.join( bin_bath, 'AStyle.exe')
   try:
#      ret = cmd_output( str(exe), '--style=google', '--indent=spaces', '--delete-empty-lines', '--pad-oper', '--pad-comma', '--pad-paren', '--pad-header',  '--max-code-length=80', '--close-templates', '--break-after-logical', '--lineend=linux', '--suffix=none', ' '.join( files_to_check )  )
      ret = cmd_output( str(exe), '--style=google', '--indent=spaces',  '--max-code-length=80', **files_to_check )
   except CalledProcessError:
      pass

   return 1


def main(argv=None):
   parser = argparse.ArgumentParser()
   parser.add_argument( 'filenames', nargs='*', help='Filenames pre-commit believes are changed.', )
   args = parser.parse_args(argv)      
   return check(args.filenames)

if __name__ == '__main__':
   exit(main())