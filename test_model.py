import pathlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from helpers.readlabels import readLabels
from helpers.model import *

MODEL = 'model10'

label_names = np.array(readLabels(MODEL))
model = readmodel(MODEL)
compile(model)

prediction_bar(model, label_names, './output.wav', 'down')

prediction_bar(model, label_names, audiodata=read_record(), name='down')