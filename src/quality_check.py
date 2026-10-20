import pandas as pd
def run_quality_checks(df):
    """check a datset for common data-quality issues."""
    quality_checks={
        "missing value":df.isnull().sum().sum(),
        "duplicate value":df.duplicated().sum(),
        "negative quantities":(df["Quantity"]<0).sum(),
        "invalid price":(df["UnitPrice"]<=0).sum()
    }
    quality_rows=[]
    for check, value in quality_checks.items():
        status="PASS" if value==0 else "REVIEW"
        quality_rows.append({"check":check,"issue count":int(value),"status":status})
    quality_report=pd.DataFrame(quality_rows)
    return quality_report

