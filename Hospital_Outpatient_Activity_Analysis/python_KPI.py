import pandas as pd
import numpy as np

db=pd.read_csv ("../outpatient_activity_cleaned.csv")
total=len(db)

Completed=db["is_completed"].sum(),
no_show=db["is_no_show"].sum(),
Cancelled=db["is_cancelled"].sum(),

no_show_rate = no_show / total
cancel_rate = cancelled / total
avg_wait=db.loc[db["is_completed"]==True, "wait


