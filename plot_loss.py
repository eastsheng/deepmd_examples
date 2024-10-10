import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 设置Mathtext字体，可以选择合适的字体
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'  # 使用Arial字体作为Mathtext字体

# 在这之后进行绘图
path = "./01.train/"
with open(f"{path}lcurve.out") as f:
    headers = f.readline().split()[1:]
lcurve = pd.DataFrame(np.loadtxt(f"{path}lcurve.out"), columns=headers)
legends = ["rmse_e_val", "rmse_e_trn", "rmse_f_val", "rmse_f_trn"]
for legend in legends:
    plt.loglog(lcurve["step"], lcurve[legend], label=legend)
plt.legend()
plt.xlabel("Training steps")
plt.ylabel("Loss")
plt.show()