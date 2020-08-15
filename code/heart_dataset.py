import os
import pandas as pd
from aif360.datasets import StandardDataset
def default_preprocessing(df):
    cf=['slope_of_peak_exercise_st_segment', 'thal', 'chest_pain_type',
                         'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results', 'exercise_induced_angina']

    ftd = ['patient_id']
    all_other = [x for x in df.columns if x not in cf and x not in ftd] 

    df[all_other] = df[all_other].astype(float)

    return df

class HeartDiseaseDataset(StandardDataset):

    def __init__(self, label_name, favorable_classes,
                 protected_attribute_names,
                 privileged_classes,
                 instance_weights_name,
                 categorical_features,
                 features_to_keep, 
                 features_to_drop,
                 na_values, custom_preprocessing,
                 metadata):
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../data', 'heart_disease.csv')

        column_names = ['patient_id','slope_of_peak_exercise_st_segment', 'thal',
       'resting_blood_pressure', 'chest_pain_type', 'num_major_vessels',
       'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results',
       'serum_cholesterol_mg_per_dl', 'oldpeak_eq_st_depression', 'sex', 'age',
       'max_heart_rate_achieved', 'exercise_induced_angina','heart_disease_present']
        try:
            df = pd.read_csv(filepath, sep=',', names=column_names, header=0)
        except IOError as err:
            print("IOError: {}".format(err))
            print("Data file not found")
            print("\nand place them, as-is, in the folder:")
            import sys
            sys.exit(1)
            
        super(HeartDiseaseDataset, self).__init__(df=df, 
                                                label_name=label_name,
                                                favorable_classes=favorable_classes,
                                                protected_attribute_names=protected_attribute_names,
                                                privileged_classes=privileged_classes,
                                                instance_weights_name=instance_weights_name,
                                                categorical_features=categorical_features,
                                                features_to_keep=features_to_keep,
                                                features_to_drop=features_to_drop, 
                                                na_values=na_values,
                                                custom_preprocessing=default_preprocessing, 
                                                metadata=metadata)