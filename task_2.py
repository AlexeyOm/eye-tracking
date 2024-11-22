import statsmodels.formula.api as sm
import pandas as pd

def duration_vs_onset(fixations_df, participants_df):
    '''
    Returns the parameters of the model, trained on the provided dataset
    Modeling fixation duration vs the onset time of the fixation
    input:
    fixations_df - url or path to the csv with fixations data
    participants_df - url or path to the csv with participants info
    output:
    glm model
    the coefs and p's you can get by result.params and result.pvalues
    '''

    compiled_fixations_df = pd.read_csv(fixations_df)
    participant_info_df = pd.read_csv(participants_df)

    merged_df = pd.merge(compiled_fixations_df, participant_info_df, on='ID')

    # replace date of birth with age
    merged_df['age'] = 2023 - merged_df['DoB']

    # leaving only valid viewers
    merged_df = merged_df[(merged_df['Valid'] == True) & (merged_df['Valid Freeviewing'] == True)]

    # drop irrelevant columns
    df = merged_df[['ID', 'Gender', 'age', 'Order', 'duration', 'onset']]

    # cutting the tail because of the experiment design does not care for the last fixations
    df = df[df['onset'] < 8]

    # convert column names to lowercase
    df.columns = df.columns.str.lower()

    # dropping default year 2000 from dataset
    df = df[(df['age'] != 23)]


    # grouping the data into 50 bins and taking the average for each of the bins
    df['onset_bin'] = pd.cut(df['onset'], bins=50)

    # Group by the bins and calculate the median duration for each group
    median_durations = df.groupby('onset_bin', observed=False)['duration'].mean()

    # Reset the index for a cleaner output
    median_durations = median_durations.reset_index()

    median_durations['right'] = median_durations['onset_bin'].apply(lambda interval: interval.right)

    median_durations['right'] = median_durations['right'].astype(str).astype(float)

    #median_durations = median_durations[median_durations['right']<8]

    model_bins = sm.glm('duration ~ right + I(right**2)', data=median_durations).fit()

    return model_bins
