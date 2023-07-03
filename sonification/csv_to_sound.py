#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:03:59 2022

@author: pranet
"""

from astronify.series import SoniSeries
from astropy.table import Table
import pandas as pd

#read_file = pd.read_csv (r'/Users/pranet/Desktop/NRAO Work/2022/backend/testprofile.txt')
#read_file.to_csv(r'/Users/pranet/Desktop/NRAO Work/2022/backend/testprofile.csv', index=None)

data = pd.read_csv("testprofile.csv")
flux = data['-2.237467239417875210e-03'].tolist()
index = range(0, len(flux))

print(flux)


data_table = Table({"time":index, "flux": flux})

data_soni = SoniSeries(data_table)
data_soni.note_spacing = 0.2
data_soni.sonify()
data_soni.play()
#soni_obj.write("outputfile.wav")
