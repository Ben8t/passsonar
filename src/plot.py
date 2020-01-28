import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

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

def simple_sonar(ax, player):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    ax.set_title(player.name)
    return ax.bar(list(player.angles.angle_rad), list(player.angles.freq), width=0.2, bottom=0.0)

def plot_sonar(fig, players_data, background_color):
    for _, player in enumerate(players_data):
        ax = fig.add_axes((player.lineup_horizontal, player.lineup_vertical, 0.2, 0.2), projection="polar", label=str(_))
        simple_sonar(ax, player)
    fig.patch.set_facecolor(background_color)
    fig.text(0.15, 0.9, "PassSonar", fontsize=32)
    return fig