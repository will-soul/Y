import pandas as pd
from astropy.wcs import WCS
from astropy.io import fits
# 读取 CSV 文件
data = pd.read_csv('ryax2.csv')
# 假设你的 CSV 文件中的列名分别为 'RA' 和 'DEC'
ra_data = data['RA'].values
dec_data = data['DEc'].values
rad = data['petroRad_r'].values
run = data['run']
camcol = data['camcol']
field = data['field']
# 加载 WCS 信息，这通常来自一个 FITS 文件的头部信息
# 假设你有一个 FITS 文件，其中包含了 WCS 信息
header = fits.getheader(r'D:\DATA\data_unzip\frame-r-001140-6-0269.fits')
wcs = WCS(header)
# 将世界坐标转换为像素坐标
x, y = wcs.all_world2pix(ra_data, dec_data, 0)
# 输出转换后的像素坐标
print("Pixel X coordinates:", x)
print("Pixel Y coordinates:", y)
x = x / 2048
y = (1489-y) / 1489
r = 2.0 * rad / 0.396127 # 彼得罗森半径与像素单位换算
l = 2 * r / 2048
h = 2 * r / 1489
Class = 0
print(x,y,r,l,h)

# data = data.astype(int)
# yolo_data= f"{Class} {x} {y} {l} {h}\n"
# cache = f"{run:06}-{camcol}-{field:04}"
# filename = f'frame-r-{cache}.txt'
#
# with open(filename, 'w', encoding='utf-8') as f:
#     f.write(yolo_data)
# if not os.path.exists(filename):
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(yolo_data)
# else:
#     lable_file = open(filename)
#     lines = lable_file.readlines()
#     is_labeled = 0
#     for line in lines:
#         if line == yolo_data: # 重复的标注
#             is_labeled=1
#             break
#     if is_labeled == 0:
#         with open(filename, 'a') as f:
#             f.write(yolo_data)
