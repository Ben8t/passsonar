import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas
from src.plot import plot_pitch, plot_sonar
from src.data_processing import aggregate_data, PlayerData

data = pandas.read_csv("./data/full_sample.csv").dropna(axis=0).query("team_id == '31'")
players_data = aggregate_data(data, 15)

fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(1, 1, 1)
plot_pitch(ax, "white", "black")
plot_sonar(fig, players_data)

plt.savefig("./img/passsonar.png")
