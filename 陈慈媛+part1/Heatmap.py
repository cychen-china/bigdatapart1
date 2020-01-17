
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

plt.figure(figsize=(16,8))
m = Basemap()
m.drawcoastlines()

plt.show()
m.drawcountries(linewidth=1.5)
m = Basemap(llcrnrlon=73, llcrnrlat=18, urcrnrlon=135, urcrnrlat=53)
m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
m.readshapefile('CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)



ax = plt.gca()
for nshape, seg in enumerate(m.states):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

m.readshapefile('TWN_adm_shp/TWN_adm0', 'taiwan', drawbounds=True)
for nshape, seg in enumerate(m.taiwan):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)

for shapedict in m.states_info:
    statename = shapedict['NL_NAME_1']
    p = statename.split('|')
    if len(p) > 1:
        s = p[1]
    else:
        s = p[0]

for shapedict in m.taiwan_info:
    s = shapedict['NAME_CHINE']

df = pd.read_csv('chnpop.csv')
cmap = plt.cm.YlOrRd
colors[s] = cmap(np.sqrt((pop - vmin) / (vmax - vmin)))[:3]
color = rgb2hex(colors[statenames[nshape]])
poly = Polygon(seg, facecolor=color, edgecolor=color)