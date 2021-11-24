import sys
from json import load

if __name__ == '__main__':
    #Here goes nothing
    assert(len(sys.argv) == 2)
    file = open(sys.argv[1],'r')

    contextdict = load(file)
    print(contextdict)

    
