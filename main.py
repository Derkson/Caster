import sys
from json import load

if __name__ == 'main':
    #Here goes nothing
    assert(len(sys.argv) == 2)
    file = open(sys.argv[1],'r')

    sysdict = load(file)
    print(sysdict)