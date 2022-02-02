from os import name
import sys
from json import load

import context

if __name__ == '__main__':
    #Here goes nothing
    assert(len(sys.argv) == 2)
    file = open(sys.argv[1],'r')

    contextdict = load(file)
    print(contextdict)
    (info, output, world, processTypes, processContainers) = context.parseContextDict(contextdict)
    #What do I want the data structure to be?
    #this next portion will be created assuming any conversions needed
    #on the original context dict have been done already.

    #working backwards approach
    print(output)
