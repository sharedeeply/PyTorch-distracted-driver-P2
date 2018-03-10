# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""
import numpy as np
import pandas as pd
import torch.nn.functional as F
from torch.autograd import Variable


def predict_result(model, test_data, use_gpu):
    img_id = list()
    prob_result = list()
    model.eval()
    for data in test_data:
        img, img_name = data
        if use_gpu:
            img = img.cuda()
        img = Variable(img, volatile=True)
        score = F.softmax(model(img), dim=1)
        img_id.extend(img_name)
        prob_result.extend([i.numpy() for i in score.cpu().data])
    prob_result = np.array(prob_result)
    img_id = np.array(img_id)[:, None]
    all_data = np.concatenate((img_id, prob_result), axis=1)
    submission = pd.DataFrame(all_data)
    return submission
