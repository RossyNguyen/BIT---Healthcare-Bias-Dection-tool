# TODO - change the next line to resemble this format:
# from <name of your data class file> import <name of the class inside that file>
from heart_disease.heart_dataset import HeartDiseaseDataset


import pandas as pd
import numpy as np

# TODO - change the name of the function accordingly
def load_preproc_data_heart(protected_attributes):
    """
    Load and pre-process dataset.
    Args:
        protected_attributes(list or None): If None use all possible protected
            attributes, else subset the protected attributes to the list.
    Returns:
        <Your> Dataset: An instance of Dataset with required pre-processing.
    """

    def custom_preprocessing(df):
        """ Custom pre-processing for Dataset"""
        # TODO - Here you can include any preprocessing necessary for your data.
        # This is not mandatory
        
        return df


    # Feature partitions
    # TODO - fill these in. For help see the guide and example below
    # TODO - after you fill it on, comment out or remove the example block
    D_features = []
    XD_features = []
    Y_features = []
    X_features = list(set(XD_features)-set(D_features))
    categorical_features = []
    features_to_drop = []


    # Guide
    # D_features (list): protected attribute names (names of attributes you think your model migh have a bias on)
    # XD_features (list): Combination of X, and D features (all features except the target feature)
    # X_features (list): feature names for input data
    # Y_features (list): feature names for binary label
    
    print(protected_attributes)
    # Example ------------------------!
    D_features = ['ethnicity'] if protected_attributes is None else protected_attributes
    XD_features = ['patient_id','ethnicity', 'sex', 'age', 'slope_of_peak_exercise_st_segment', 'thal',
                   'resting_blood_pressure', 'chest_pain_type', 'num_major_vessels',
                   'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results',
                   'serum_cholesterol_mg_per_dl', 'oldpeak_eq_st_depression',
                   'max_heart_rate_achieved', 'exercise_induced_angina']
    Y_features = ['heart_disease_present']
    features_to_drop = ['patient_id']
    X_features = list(set(XD_features)-set(features_to_drop))
    categorical_features = ['slope_of_peak_exercise_st_segment', 'thal', 'chest_pain_type',
                     'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results', 'exercise_induced_angina']
    
    # End example ------------------------!

    # protected attribute maps
    # TODO - fill this in and remove example lines
    all_protected_attribute_maps = {}
    print(X_features)
    label_map = {}
    #example
    all_protected_attribute_maps = {"sex": {1.0: 'Male', 0.0: 'Female'},
                                    "ethnicity":{1.0:'caucasian',2.0:'latin american',3.0:'east asian', 4.0:'south asian', 5.0:'arabic', 6.0:'african'}}
    
    label_map = {1.0: 'Heart Disease', 0.0: 'No Heart Disease'}
    #------------------------!

    # privileged classes
    # TODO - fill this in and remove example line
    all_privileged_classes = {}
    #example
    all_privileged_classes = {"ethnicity": [1.0]}
    #------------------------!
    print('feature_to_keep {}'.format(X_features+Y_features+D_features))
    # TODO - change from "HeartDiseaseDataset" to the name of your own dataset from the Data class file
    return HeartDiseaseDataset(
        label_name=Y_features[0],
        favorable_classes=[0],
        protected_attribute_names=D_features,
        privileged_classes=[all_privileged_classes[x] for x in D_features],
        instance_weights_name=None,
        categorical_features=categorical_features,
        features_to_keep=X_features+Y_features+D_features,
        features_to_drop=features_to_drop,
        na_values=[],
        metadata={ 'label_maps': [label_map],
                   'protected_attribute_maps': [all_protected_attribute_maps[x]
                                for x in D_features]},
        custom_preprocessing=custom_preprocessing)


def main():
    protected_attribute = 'ethnicity'
    dataset_orig = load_preproc_data_heart([protected_attribute])
    #print(dataset_orig)

if __name__ == '__main__':
    main()