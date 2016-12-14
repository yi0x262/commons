import matplotlib.pyplot as plt
from collections import OrderedDict

from flatten import flatten

class graphplotter(OrderedDict):
    def __new__(self,names,*args,**keys):
        od = super().__new__(self,*args,**keys)
        for name in names:
            print(name)
            od[name]=list()
        return od
    def __init__(self,names):
        pass#for avoid update by arguments
    def __call__(self,name,data):
        """
        name :  str
        data :  numpy   (ndim = 1or2)
                list or list(list())
        """
        self[name].append(flatten(data))#get deepcopy
    def plot(self):
        pass

    def _each_plot(self,axes,x,y,name=None):
        if len(x) != len(y):
            y.resize(len(x))#adjast data length

if __name__ == '__main__':
    pass
