# Preprocessing data for additional participants

1. Open the https://osf.io/sk4fr/ in browser
2. Select nemo_eyetracking and click **Download as zip** button 
3. Extract everything to the root of your project folder
4. Open the **data** folder, steps up to 9th are done there
5. Delete the contents of **pre_processed** folder
6. Extract the contents of the zip files in **fixation_events** and **meaning_maps** into the root of the respective folders
7. Save **participant_info.csv** from https://osf.io/npmzd to the root of **data/pre_processed folder**
8. Download **pre_processed_updated.zip** from https://osf.io/ahu83
9. Extract **csv** files to the root of **pre_processed** folder
10. Change all 3 occurences of **median_absolute_deviation** to **median_abs_deviation** in **utils/dataloader_helpers.py**
11. Install dependencies from **requirements.txt**
12. Run **src/main.py**
