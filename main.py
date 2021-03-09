import matplotlib as matplotlib
import numpy as np
import os
import tinydb
import matplotlib.pyplot as plt

from musicnn.tagger import top_tags
# print(top_tags("D:\\itzst\\Documents\\Programming\\Python "
# "Projects\\Autocompiler\\venv\\musicnn\\audio\\TRWJAZW128F42760DD_test.mp3"))

from tinydb import TinyDB

from musicnn.extractor import extractor
taggram, tags = extractor(
    'D:\\itzst\\Documents\\Programming\\Python Projects\\Autocompiler\\venv\\musicnn\\audio\\SNES Battle Course 4 [Mario Kart Wii].mp3',
    model='MTT_musicnn', extract_features=False)
tags_likelihood_mean = np.mean(taggram, axis=0)  # averaging the Taggram through time

db = TinyDB(os.getcwd() + '/db.json')

# in_length = 3
# plt.rcParams["figure.figsize"] = (10,8)
# fontsize = 12

# fig, ax = plt.subplots()

# title
# ax.title.set_text('Tags likelihood (mean of the taggram)')
# ax.title.set_fontsize(fontsize)

# y-axis title
# ax.set_ylabel('(likelihood)', fontsize=fontsize)

# y-axis
# ax.set_ylim((0, 1))
# ax.tick_params(axis="y", labelsize=fontsize)

# x-axis
# ax.tick_params(axis="x", labelsize=fontsize-1)
# pos = np.arange(len(tags))
# ax.set_xticks(pos)
# ax.set_xticklabels(tags, rotation=90)

# depict song-level tags likelihood
# ax.bar(pos, tags_likelihood_mean)

topFiveValues = tags_likelihood_mean.argsort()[-5:][::-1]
loopcount = 0
for x in topFiveValues:
    print(str(tags[topFiveValues[loopcount]]) + ":" + str(tags_likelihood_mean[topFiveValues[loopcount]]))
    loopcount += 1


# plt.show()
