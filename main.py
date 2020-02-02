import numpy
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas
import streamlit
from PIL import Image
from src.plot import plot_pitch, plot_sonar
from src.data_processing import aggregate_data, PlayerData, postgres_connect, get_games, gather_pass_data


streamlit.title("PassSonar")

database_connection = postgres_connect("172.28.0.1", "5432", "soccer", "root", "root")
games = get_games(database_connection)
games["concatenate_game_info"] = games["home_team_name"] + " vs " + games["away_team_name"] + " - " + games["startDate"]

game = streamlit.sidebar.selectbox("game", list(games["concatenate_game_info"]))
background_color = streamlit.sidebar.text_input("background_color", "#1b4d99")
foreground_color = streamlit.sidebar.text_input("foreground_color", "#80A0C6")
filtered_games = games[games["concatenate_game_info"] == game]
game_id = list(filtered_games["game_id"])[0]


fonts = {}
fonts["ObjectSans-Regular"] = font_manager.FontProperties(fname="/usr/local/share/fonts/ObjectSans-Regular.ttf")
fonts["ObjectSans-Heavy"] = font_manager.FontProperties(fname="/usr/local/share/fonts/ObjectSans-Heavy.ttf")

colors = {}
colors["background_color"] = background_color
colors["foreground_color"] = foreground_color
colors["sonar_colors"] = ["#83FFC3","#56FFAE","#00CB69","#00793F"]
colors["text_color"] = "#FEFEFE"
colors["alternative_text_color"] = "#e8e8e8"

texts = {}
texts["title"] = "PassSonar"
texts["game"] = list(filtered_games["home_team_name"] + " vs " + filtered_games["away_team_name"])[0]
texts["date"] = list(filtered_games["startDate"])[0].split("T")[0]


# data = pandas.read_csv("./data/full_sample.csv").dropna(axis=0).query("team_id == '31'")
data = gather_pass_data(database_connection, game_id).dropna(axis=0)
team_id = streamlit.sidebar.radio("team_id", [list(filtered_games["home_team_id"])[0], list(filtered_games["away_team_id"])[0]])

team_data = data.query(f"team_id == '{team_id}'")
players_data = aggregate_data(team_data, 15)

fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(1, 1, 1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_frame_on(False)

plot_pitch(ax, colors["foreground_color"])
plot_sonar(fig, players_data, colors, fonts, texts)

plt.savefig("./img/passsonar.png", facecolor=fig.get_facecolor())
image = Image.open("./img/passsonar.png")
streamlit.image(image, use_column_width=True)