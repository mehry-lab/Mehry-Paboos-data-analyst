import pandas as pd
import numpy as np

db=pd.read.csv("outpatient_activity.csv")
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



