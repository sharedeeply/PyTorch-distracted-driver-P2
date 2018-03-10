# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""
import os

from PIL import Image


class TestSet(object):
    def __init__(self, test_dir, test_transform):
        self.test_dir = test_dir
        self.test_transform = test_transform
        self.test_img_list = os.listdir(test_dir)

    def __getitem__(self, item):
        test_img_name = self.test_img_list[item]
        test_img = Image.open(os.path.join(self.test_dir, test_img_name))
        test_img = self.test_transform(test_img)
        return test_img, test_img_name

    def __len__(self):
        return len(self.test_img_list)
