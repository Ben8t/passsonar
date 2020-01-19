import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas
import matplotlib.gridspec as gridspec
from src.plot import simple_sonar, plot_pitch
from src.data_processing import process_angles

data = pandas.read_csv("data/sample.csv").dropna(axis=0)

processed_data = process_angles(data, 15)

# fig, axes = plt.subplots(3, 3, subplot_kw={"projection":"polar"})
# print(axes)

# simple_sonar(axes[0, 2], processed_data)
# simple_sonar(axes[1, 0], processed_data)
# simple_sonar(axes[2, 1], processed_data)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.4, 0.8])
plot_pitch(ax, "white", "black")
ax1 = fig.add_axes([0.20, 0.30, 0.16, 0.16], projection="polar")
simple_sonar(ax1, processed_data)
# ax2 = fig.add_axes([0.25, 0.50, 0.16, 0.16], projection="polar")
# simple_sonar(ax2, processed_data)
plt.savefig("img/passsonar.png")

