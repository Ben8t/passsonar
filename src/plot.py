import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def plot_pitch(ax, background_color, line_color):
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
    ax.plot((0.25*pitch_width, 0.25*pitch_width), (0, 0.15*pitch_length), color=line_color)
    ax.plot((0.75*pitch_width, 0.75*pitch_width), (0, 0.15*pitch_length), color=line_color)
    ax.plot((0.25*pitch_width, 0.75*pitch_width), (0.15*pitch_length, 0.15*pitch_length), color=line_color)
    return ax

def simple_sonar(ax, data):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    return ax.bar(list(data.angle_rad), list(data.freq), width=0.2, bottom=0.0)