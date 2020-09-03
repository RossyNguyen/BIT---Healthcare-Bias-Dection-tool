# Bias Identification Tool (B.I.T)
## Overview 
>This project aims to build a bias identification tool for clinical recommendation from doctors and healthcare providers. This usecase focus on the general practisioners's recommendation and users of this tool includes central healthcare organisation like NHS, the patient union and other organisation that is responsible for delivering social welfare schemes. Using historical health data, B.I.T goal is to identify conscious and unconscious bias that are inherent in a doctor recommendation, given all the patient and disease features provided. In UK on average a general practitioner is responsible for providing health care service to approximately 2087 people who come from a particular geographical location. The patients belongs to different ethnicity, gender, drug addiction history, age, languages, economic status etc. The goal of the tool is to identify any bias in their recommendation which would influence the quality of treatment provided to the patient e.g. patient time,recommended diagnostic checkup, medication, medical advice etc. The tool is used by doctors or general practisioners to aid their decision making process. 

To develop the tool we have to rely on publicly available data, but it is unavailable. Though [archive data](http://webarchive.nationalarchives.gov.uk) is available in the UK government website , only data description is available. The data is not public available at the moment, so require help to access real data. To proceed further we had to rely on mock data. An example of [heart-disease dataset](https://www.kaggle.com/johnsmith88/heart-disease-dataset) is used in this project to develop the tool. An additional feature called ethnicity is added to original data as the protected attribute.

## Work Flow
<img src="documents/images/call_for_code_flowchart_2020.jpg" width="500" height="500" style="width:500px;height:500px;margin-left:200px;margin-top:-50px"/>

>The workflow diagram provides details about how the tools will be used to identify the bias in a doctor recommendation for a particular ailment. The tool would be used as an extended feature within an existing health care system which is already used by doctors to audit their recommendation to their patients. Whenever a doctor fill in his/her patient's recommendations into the health system, the tool would inform the doctor if the recommendations provided has any bias. If a bias is detected, the tools request the doctor to justify his recommendations using a questioners. The questionnaire would be auto-generated based on unbiased historical data for the particular ailment for which recommendation was provided. Based on the justification score the recommendation are accepted with suggestions to reduce the bias in his earlier recommendation. Before justification the doctor can revise his recommendation to bring down the bias. This can be done by requesting further information from the patient, tests, training etc. If the doctor has to justify his recommendation several times, his future recommendation would be peer reviewed for bias. If this behaviour continues, it would be upto the concerned administration to look into the issue and rectify. The doctor is allowed to share his recommendation to the patient even if it has bias.

## Architecture 
<img src="documents/images/call_for_code_architecture_2020.jpg" 
style="width:500px;height:500px;margin-left:200px;margin-right:auto"/>

>The bias identification tool (BIT) will be part of an existing health system, which is used by GPs to log their clinical recommendations. The historical data of this system will be used by the BIT to identify the bias in the new recommendation. If a bias is detected, BIT would use Watson Assistant to build a questionnaire based on the new recommendation and historical data. The BIT ui would provide the user with the results of the bias analysis and any further interaction with the user based on his clinical recommendations. The BIT analysis component would be responsible for identifying the bias based on historical data. It's also responsible for analysing the questionnaire answer and handle user interaction accordingly. The BIT analysis component would be responsible for utilising the watson services and health data to provide bias identification service.

## Implementation

>The BIT would have a UI component, Analysis component and Service component. 

<h4>UI</h4>

>The UI component of BIT would be developed using reactjs. The UI would be used to provide the BIT analysis result when a new clinical recommendation is made by the user along with other analysis in relations to new recommendation. The UI will also manage the bias rectification process which involves justification, peer review and other recommended process by the domain experts.

<h4>Analysis</h4>

>The analysis component of BIT would be developed using python or spring boot and would be available to UI component as service. The component would be responsible for using the watson services to provide data modelling and nlp related functionality in BIT. To achieve this the watson service require data from the health system, which the BIT would provide.

Checking the repository
