import dpdata
import numpy as np

# training_systems = dpdata.LabeledSystem(
# 	"./00.data/data/train_data/data_0/",
# 	fmt="deepmd/npy")

training_systems = dpdata.LabeledSystem("./00.data/OUTCAR")

predict = training_systems.predict("./01.train/graph.pb")

# print(training_systems["energies"],predict["energies"])
data = np.vstack((training_systems["energies"],predict["energies"])).T
np.savetxt("./01.train/train_pre.dat",data)
