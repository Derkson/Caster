import collections

class Flow:
    def __init__(self,tokenName=None,rate=None,flowDict=None):
        if flowDict == None:
            self.tokenName = tokenName
            self.rate = rate
        else:
            self.tokenName = flowDict["tokenName"]
            self.rate = flowDict["rate"]
    
    def isToken(self,token):
        return self.tokenName == token

class Amount:
    def __init__(self,tokenName=None,amount=None):
        self.tokenName = tokenName
        self.amount = amount

    def isToken(self,token):
        return self.tokenName == token

class Process:
    def __init__(self,name=None,inputs=None,outputs=None,processDict=None):
        if processDict == None:
            self.name = name
            self.inputs = inputs
            self.outputs = outputs
        else:
            self.name = processDict["name"]
            self.inputs = processDict["input"]
            self.outputs = processDict["outputs"]
    
    def doesOutput(self, output):
        return self.outputs.count(output) > 0

class ProcessList(collections.MutableSequence):

    def __init__(self, processListDict):
        self.name = processListDict["name"]
        self.list = list()
        for p in processListDict["processes"]:
            self.list.append(Process(processDict=p))

    def check(self, v):
        if not isinstance(v, Process()):
            raise TypeError

    def __len__(self): return len(self.list)

    def __getitem__(self, i): return self.list[i]

    def __delitem__(self, i): del self.list[i]

    def __setitem__(self, i, v):
        self.check(v)
        self.list[i] = v

    def insert(self, i, v):
        self.check(v)
        self.list.insert(i, v)

    def __str__(self):
        return str(self.list)


class Container:
    def __init__(self,dimensions=None,size=None,constraints=None,containerDict=None):
        if containerDict == None:
            self.dimensions = dimensions
            self.size = size
            self.constraints = constraints
        else:
            self.dimensions = containerDict["dimensions"]
            self.size = containerDict["size"]
            self.constraints = containerDict["constraints"]
    
    def isAbstract(self):
        return self.dimensions == 0

def parseContextDict(contextDict):
    info = {}
    output = []
    world = Container()
    processTypes = []
    processContainers = []

    for k in contextDict:
        if k is "goals":
            try:
                for goal in contextDict[k]:
                    output.append(Flow(flowDict=goal))
            except Exception as excep:
                print("Exception with goals:",excep)
        if k is "container":
            try:
                world = Container(contextDict=contextDict[k])
            except Exception as excep:
                print("Exception with goals:",excep)
        if k is "processTypes":
            try:
                for processType in contextDict[k]:
                    processTypes.append(ProcessList(processType))
            except Exception as excep:
                print("Exception with processTypes:",excep)

    return (info, output, world, processTypes, processContainers)