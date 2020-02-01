import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from PIL import Image
import io
import requests

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return matplotlib.colors.LinearSegmentedColormap('CustomMap', cdict)

def plot_pitch(ax, line_color):
    pitch_width = 0.6
    pitch_length = 0.9
    # boundaries
    ax.plot((0, 0), (0, pitch_length), color=line_color)
    ax.plot((0, pitch_width), (pitch_length, pitch_length), color=line_color)
    ax.plot((pitch_width, pitch_width), (pitch_length, 0), color=line_color)
    ax.plot((pitch_width, 0), (0, 0), color=line_color)
    ax.plot((0, pitch_width), (pitch_length/2, pitch_length/2), color=line_color)
    # centre
    centre_circle = plt.Circle((pitch_width/2,pitch_length/2), 0.0915, color=line_color, fill=False)
    centre_spot = plt.Circle((pitch_width/2,pitch_length/2), 0.004, color=line_color)
    ax.add_artist(centre_circle)
    ax.add_artist(centre_spot)
    # boxes
    ax.plot((0.25*pitch_width, 0.25*pitch_width), (0, 0.14*pitch_length), color=line_color)
    ax.plot((0.75*pitch_width, 0.75*pitch_width), (0, 0.14*pitch_length), color=line_color)
    ax.plot((0.25*pitch_width, 0.75*pitch_width), (0.14*pitch_length, 0.14*pitch_length), color=line_color)
    ax.plot((0.35*pitch_width, 0.35*pitch_width), (0, 0.07*pitch_length), color=line_color)
    ax.plot((0.65*pitch_width, 0.65*pitch_width), (0, 0.07*pitch_length), color=line_color)
    ax.plot((0.35*pitch_width, 0.65*pitch_width), (0.07*pitch_length, 0.07*pitch_length), color=line_color)
    arc1 = Arc((0.5*pitch_width, 0.11*pitch_length), height=0.2*pitch_width, width=0.2*pitch_width, angle=0, theta1=26, theta2=154, color=line_color)
    ax.add_patch(arc1)
    penalty_spot1 = plt.Circle((0.5*pitch_width, 0.10*pitch_length), 0.004, color=line_color)
    ax.add_artist(penalty_spot1)
    ax.plot((0.25*pitch_width, 0.25*pitch_width), (pitch_length, 0.86*pitch_length), color=line_color)
    ax.plot((0.75*pitch_width, 0.75*pitch_width), (pitch_length, 0.86*pitch_length), color=line_color)
    ax.plot((0.25*pitch_width, 0.75*pitch_width), (0.86*pitch_length, 0.86*pitch_length), color=line_color)
    ax.plot((0.35*pitch_width, 0.35*pitch_width), (pitch_length, 0.93*pitch_length), color=line_color)
    ax.plot((0.65*pitch_width, 0.65*pitch_width), (pitch_length, 0.93*pitch_length), color=line_color)
    ax.plot((0.35*pitch_width, 0.65*pitch_width), (0.93*pitch_length, 0.93*pitch_length), color=line_color)
    arc2 = Arc((0.5*pitch_width, 0.89*pitch_length), height=0.2*pitch_width, width=0.2*pitch_width, angle=0, theta1=206, theta2=334, color=line_color)
    ax.add_patch(arc2)
    penalty_spot2 = plt.Circle((0.5*pitch_width, 0.90*pitch_length), 0.004, color=line_color)
    ax.add_artist(penalty_spot2)
    return ax

def simple_sonar(ax, player, colors, fonts):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    data_normalizer = matplotlib.colors.Normalize()
    rgb_colors = [matplotlib.colors.ColorConverter().to_rgb(color) for color in colors["sonar_colors"]]
    color_map = make_colormap(rgb_colors)
    ax.set_title(player.name, fontproperties=fonts["ObjectSans-Regular"], color=colors["text_color"], fontsize=12)
    return ax.bar(list(player.angles.angle_rad), list(player.angles.freq), width=0.2, bottom=0.0, color=color_map(data_normalizer(list(player.angles.distance))))

def get_team_logo(team_id):
    url = f"https://d2zywfiolv4f83.cloudfront.net/img/teams/{team_id}.png"
    print(url)
    image_data = requests.get(url).content
    picture = Image.open(io.BytesIO(image_data))
    return picture

def plot_sonar(fig, players_data, colors, fonts, texts):
    for _, player in enumerate(players_data):
        ax = fig.add_axes((player.lineup_horizontal, player.lineup_vertical, 0.2, 0.2), projection="polar", label=str(_))
        simple_sonar(ax, player, colors, fonts)
    fig.patch.set_facecolor(colors["background_color"])
    fig.text(0.155, 0.92, texts["title"], fontproperties=fonts["ObjectSans-Heavy"], fontsize=54, color=colors["text_color"])
    fig.text(0.25, 0.88, texts["game"], fontproperties=fonts["ObjectSans-Regular"], fontsize=24, color=colors["text_color"])
    fig.text(0.25, 0.86, texts["date"], fontproperties=fonts["ObjectSans-Regular"], fontsize=12, color=colors["text_color"])
    team_logo = get_team_logo("31")
    fig.figimage(team_logo, 155, 1200)
    return fig