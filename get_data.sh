#!/usr/bin/env bash
cd dataset
unzip driver_imgs_list.csv.zip
unzip imgs.zip
cp -r train train_valid
mkdir valid
cd ..
python reorg_data.py