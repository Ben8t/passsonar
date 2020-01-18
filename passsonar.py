import numpy
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc
import pandas
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes


from src.data_processing import process_angles

data = pandas.read_csv("sample.csv").dropna(axis=0)

print(process_angles(data, 15))





# player_id = "104749"
# data = pandas.read_csv("data.csv").query(f"player_id == '{player_id}'")
# angles = [i for i in range(-180, 180+15, 15)]
# lacking_angles = [angle for angle in angles if angle not in list(data.angle)]
# filled_data = {
#     "angle": lacking_angles, 
#     "freq": [0] * len(lacking_angles),
#     "player_id": [data.player_id.unique()[0]] * len(lacking_angles),
#     #"game_id" : [data.game_id.unique()[0]] * len(lacking_angles),
#     "team_id" : [data.team_id.unique()[0]] * len(lacking_angles),
#     "player_name" : [data.player_name.unique()[0]] * len(lacking_angles),
#     "distance" : [0] * len(lacking_angles)
# }

# filled_dataframe = pandas.DataFrame.from_dict(filled_data)
# full_data = data.append(filled_dataframe, ignore_index=True)
# full_data["angle_rad"] = (full_data["angle"] * numpy.pi / 180) - numpy.pi/2
# full_data = full_data.sort_values(by="angle", ascending=True).reset_index(drop=True)


# fig = figure(figsize=(8,8))
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

# N = len(list(full_data.angle_rad))
# theta = list(full_data.angle_rad)
# radii = list(full_data.freq)
# # radii = [sample/sum(list(full_data.freq)) for sample in list(full_data.freq)]
# bars = ax.bar(theta, radii, width=0.2, bottom=0.0)
# print(radii)
# print([0.4 for rad in radii])
# bars2 = ax.bar(theta, [10 for rad in radii], width=0.2, bottom=radii)
# plt.axis('on')

# plt.savefig("other.png")

# # https://matplotlib.org/3.1.1/gallery/axisartist/demo_floating_axes.html
# # https://kite.com/python/examples/5561/matplotlib-plot-a-polar-plot
# # https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html

