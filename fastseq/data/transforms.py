# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_data.transforms.ipynb (unless otherwise specified).

__all__ = ['NormalizeTS']

# Cell
from fastai2.torch_basics import *
from fastai2.data.all import *
# from pyts.image import GramianAngularField, MarkovTransitionField, RecurrencePlot

# Cell
class NormalizeTS(ItemTransform):
    "Normalize the Time-Series."
    def __init__(self,):
        self.m, self.s = 0, 0
    def encodes(self, o):
        self.m, self.s = torch.mean(o[0],-1,keepdim=True), o[0].std(-1,keepdim=True)+1e-7
        return Tuple([(o[i]-self.m)/self.s for i in range(len(o))])

    def decodes(self, o):
        return Tuple([o[i]*self.s+self.m for i in range(len(o))])
