# -*- coding: utf-8 -*-
"""
Created on March 26 2024
@author: cami-uche-enwe
Leiden University

requirements: MNE installed; psychofit installed

"""

#%% =============================== #
# import packages
# ================================= #

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
sns.set_style('darkgrid')
from pathlib import Path
import utils
from audio_extract import extract_audio
from tqdm import tqdm

# flexible paths
from utils_path import folder_path, figures_folder

#%% =============================== #
# get files and file contents
# ================================= #
figures_folder = os.path.join(os.getcwd(), 'figures') # to save

# loop over all subject folders
subjects = sorted(os.listdir(folder_path))
print(subjects)

#%% =============================== #
# preprocess and extract
# ================================= #

for subj in tqdm(subjects):
    # make the folders necessary
    if not os.path.exists(os.path.join(folder_path, subj, 'raw_behavior_data')):
        for f in ['raw_behavior_data', 'raw_video_data', 'raw_eyelink_data', 'alf']:
            os.mkdir(os.path.join(folder_path, subj, f))

        # move files to the correct folders
        for exts in ['csv', 'psydat', 'log']:
            file_names = [s for s in os.listdir(os.path.join(folder_path, subj)) if s.endswith('.' + exts) and not s.startswith('.')]
            for f in file_names:
                os.rename(os.path.join(folder_path, subj, f), os.path.join(folder_path, subj, 'raw_behavior_data', f))    
        for exts in ['asc', 'EDF']:
            file_names = [s for s in os.listdir(os.path.join(folder_path, subj)) if s.endswith('.' + exts) and not s.startswith('.')]
            for f in file_names:
                os.rename(os.path.join(folder_path, subj, f), os.path.join(folder_path, subj, 'raw_eyelink_data', f))
        for exts in ['mkv', 'wav']:
            file_names = [s for s in os.listdir(os.path.join(folder_path, subj)) if s.endswith('.' + exts) and not s.startswith('.')]
            for f in file_names:
                os.rename(os.path.join(folder_path, subj, f), os.path.join(folder_path, subj, 'raw_video_data', f))

#%% preprocess ALF behavior
for subj in tqdm(subjects):
    try:
        # extract psychopy file into usable trials df and session df
        behavior_file_name = [s for s in os.listdir(os.path.join(folder_path, subj, 'raw_behavior_data')) if s.endswith('.csv') and not s.startswith('.')]
        data = pd.read_csv(os.path.join(folder_path, subj, 'raw_behavior_data', behavior_file_name[0]))
        trials_df, session_df = utils.convert_psychopy_one(data, behavior_file_name[0])
        trials_df.to_csv(os.path.join(folder_path, subj, 'alf', 'trials_table.csv'))
        session_df.to_csv(os.path.join(folder_path, subj, 'alf', 'session_info.csv'))
    except Exception as e:
        print("skipped subject with error", subj, e)
        continue

#%% preprocess AUDIO AND VIDEO
for subj in tqdm(subjects):
    try:
        utils.process_audio(folder_path, subj) # TODO: make this save imcomplete detections rather than erroring out
    except Exception as e:
        print("skipped subject with error", subj, e)
    try:
        utils.process_video(folder_path, subj)
    except Exception as e:
        print("skipped subject with error", subj, e)
   

#%% =============================== #
# make snapshot figures
# ================================= #

for subj in subjects:

    # # BEHAVIORAL DATA FROM PSYCHOPY CSV FILE
    if not os.path.exists(os.path.join(figures_folder, subj + '_behavior_snapshot.png')):
        try:
            behavior_file_name = [s for s in os.listdir(os.path.join(folder_path, subj, 'alf')) if s.endswith('trials_table.csv') and not s.startswith('.')]
            data = pd.read_csv(os.path.join(folder_path, subj, 'alf', behavior_file_name[0]))
            utils.plot_snapshot_behavior(data, figures_folder, subj + '_behavior_snapshot.png')
        except Exception as e:
            print("skipped behavior snapshot, subject with error", subj, e)
    else:
        continue

#%% PUPIL DATA
for subj in subjects:
    # if not os.path.exists(os.path.join(figures_folder, subj + '_pupil_snapshot.png')):
    try:
        # EYETRACKING DATA FROM EYELINK ASC FILE
        pupil_file_name = [s for s in os.listdir(os.path.join(folder_path, subj, 'raw_eyelink_data')) if s.endswith('.asc')]
        utils.plot_snapshot_pupil(os.path.join(folder_path, subj, 'raw_eyelink_data', pupil_file_name[0]),
                                figures_folder, subj + '_pupil_snapshot.png')
    except Exception as e:
        print("skipped pupil snapshot, subject with error", subj, e)
    # else:
    #     continue
#%%
for subj in subjects:
    if not os.path.exists(os.path.join(figures_folder, subj + '_audio_snapshot.png')):
        try:
            utils.plot_snapshot_audio(os.path.join(folder_path, subj), 
                                      figures_folder, subj + '_audio_snapshot.png')
        
        except Exception as e:
            print("skipped subject with error", subj, e)
    else:
        continue

    if not os.path.exists(os.path.join(figures_folder, subj + '_video_snapshot.png')):
        try:
            utils.plot_snapshot_video(os.path.join(folder_path, subj), subj,
                                      figures_folder, subj + '_video_snapshot.png')
        
        except Exception as e:
            print("skipped subject with error", subj, e)
    else:
        continue
    
# %%
