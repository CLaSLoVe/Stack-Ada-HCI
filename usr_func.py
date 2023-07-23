import sys
sys.path.append("..")
from utils.xy2aoi import assign_to_aoi


def process_eye_tracking_data(data):
    tag = 'aoi'
    data = list(map(float, data.decode().split(', ')))
    aoi, par = assign_to_aoi(data)
    return tag, par


def process_scene_parameter_data(data):
    tag = 'par'
    data = list(map(float, data.decode().split(', ')))
    return tag, dict(zip(par_namelist, data))


par_namelist = ['Panel1', 'Panel2', 'Panel3', 'Panel4', 'Panel5', 'Panel6']