import zipfile
import shutil
import os
from reorg_data import reorg_data


def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name, 'r')
    zip_file.extractall('./dataset/')
    zip_file.close()


if __name__ == '__main__':
    if not os.path.exists('./dataset'):
        os.mkdir('./dataset')
    un_zip('./driver_imgs_list.csv.zip')
    print('driver_imgs_list unzip finished.')
    un_zip('./imgs.zip')
    print('imgs unzip finished.')
    shutil.copytree('./dataset/train', './dataset/train_valid')
    os.mkdir('./dataset/valid')
    reorg_data(
        train_dir='./dataset/train',
        valid_dir='./dataset/valid',
        valid_ratio=0.1)
    print('All preprocess finished!')