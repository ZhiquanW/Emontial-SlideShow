#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zhiquan Wang'
__copyright__ = 'Copyright 2020, Zhiquan wang'
__maintainer__ = 'Zhiquan Wang'
__email__ = 'wang4490@purdue.edu'
__status__ = 'development'
__laboratory__ = 'vrlab-purdue'
__date__ = '2020/04/23- ‏‎00:53:30 PM'
from typing import List
import numpy as np


class Slide(object):
    def __init__(self, id: int, name: str, image: np.array, valence: float, arousal: float, intensity: float, dominant_color: np.array):
        self.id = id
        self.name = name
        self.image = image
        self.valence = valence
        self.arousal = arousal
        self.intensity = intensity
        self.dominant_color = dominant_color


class TargetCurves(object):
    def __init__(self, info_mat: List):
        print(len(info_mat))
        self.straight = info_mat[0]
        self.straight_curve_down = info_mat[1]
        self.straight_curve_hill = info_mat[2]
        self.straight_curve_up = info_mat[3]
        self.straight_u_shape = info_mat[4]
        self.straight_down = info_mat[5]

        self.straight_up = info_mat[6]

# def cal_total_cost(slide_show:List,target_values:dict):
#     valence_cost = 0
#     value_mat = [[slide.valence, slide.arousal] for slide in slide_show]
#     print(value_mat)
