import pandas as pd
import matplotlib.pyplot as plt

db = pd.read_csv("../outpatient_activity_cleaned.csv")

wait_by_spec = (
    db[db["is_completed"] == True]
    .groupby("specialty")["wait_minutes_calc"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure(figsize=(10, 5))
wait_by_spec.plot(kind="barh")
plt.title("Average Wait Time by Specialty")
plt.xlabel("Minutes")
plt.ylabel("Specialty")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../fig_wait_by_specialty.png", dpi=200)
plt.show()


no_show_rate = (
    df.groupby("specialty")
      .apply(lambda x: x["is_no_show"].sum() / len(x))
      .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
no_show_rate.plot(kind="bar")
plt.title("No-Show Rate by Specialty")
plt.ylabel("No-Show Rate")
plt.xlabel("Specialty")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../fig_no_show_rate_by_specialty.png", dpi=200)
plt.show()


df["month"] = pd.to_datetime(df["scheduled_time"], errors="coerce").dt.to_period("M").astype(str)
monthly = df.groupby("month")["visit_id"].count()

plt.figure(figsize=(11, 4))
monthly.plot(kind="line")
plt.title("Outpatient Bookings Over Time (Monthly)")
plt.ylabel("Booked Visits")
plt.xlabel("Month")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../fig_monthly_bookings.png", dpi=200)
plt.show()
