import pandas as pd
import numpy as np

db=pd.read_csv("outpatient_activity.csv")
daTime=["scheduled_time", "arrival_time", "seen_time"]
for c in daTime
    db[c]=pd.to_datetime(db[c], errors="coerce")

db["wait_minutes_calc"]=(
    (db["seen_time"] - db["scheduled_time"]).dt.total_seconds() / 60
)
db["is_completed"] = db["outcome"].eq("Completed")
db["is_no_show"] = db["outcome"].eq("No-Show")
db["is_cancelled"] = db["outcome"].eq("Cancelled")

db.loc[~db["is_completed"], "wait_minutes_calc"] = np.nan
db["month"]=db["scheduled_time"].dt.to_period("M").astype(str)

DSummary={
    "Rows":len (db),
    "Completed": int(db["is_completed"].sum()),
    "Noshow": int (db["is_no_show"].sum()),
    "Cancelled": int(db["is_cancelled"].sum()),
    "Waitting": int(db["wait_minutes_calc"].isna().sum())
    }
print("Data Quality Summary:", DSummary)
db.to_csv("../outpatient_activity_cleaned.csv", index=False)
print("Saved: outpatient_activity_cleaned.csv")





    
