import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes
from src.plot import simple_sonar
from src.data_processing import process_angles

data = pandas.read_csv("data/sample.csv").dropna(axis=0)

processed_data = process_angles(data, 15)

fig, axes = plt.subplots(1, 3, subplot_kw={"projection":"polar"})

simple_sonar(axes[0], processed_data)
simple_sonar(axes[1], processed_data)
simple_sonar(axes[2], processed_data)

plt.savefig("img/passsonar.png")

