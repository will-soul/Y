import gc

import pandas as pd
import os
import requests
import urllib3
urllib3.disable_warnings()
#                                                                frame-irg-002888-1-0024-115.0982-20.82695
# https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/1411/1/frame-irg-001411-1-0091.jpg
# https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/2830/5/frame-r-002830-5-0144.fits.bz2
# https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/2830/5/frame-r-002830-5-0144.fits.bz2
# https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/2864/5/frame-r-002864-5-0201.fits.bz2
# 它首先从一个CSV文件中读取元数据，然后根据这些元数据构建下载URL和文件名，最后下载并保存文件。如果文件已经存在，则跳过下载



class Download_fits:
    def __init__(self, csv_path, save_path):
        self.url = "https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/"  # 应该是SDSS官网基础URL
        self.save_path = save_path   # 当地文件路径 本地要保存到的 G:\tushujv\tuwhite
        self.csv_path = csv_path    # 提前准备好的csv文件，csv_path = r"G:\tushujv\MyTable_8_zjcwhite.csv"
        self.band_list = "irg"     # （请提前标注要下载的波段） irg。

    def download(self):
60.69
        meta_data = pd.read_csv(self.csv_path)  # 读取提取准备好的csv文件内容为 meta_data里面是csv_path = r"G:\tushujv\MyTable_8_zjcwhite.csv"

        for index, row in meta_data.iterrows(): # 遍历csv每一行
            run = int(row['run'])
            camcol = int(row['camcol'])
            field = int(row['field'])
            RA=str(row["ra"])
            DEC=str(row["dec"])

            if not os.path.exists(os.path.join(self.save_path)): # 系统中没路径  要保存的路径
                os.mkdir(os.path.join(self.save_path)) #如果没有就创建

            try:
                    # url 根据 run camcol band 构建完整的下载URL
                    #  https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301  /1411/  1  /frame-irg-001411-  1  -0091.jpg
                    url = self.url + "%s/%s/frame-r-%s-%s-%s.jpg" % (
                        run, camcol, '{:0>6d}'.format(run), camcol, '{:0>4d}'.format(field))
                    # 构建fits文件名 其中某个波段 外循环一次 先下完一个波段  /frame-irg-001411-1-0091.jpg
                    fits_name = "frame-irg-%s-%s-%s-%s-%s.jpg" % (
                         '{:0>6d}'.format(run), camcol, '{:0>4d}'.format(field),RA,DEC)


                    # self.save_path, band, fits_name 这个是下载的fits文件全名
                    if not os.path.exists(os.path.join(self.save_path, "irg", fits_name)):
                        # 不存在的 则下载fits文件 并保存到指定路径
                        requests.packages.urllib3.disable_warnings()
                        r = requests.get(url, verify=False) # 下载内容
                        with open(os.path.join(self.save_path, "irg", fits_name), 'wb') as f:
                            f.write(r.content)
                        print("download %s success" % (fits_name))
                    else:
                        print("already done!")

            except Exception as e:
                print(e)
            finally:
                del index,row,run,camcol,field
                gc.collect()



# save_path 自己电脑上想把下载的文件保存在哪个地方，就改成对应文件夹的对绝对路径
save_path = r"C:\Users\Li\PycharmProjects\download_\irg"
# csv_path ：自己的那个csv文件下载在哪里，就吧下面改成对应csv的绝对路径就行
csv_path = r"C:\Users\Li\PycharmProjects\download_\data\csv\ryax.csv"
opt = Download_fits(csv_path, save_path)
opt.download()
