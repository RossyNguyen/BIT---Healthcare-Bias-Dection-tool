from heart_dataset import HeartDiseaseDataset
import pandas as pd
import numpy as np

def load_preproc_data_heart(protected_attributes):
    """
    Load and pre-process dataset.
    Args:
        protected_attributes(list or None): If None use all possible protected
            attributes, else subset the protected attributes to the list.
    Returns:
        Dataset: An instance of Dataset with required pre-processing.
    """

    def custom_preprocessing(df):
        """ Custom pre-processing for Dataset"""
      
    # Feature partitions
   
    # D_features (list): protected attribute names (names of attributes you think your model migh have a bias on)
    # XD_features (list): Combination of X, and D features (all features except the target feature)
    # X_features (list): feature names for input data
    # Y_features (list): feature names for binary label

    D_features = ['sex'] if protected_attributes is None else protected_attributes
    XD_features = ['patient_id', 'slope_of_peak_exercise_st_segment', 'thal',
                   'resting_blood_pressure', 'chest_pain_type', 'num_major_vessels',
                   'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results',
                   'serum_cholesterol_mg_per_dl', 'oldpeak_eq_st_depression', 'sex', 'age',
                   'max_heart_rate_achieved', 'exercise_induced_angina']
    Y_features = ['heart_disease_present']
    X_features = list(set(XD_features)-set(D_features))
    categorical_features = ['slope_of_peak_exercise_st_segment', 'thal', 'chest_pain_type',
                     'fasting_blood_sugar_gt_120_mg_per_dl', 'resting_ekg_results', 'exercise_induced_angina']
    features_to_drop = ['patient_id']

    all_protected_attribute_maps = {"sex": {1.0: 'Male', 0.0: 'Female'}}
    label_map = {1.0: 'Heart Disease', 0.0: 'No Heart Disease'}
    all_privileged_classes = {"sex": [1.0]}
   
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

