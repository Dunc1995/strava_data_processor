#!/usr/bin/env python

#region #*----------Modules----------
import argparse

#endregion

#region #*----------Constants----------
A_TEST_SECRET = None
#endregion

#region #*----------Methods----------

#endregion

#region #*----------Main Function----------
#? Main application function.
#? This is executed by default unless this script is imported as a module.
def main(args):
    print("Successful Workflow!")
    print(str(A_TEST_SECRET))
#endregion

#region #!----------Application Entry Point----------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='template')
    parser.add_argument('--example', '-e', help='This is an example argument')
    args = parser.parse_args()
    main(args)
#endregion