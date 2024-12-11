# is507-fall2024-tastedata
Supplementary git repository for project reproduce.

## Overview
- Purpose: is507-fall2024-tastedata is Github repository for the final project of IS 507 by group Taste the data. The project is about processing red wine dataset to create an reliable wine quality evaluator.

- Dataset: The Wine Quality dataset consists of 2 CSV files, one for red wine and another for white wine. Cortez et al. (2009) mentioned that the wine data are from the product of Vinho Verde, a product from the Minho (north-west) region of Portugal. Our group used red wine dataset that consist of 1599 samples with 11 features and 1 target variable. 11 features: fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, and alcohol are the physicochemical properties measured for each samples, which all 11 features are numerical and continuous variable. 1 target variable is quality, which indicate wine quality score scaled between 0 to 10, ordinal numbers. According to the Pandas .info() command, all 11 features and 1 target variable showed no missing-value.

- Analysis: Conducted regression task on the red wine dataset, using LASSO Regression, Ridge Regression, Decision Tree, and Random Forest. Preprocessing applied for scaling continuous 11 features, and applied GridsearchCV to go over parameters and 10 Cross-validation.

## Process of reproducing the project
1. Please clone this repository.
2. Then please run data_preparation.py file using python3 "script/data_preparation.py" command on your terminal that located in cloned repository. This will download and check the Wine quality dataset at the data folder under this repository.
3. Now you can check the overall codes at is507_project.ipynb file. The ipynb file located under script folder.