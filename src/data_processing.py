import numpy
import pandas
from math import atan2, sqrt

def compute_angle(row, degree_range):
    return - degree_range * round((atan2(row.y_end - row.y_begin, row.x_end - row.x_begin) * 180 / numpy.pi) / degree_range)

def compute_distance(row):
    return sqrt(pow((row.y_end - row.y_begin), 2) + pow((row.x_end - row.x_begin), 2))

def process_angles(data, degree_range):
    data["angle"] = data.apply(compute_angle, degree_range=degree_range, axis=1)
    data["distance"] = data.apply(compute_distance, axis=1)
    data = data.groupby(["angle"]).agg(
        freq=pandas.NamedAgg(column='angle', aggfunc='count'), 
        distance=pandas.NamedAgg(column='distance', aggfunc='mean')
    ).reset_index()
    angles = [i for i in range(-180, 180 + degree_range, degree_range)]
    lacking_angles = [angle for angle in angles if angle not in list(data.angle)]
    filled_data = {
        "angle": lacking_angles, 
        "freq": [0] * len(lacking_angles),
        "distance" : [0] * len(lacking_angles)
    }
    filled_dataframe = pandas.DataFrame.from_dict(filled_data)
    full_data = data.append(filled_dataframe, ignore_index=True)
    full_data["angle_rad"] = (full_data["angle"] * numpy.pi / 180) - numpy.pi/2
    full_data = full_data.sort_values(by="angle", ascending=True).reset_index(drop=True)
    return full_data
