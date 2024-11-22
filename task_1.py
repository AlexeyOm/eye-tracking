import statsmodels.formula.api as sm
import pandas as pd
def duration_vs_age(fixations_df, participants_df):
    '''
    Returns the parameters of the model, trained on the provided dataset
    Modeling the fixation duration vs age, grouped by years, with mean as aggregator
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

    # convert column names to lowercase
    df.columns = df.columns.str.lower()

    # dropping default year 2000 from dataset
    df = df[(df['age'] != 23)]

    # grouping by age and multiplying duration to get the value in miliseconds
    grouped_df = df.groupby('age').agg({'duration': 'mean'}).reset_index()
    grouped_df['duration'] = grouped_df['duration'] * 1000

    model = sm.glm('duration ~ age + I(age**2) ', data=grouped_df).fit()

    return model