# coding: utf-8
from PIL import Image
import os
import numpy as np
import pandas as pd


def cnv_image(file_path):
    df = pd.read_csv('./csv/' + file_path)
    name, ext = os.path.splitext(file_path)
    # print(df.values[0][0])
    # print(df.info())
    # print(len(df))
    # print(len(df.columns))

    arr = np.arange(len(df) * len(df.columns) * 3).reshape(len(df), len(df.columns), 3)
    # print(arr)

    for x in range(len(df)):
        for y in range(len(df.columns)):
            s = df.values[x][y].split(',')
            arr[x][y][0] = s[0]
            arr[x][y][1] = s[1]
            arr[x][y][2] = s[2]

    # print(arr)
    # print(arr.dtype)
    # print(arr.ndim)
    # print(arr.shape)
    cast_arr = arr.astype(np.uint8)
    print(cast_arr.dtype)
    print(cast_arr.ndim)
    print(cast_arr.shape)
    pil_img = Image.fromarray(cast_arr)
    pil_img.save('pict/' + name + '.png')


path = 'csv'

for file in os.listdir(path):
    if not file.startswith('.'):
        print(file)
        cnv_image(file)
