import pandas as pd
import numpy as np

db=pd.read_csv ("../outpatient_activity_cleaned.csv")
total=len(db)

Completed=db["is_completed"].sum()
no_show=db["is_no_show"].sum()
Cancelled=db["is_cancelled"].sum()

no_show_rate = no_show / total
cancel_rate = cancelled / total
avg_wait=db.loc[db["is_completed"]==True, "wait_minutes_calc"].mean()

print(f"Total booked visits: {total}")
print(f"Completed: {completed}")
print(f"No-shows: {no_show} ({no_show_rate:.2%})")
print(f"Cancelled: {cancelled} ({cancel_rate:.2%})")
print(f"Average wait: {avg_wait:.1f} minutes")

kpi_by_specialty = (
    db.groupby("specialty")
      .agg(
          booked=("visit_id", "count"),
          completed=("is_completed", "sum"),
          no_show=("is_no_show", "sum"),
          cancelled=("is_cancelled", "sum"),
          avg_wait=("wait_minutes_calc", "mean")
      )
      .reset_index()
)

kpi_by_specialty["no_show_rate"] = kpi_by_specialty["no_show"] / kpi_by_specialty["booked"]
kpi_by_specialty["cancel_rate"] = kpi_by_specialty["cancelled"] / kpi_by_specialty["booked"]

kpi_by_specialty = kpi_by_specialty.sort_values("no_show_rate", ascending=False)

print("\n KPI by Specialty (by no-show rate)")
print(kpi_by_specialty.head(10))

kpi_by_specialty.to_csv("../kpi_by_specialty.csv", index=False)
print("Saved: kpi_by_specialty.csv")

trend = (
    df.groupby(["month", "specialty"])
      .agg(booked=("visit_id", "count"),
           no_show=("is_no_show", "sum"),
           avg_wait=("wait_minutes_calc", "mean"))
      .reset_index()
)
trend["no_show_rate"] = trend["no_show"] / trend["booked"]
trend.to_csv("../monthly_trend.csv", index=False)
print("Saved: monthly_trend.csv")




