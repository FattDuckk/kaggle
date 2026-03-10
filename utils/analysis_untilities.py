import pandas as pd

def overview(data):
    print(f"No.Rows: {len(data)}")
    print(f"No.Columns: {len(data.columns)}")
    print("Columns: ")

    pad = max(len(col) for col in data.columns) + 2
    dtype_padding = max(len(str(dtype)) for dtype in data.dtypes) + 2
    uniques_padding = max(len(str(data[col].nunique())) for col in data.columns) + 10
    
    for col in data.columns:
        unique_str = f"({data[col].nunique()} Uniques)"
        nulls = data[col].isnull().sum()
        print(f"  - {col:<{pad}}  {unique_str:<{uniques_padding}} ({nulls} nulls)  {str(data[col].dtype):<{dtype_padding}} ")