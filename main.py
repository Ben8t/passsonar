import numpy
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas
from src.plot import plot_pitch, plot_sonar
from src.data_processing import aggregate_data, PlayerData


fonts = {}
fonts["ObjectSans-Regular"] = font_manager.FontProperties(fname="/usr/local/share/fonts/ObjectSans-Regular.ttf")
fonts["ObjectSans-Heavy"] = font_manager.FontProperties(fname="/usr/local/share/fonts/ObjectSans-Heavy.ttf")

data = pandas.read_csv("./data/full_sample.csv").dropna(axis=0).query("team_id == '31'")
players_data = aggregate_data(data, 15)
background_color = "#00FF00"


fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(1, 1, 1)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_frame_on(False)
plot_pitch(ax, "white")
plot_sonar(fig, players_data, background_color, fonts)
plt.savefig("./img/passsonar.png", facecolor=fig.get_facecolor())
