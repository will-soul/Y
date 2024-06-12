from astropy.io import fits
fits_image_filename = r"D:\fits_download\fits_unzip\frame-r-000109-2-0188"  # 替换为你的文件路径
hdul = fits.open(fits_image_filename)
hdul.info()
image_data = fits.getdata(fits_image_filename, ext=0)
