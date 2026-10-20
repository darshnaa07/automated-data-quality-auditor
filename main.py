import pandas as pd
from src.quality_check import run_quality_checks
from pathlib import Path
#loading data
file_path=Path("data/online+retail/Online Retail.xlsx")
try:
    df=pd.read_excel(file_path)
    print("dataset loaded successfully")
except FileNotFoundError:
    print("error:excel file not found.please check the filepath")
except Exception as e:
    print(f"error loading dataset:{e}")
quality_report=run_quality_checks(df)
print(quality_report)
#data overview
print(df.head())
#printing column name
print(df.columns)
#finding any missing value
print(df.isnull().sum())
#finding duplicate value if any
print(df.duplicated().sum())
#dataset shape 
print(df.shape)
df.info()
#statistical summary
print(df.describe())
#data types
print(df.dtypes)
#unique values
print(df.nunique())
#checking negative quantities
negative_quantity=(df["Quantity"]<0).sum()
print("\nNegative quantities:",negative_quantity)
#check for invalid prices
invalid_price=(df["UnitPrice"]<=0).sum()
print("\nInvalid price:", invalid_price)
#count unique costumer
print("\nUnique customer:", df["CustomerID"].nunique())

#create a data quality report

report={"total rows":len(df),
        "total columns":len(df.columns),
        "missing values":df.isnull().sum().sum(),
        "duplicate row":df.duplicated().sum(),
        "negative quantities":(df["Quantity"]<0).sum(),
        "invalid price":(df["UnitPrice"]<=0).sum(),
        "unique customer":df["CustomerID"].nunique()}

print("\n---DATA QUALITY REPORT---")

for check,result in report.items():
    print(f"{check}:{result}")

#convert report dictionary into a dataframe
report_df=pd.DataFrame(list(report.items()),columns=["check","result"])

#save report as a csv file
report_df.to_csv("reports/data_quality_report.csv",index=False)
print("\nReport saved successfully!")

#detailed missing value report
missing_report=pd.DataFrame({"missing count":df.isnull().sum(),"missing percentage":(df.isnull().mean()*100).round(2)})
missing_report=missing_report[missing_report["missing count"]>0]
print("/n---missing value report---")
print(missing_report)

#detect duplicate rows
duplicate_count=df.duplicated().sum()
print("\n---DUPLICATED ROWS REPORT---")
print("total duplicate rows:",duplicate_count)

#create a dataset without exact duplicate rows
df_cleaned=df.drop_duplicates()
print("rows before cleaning:",len(df))
print("rows after cleaning:",len(df_cleaned))
print("rows removed:",len(df)-len(df_cleaned))

#save cleaned dataset
df_cleaned.to_csv("data/cleaned_retail.csv",index=False)
print("\n cleaned datset saved successfully!")

#automated data quality check
quality_checks={"missing value":df_cleaned.isnull().sum().sum(),
                "duplicate rows":df_cleaned.duplicated().sum(),
                "negative quantities":(df_cleaned["Quantity"]<0).sum(),
                "invalid prices":(df_cleaned["UnitPrice"]<=0).sum()}
print("\n---automated quality check---")
for check, value in quality_checks.items():
    if value==0:
        status="PASS"
    else:
        status="REVIEW"
    print(f"{check}:{value}|status:{status}")

#loop through each quality check
quality_rows=[]
for check, value in quality_checks.items():
    if value==0:
        status="PASS"
    else:
        status="REVIEW"
    quality_rows.append({"check":check,"issue count":value,"status":status})

#convert quality check into a dataframe
quality_report=pd.DataFrame(quality_rows)

#save the report
quality_report.to_csv("reports/automated_quality_report.csv",index=False)
print("quality report saved successfully!")

import matplotlib.pyplot as plt
#create a bar chart of data quality issues
plt.figure(figsize=(10,5))
plt.bar(quality_checks.keys(),quality_checks.values())
plt.title("data quality issue report")
plt.xlabel("quality checks")
plt.ylabel("number of issues")
plt.xticks(rotation=20)
plt.tight_layout()

#save the chart
plt.savefig("reports/data_quality_chart.png")
plt.show()
print("data quality chart saved successfully!")

#test the auditor with sample data
test_data= pd.DataFrame({
    "Quantity":[10,-2,5,3],
    "UnitPrice":[100,50,0,25],
    "customerID":[101,102,None,104]
})
print("\n---testing with sample data---")
test_report=run_quality_checks(test_data)
print(test_report)






