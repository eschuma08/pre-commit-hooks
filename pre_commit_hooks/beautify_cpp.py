import argparse
import os
from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import format_cpp

def check( filenames ):
   files_to_check = [ str( os.path.abspath( filename )) for filename in filenames ]
   script_path = os.path.realpath(__file__)
   bin_bath = os.path.join( os.path.dirname( os.path.abspath(script_path) ), '..', 'bin' )
   cfg_file = os.path.join( bin_bath, 'defaults.cfg' )
   #format_cpp( files_to_check, os.path.join( bin_bath, 'AStyle.exe'), ['--style=allman', '--dry-run'] )
   format_cpp( files_to_check, os.path.join( bin_bath, 'AStyle.exe'), ['--style=allman'] )
   
   #for root, dirs, files in os.walk( os.path.join( os.path.dirname( os.path.abspath(script_path) ), '..') ):
   #   path = root.split(os.sep)
   #   print((len(path) - 1) * '---', os.path.basename(root))
   #   for file in files:
   #      print(len(path) * '---', file)
   
   
   #format_cpp( files_to_check, os.path.join( bin_bath, 'uncrustify.exe'), ['-c', '{}'.format(cfg_file), '*.cpp' ] )
   return 0


def main(argv=None):
   parser = argparse.ArgumentParser()
   parser.add_argument( 'filenames', nargs='*', help='Filenames pre-commit believes are changed.', )
   args = parser.parse_args(argv)      
   return check(args.filenames)

if __name__ == '__main__':
   exit(main())