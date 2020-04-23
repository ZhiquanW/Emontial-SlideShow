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
    def __init__(self, name: str, image: np.array, valence: float, arousal: float, intensity: float, dominant_color: np.array):
        self.name = name
        self.image = image
        self.valence = valence
        self.arousal = arousal
        self.intensity = intensity
        self.dominant_color = dominant_color
