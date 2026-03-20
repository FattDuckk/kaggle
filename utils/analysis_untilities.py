import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prints a data overview
def overview(data):
    print(f"No.Rows: {len(data)}")
    print(f"No.Columns: {len(data.columns)}")
    print("Columns: ")

    pad = max(len(col) for col in data.columns) + 2
    dtype_padding = max(len(str(dtype)) for dtype in data.dtypes) + 2
    uniques_padding = max(len(str(data[col].nunique())) for col in data.columns) + 10
    null_padding = max(len(str(data[col].isnull().sum())) for col in data.columns) + 8
    
    for col in data.columns:
        unique_str = f"({data[col].nunique()} Uniques)"
        nulls = data[col].isnull().sum()
        null_str   = f"({data[col].isnull().sum()} Nulls)"
        print(f"  - {col:<{pad}}  {unique_str:<{uniques_padding}} {null_str:<{null_padding}} {str(data[col].dtype):<{dtype_padding}} ")

def quick_eda(df, target=None):
    # Null heatmap
    sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
    plt.title("Nulls")
    plt.show()

    # Distributions for numeric cols
    df.hist(figsize=(12, 8), bins=20)
    plt.tight_layout()
    plt.show()

    # If target provided, show survival rate per categorical col
    if target:
        cat_cols = df.select_dtypes(include='object').columns
        for col in cat_cols:
            sns.barplot(x=col, y=target, data=df)
            plt.title(f"{target} by {col}")
            plt.show()
        