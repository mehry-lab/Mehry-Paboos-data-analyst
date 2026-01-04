import pandas as pd
import numpy as np

db=pd.read_csv ("../outpatient_activity_cleaned.csv")
total=len(db)

completed=db["is_completed"].sum()
no_show = df["is_no_show"].sum()
cancelled = df["is_cancelled"].sum()

