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

colors = {}
colors["background_color"] = "#1b4d99"
colors["foreground_color"] = "#80A0C6"
colors["sonar_colors"] = ["#83FFC3","#56FFAE","#00CB69","#00793F"]
colors["text_color"] = "#FEFEFE"
colors["alternative_text_color"] = "#e8e8e8"

texts = {}
texts["title"] = "PassSonar"
texts["game"] = "Team A vs Team B"
texts["date"] = "01/01/2020"


data = pandas.read_csv("./data/full_sample.csv").dropna(axis=0).query("team_id == '31'")
players_data = aggregate_data(data, 15)

fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(1, 1, 1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_frame_on(False)

plot_pitch(ax, colors["foreground_color"])
plot_sonar(fig, players_data, colors, fonts, texts)

plt.savefig("./img/passsonar.png", facecolor=fig.get_facecolor())
