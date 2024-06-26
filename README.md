# This code is for the Human IBL decision-making task
- Task code at https://github.com/cami-uche-enwe/human_IBL_cursor
- Instructions [here](https://docs.google.com/document/d/1C6Kt_tYg0wLJQ1GE0N0mQVeitvk-i0vjs0vuYjYIJsQ/edit)

# What the code does
This code helps to retrieve the data that is saved on git lab via Pavlovia _OR_ local files that were collected using PsychoPy

- The experiment that the data is taken from can be found here: https://gitlab.pavlovia.org/Anninas/human_ibl_piloting. For more information about the experiment you can look at it's README file https://gitlab.pavlovia.org/Anninas/human_ibl_piloting/blob/master/readme.md 
- The code plots three plots for each of the participant that took the experiment and saves it in the behavioral_snapshot_figures folder
- The first plot shows the signed contrast on the x-axis and the percentage of right choices ("m") for that specific contrast on the y-axis.
- The second plot shows the signed contrast on the x-axis and the corresponding reaction time in seconds on the y axis 
- The third plot show the trail number on the x-axis and the corresponding RT in seconds on the y-axis

# How to use the code for online experiment data
- Download `behavioral_snapshots.py`
- Install [brainbox](https://github.com/int-brain-lab/ibllib) for psychometric function fitting

# How to use the code for offline experiment data
- Download `offline_behavioural_snapshots.py`
- Edit the `folder_path` in the file to match the path corresponding to your own data folder
- Install [brainbox](https://github.com/int-brain-lab/ibllib) for psychometric function fitting

By Anne Urai, Leiden University, 2022
a.e.urai@fsw.leidenuniv.nl

