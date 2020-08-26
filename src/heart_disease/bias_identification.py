'''
Created on 23 Aug 2020

@author: abrahamj
'''
import numpy as np
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from heart_disease.heart_dataset import HeartDiseaseDataset
from heart_disease.data_preproc_functions import load_preproc_data_heart
from IPython.core.display import Markdown, display
from sklearn.ensemble._forest import RandomForestClassifier


class BiasIdentification:
    def identifyBias(self, dataset:HeartDiseaseDataset):
        pass


def main():
    print('Calculate bias')
    np.random.seed(1)
    protected_attribute = 'ethnicity'
    dataset = load_preproc_data_heart([protected_attribute])
    
    privileged_groups = [{protected_attribute:1}]
    unprivileged_groups = [{protected_attribute:2}, {protected_attribute:3}, {protected_attribute:4}, {protected_attribute:5},{protected_attribute:6}]
    
    data_orig_train, data_orig_vt = dataset.split([0.7], shuffle=True)
    data_orig_valid, data_orig_test = data_orig_vt.split([0.5], shuffle=True)
    
    metric_orig_train = BinaryLabelDatasetMetric(data_orig_train,
                                                unprivileged_groups=unprivileged_groups,
                                                privileged_groups=privileged_groups
                                                 )
    print("Mean {}".format(metric_orig_train.mean_difference()))
    
    rw = Reweighing(unprivileged_groups = unprivileged_groups, privileged_groups=privileged_groups)
    data_transf_train = rw.fit_transform(data_orig_train)
    metric_transf_train = BinaryLabelDatasetMetric(data_transf_train, unprivileged_groups=unprivileged_groups, privileged_groups = privileged_groups)
    
    print("Mean difference after transformation =%f " % metric_transf_train.mean_difference())
   
    calculate_bias_measures(data_orig_train, data_orig_vt, unprivileged_groups, privileged_groups)
    calculate_bias_measures(data_orig_valid, data_orig_test, unprivileged_groups, privileged_groups)

def calculate_bias_measures(data_orig_train, data_orig_vt, unprivileged_groups, privileged_groups):
    model = RandomForestClassifier().fit(data_orig_train.features, data_orig_train.labels.ravel(), sample_weight=data_orig_train.instance_weights)
    dataset = data_orig_vt
    dataset_pred = dataset.copy()
    dataset_pred.labels = model.predict(data_orig_vt.features)
    classified_metric_race = ClassificationMetric(dataset, dataset_pred,
                                                  unprivileged_groups=unprivileged_groups,
                                                  privileged_groups=privileged_groups
                                                  )
    metric_pred_race = BinaryLabelDatasetMetric(dataset_pred,
                                                unprivileged_groups=unprivileged_groups,
                                                  privileged_groups=privileged_groups
                                                 )
    print("Mean difference {}".format(metric_pred_race.mean_difference()))
    print("Disparate Metric {}".format(metric_pred_race.disparate_impact()))
    print("Equal Opportunity Difference {}".format(classified_metric_race.equal_opportunity_difference()))
    print("Average Abs Odds Difference {}".format(classified_metric_race.average_abs_odds_difference()))
    print("Theil index {}".format(classified_metric_race.theil_index()))
    
if __name__ == '__main__':
    main()