import os
import sys
import glob
from PIL import Image, ImageStat

transparency = 0.35

work_dir = sys.argv[1:]

for sub_dir in work_dir:
    print('Processing: '+sub_dir)
    os.chdir(sub_dir)
    if os.path.isdir('./Merged') is False:
        os.mkdir('./Merged')
    files = glob.glob('*.tif')
    files.sort()
    i = 0
    while i <= len(files) - 2:
        file1 = Image.open(files[i])
        file2 = Image.open(files[i+1])
        mean_pix1 = ImageStat.Stat(file1).mean
        mean_pix2 = ImageStat.Stat(file2).mean

        if mean_pix1[0] > mean_pix2[0]:
            file1 = Image.blend(file2, file1, transparency)
        
        else:
            file1 = Image.blend(file1, file2, transparency)
        os.chdir('./Merged')
        file1.save(files[i].split()[0]+'_'+files[i+1].split()[0]+'_'+'merged'+'.tif', compession='tiff_lzw')
        os.chdir(sub_dir)
        file1.close()
        file2.close()
        i += 2

