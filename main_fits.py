# 引入库
import pandas as pd
import os.path
from urllib import request
# 文件路径
fits_save = r"C:\Users\Li\PycharmProjects\fits_label\fits3"
csv_load=r"C:\Users\Li\PycharmProjects\download_\data\csv\ryax.csv"  # 星体信息表
# 下载路径
url="https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/"
# 读csv，遍历星体表
data = pd.read_csv(csv_load)
data = data.astype(int)
for index, row in data.iterrows():
    # 每行信息填充
    run = row['run']
    camcol = row['camcol']
    field = row['field']
    cache=f"{run:06}-{camcol}-{field:04}"
    fits_url=url+f"{run}/{camcol}/frame-r-{cache}.fits.bz2"
    fits_path=os.path.join(fits_save,f"frame-r-{cache}.fits.bz2")
    # 下载fits
    print(f"\ndownload {cache} ",end='')
    if not os.path.exists(fits_path):
        file = open(fits_path, "wb")
        try:
            req = request.Request(fits_url)
            url_open = request.urlopen(req, timeout=60)
            fits = url_open.read()
            file.write(fits)
            print("fits...",end='')
        except Exception as e:
            print("\ntimeout:" + fits_url,end='')
        file.close()
