import configparser
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


config = configparser.ConfigParser()
config.read('../aois.ini')


fig, ax = plt.subplots()
for section in config.sections():
    x = int(config.get(section, 'x'))
    y = int(config.get(section, 'y'))
    width = int(config.get(section, 'width'))
    height = int(config.get(section, 'height'))
    rect = Rectangle((x, y), width, height, facecolor='none', edgecolor='red')
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, section, ha='center', va='center')

ax.set_xlim(0, 800)
ax.set_ylim(0, 600)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('AOI Regions')

plt.show()