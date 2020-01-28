import numpy
import pandas
from math import atan2, sqrt

def compute_angle(row, degree_range):
    return - degree_range * round((atan2(row.y_end - row.y_begin, row.x_end - row.x_begin) * 180 / numpy.pi) / degree_range)

def compute_distance(row):
    return sqrt(pow((row.y_end - row.y_begin), 2) + pow((row.x_end - row.x_begin), 2))

class PlayerData:

    def __init__(self, player_dataframe, degree_range=15):
        self.__player_dataframe = player_dataframe
        self.__degree_range = degree_range

    @property
    def passes(self):
        return self.__player_dataframe[["x_begin", "y_begin", "x_end", "y_end"]]

    @property
    def name(self):
        return self.__player_dataframe["player_name"].unique()[0]

    @property
    def id(self):
        return self.__player_dataframe["player_id"].unique()[0]

    @property
    def team_name(self):
        return self.__player_dataframe["team_name"].unique()[0]

    @property
    def team_id(self):
        return self.__player_dataframe["team_id"].unique()[0]
    
    @property
    def lineup_horizontal(self):
        return 0.6655 - self.__player_dataframe["lineup_horizontal"].unique()[0]/15.0 + 0.08

    @property
    def lineup_vertical(self):
        return self.__player_dataframe["lineup_vertical"].unique()[0]/18.0 + 0.1

    def __process_angles(self):
        player_angle = self.passes.copy()
        player_angle["angle"] = player_angle.apply(compute_angle, degree_range=self.__degree_range, axis=1)
        player_angle["distance"] = player_angle.apply(compute_distance, axis=1)
        player_angle = player_angle.groupby(["angle"]).agg(
            freq=pandas.NamedAgg(column='angle', aggfunc='count'), 
            distance=pandas.NamedAgg(column='distance', aggfunc='mean')
        ).reset_index()
        angles = [i for i in range(-180, 180 + self.__degree_range, self.__degree_range)]
        lacking_angles = [angle for angle in angles if angle not in list(player_angle.angle)]
        filled_data = {
            "angle": lacking_angles, 
            "freq": [0] * len(lacking_angles),
            "distance" : [0] * len(lacking_angles)
        }
        filled_dataframe = pandas.DataFrame.from_dict(filled_data)
        full_data = player_angle.append(filled_dataframe, ignore_index=True)
        full_data["angle_rad"] = -(full_data["angle"] * numpy.pi / 180) + numpy.pi/2
        full_data = full_data.sort_values(by="angle", ascending=False).reset_index(drop=True)
        return full_data

    @property
    def angles(self):
        return self.__process_angles()

def aggregate_data(data, degree_range):
    return [PlayerData(x, degree_range) for _, x in data.groupby(data["player_name"])]