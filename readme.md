# AUTOMATED DATA QUALITY AUDITOR

## PROJECT OVERVIEW
A python-based project that inspect a datset,identifies potential data-quality issues, and generate reports and visualisations.

## DATASET
UCI online retail dataset

## TECHNOLOGIES USED
-Python
-Matplotlib
-Pandas
-Execel/CSV

## FEATURES 
-Dataset inspection
-Missing value detection
-Duplicate-row detection
-Negative value detection
-Invalid-price detection
-Automated data-quality reports
-Data-quality visualisation
-Export of a dataset without exact duplicate rows

## PROJECT OUTPUTS
-Cleaned dataset in CSV format
-Automated quality report 
-Missing-value report
-Data-quality charts

## HOW TO RUN
### 1. Install python
 Download and install python from the official website :
 https://www.python.org/downloads/

### 2.Download the project
 Clone the repository or download the project files from github.

### 3.Install required packages
 Open the terminal in the project folder and run:
 '''pip install -r requirement.txt '''

### 4.Run the project
 Run the following command in the terminal:
 '''python main.py'''

### 5.View the output
 After successfully execution,check these files:
 -'data/cleaned_online_retail.csv'
 -'reports/automated_quality_report.csv'
 -'reports/missing_values_report.csv'
 -'reports/data_quality_chart.png'

## FUTURE IMPROVEMENTS
-Add more data validation rules.
-Generate a more detailed HTML reports
-Improve error handling
