import os

from data import common
<<<<<<< HEAD
=======
from data import srdata
>>>>>>> refs/remotes/origin/dataloader_modify
from data import vsrdata

import numpy as np

import torch
import torch.utils.data as data

# Data loader for CDVL videos
class CDVL_VIDEO(vsrdata.VSRData):

    def __init__(self, args, name='CDVL_VIDEO', train=True):
        super(CDVL_VIDEO, self).__init__(args, name=name, train=train)


    def _scan(self):
        names_hr, names_lr = super(CDVL_VIDEO, self)._scan()
        names_hr = names_hr[self.begin - 1:self.end]
        names_lr = names_lr[self.begin - 1:self.end]

        return names_hr, names_lr
        
    def _set_filesystem(self, dir_data):
        ################################################
        #                                              #
        # Fill in your directory with your own template#
        #                                              #
        ################################################
        if self.args.template == "SY":
            super(CDVL_VIDEO, self)._set_filesystem(dir_data)

        if self.args.template == "JH_video":
            print("Loading CDVL videos")
            self.apath = os.path.join(dir_data, self.name)
            self.dir_hr = os.path.join(self.apath, 'HR')
            self.dir_lr = os.path.join(self.apath, 'LR')
            print("HR path:", self.dir_hr)
            print("LR path:", self.dir_lr)