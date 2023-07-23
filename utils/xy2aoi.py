import configparser
import os


# 读取aois.ini文件
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '../config/aois.ini')
config.read(config_path)

# 将AOI的坐标转换为字典
aoi_dict = {}
for section in config.sections():
    x = int(config.get(section, 'x'))
    y = int(config.get(section, 'y'))
    width = int(config.get(section, 'width'))
    height = int(config.get(section, 'height'))
    par = config.get(section, 'panels').split(', ')
    aoi_dict[section] = (x, y, width, height, par)


def assign_to_aoi(xy):
    x, y = xy
    for section, (aoi_x, aoi_y, aoi_width, aoi_height, panels) in aoi_dict.items():
        if x >= aoi_x and x <= aoi_x + aoi_width and y >= aoi_y and y <= aoi_y + aoi_height:
            return section, panels
    return None, None


if __name__ == '__main__':
    # 测试
    x = 200
    y = 200
    aoi, par = assign_to_aoi((x, y))
    if aoi:
        print(f"The point ({x}, {y}) is assigned to {aoi}. Related panel: {par}")
    else:
        print(f"No AOI found for the point ({x}, {y}).")