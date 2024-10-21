# split_data.py
import dpdata
import numpy as np

data = dpdata.LabeledSystem("OUTCAR")
data.to("deepmd/npy", "data", set_size=3)
