import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------
# Simulation Parameters
# ---------------------

DURATION_HOURS = 24
SAMPLING_SECONDS = 5
TOTAL_SAMPLES = int((DURATION_HOURS * 3600) / SAMPLING_SECONDS)

SLEEP_HR = 55
REST_HR = 70
ACTIVE_HR = 95
EXERCISE_HR = 145

NOISE_STD = 2
np.random.seed(42)

# ---------------------
# Create Time Index
# ---------------------

time_index = pd.date_range(
    start="2025-01-01 00:00:00",
    periods=TOTAL_SAMPLES,
    freq="5s"
)

df = pd.DataFrame(index=time_index)
df["heart_rate"] = REST_HR

# ---------------------
# Simulate Sleep & Activity
# ---------------------

sleep_mask = (df.index.hour >= 23) | (df.index.hour < 7)
df.loc[sleep_mask, "heart_rate"] = SLEEP_HR

active_mask = (df.index.hour >= 7) & (df.index.hour < 22)
df.loc[active_mask, "heart_rate"] = ACTIVE_HR

# ---------------------
# Inject Exercise Sessions
# ---------------------

exercise_sessions = [
    ("07:00", 30),
    ("18:30", 45)
]

for start_time, duration_min in exercise_sessions:
    start = pd.Timestamp(f"2025-01-01 {start_time}")
    end = start + pd.Timedelta(minutes=duration_min)
    df.loc[start:end, "heart_rate"] = EXERCISE_HR

# ---------------------
# Heart Rate Recovery (FIXED)
# ---------------------

for start_time, duration_min in exercise_sessions:
    end = pd.Timestamp(f"2025-01-01 {start_time}") + pd.Timedelta(minutes=duration_min)

    recovery_index = df.loc[
        end : end + pd.Timedelta(minutes=15)
    ].index

    if len(recovery_index) > 0:
        recovery = np.linspace(EXERCISE_HR, ACTIVE_HR, len(recovery_index))
        df.loc[recovery_index, "heart_rate"] = recovery

# ---------------------
# Add Sensor Noise
# ---------------------

df["heart_rate"] += np.random.normal(0, NOISE_STD, TOTAL_SAMPLES)
df["heart_rate"] = df["heart_rate"].clip(lower=40)

# ---------------------
# Inject Dropouts
# ---------------------

motion_mask = df["heart_rate"] > 100
drop_indices = df[motion_mask].sample(frac=0.05).index
df.loc[drop_indices, "heart_rate"] = np.nan

# ======================
# Pandas Tasks
# ======================

# Infer sleep vs active
df["state"] = "Active"
df.loc[df["heart_rate"] < 65, "state"] = "Sleep"

# Detect exercise
df["exercise"] = df["heart_rate"] > 130
df["exercise_block"] = (df["exercise"] != df["exercise"].shift()).cumsum()

exercise_events = df[df["exercise"]].groupby("exercise_block").agg(
    start=("heart_rate", "idxmin"),
    end=("heart_rate", "idxmax"),
    duration_sec=("heart_rate", lambda x: len(x) * SAMPLING_SECONDS)
)

# Recovery time calculation
recovery_times = []

for _, row in exercise_events.iterrows():
    post = df.loc[row["end"]:]
    recovered = post[post["heart_rate"] < 90]
    if not recovered.empty:
        recovery_times.append(
            (recovered.index[0] - row["end"]).seconds / 60
        )

# Abnormal HR detection
df["abnormal"] = (df["heart_rate"] < 45) | (df["heart_rate"] > 160)

# Daily summary
summary = pd.DataFrame({
    "Total Sleep Hours": [(df["state"] == "Sleep").sum() * SAMPLING_SECONDS / 3600],
    "Exercise Sessions": [len(exercise_events)],
    "Avg Recovery Time (min)": [np.mean(recovery_times)],
    "Abnormal HR Events": [df["abnormal"].sum()]
})

print("\n--- DAILY FITNESS SUMMARY ---")
print(summary)

# ======================
# Visualizations
# ======================

plt.figure(figsize=(14,4))
df["heart_rate"].plot()
plt.title("Heart Rate Over 24 Hours")
plt.xlabel("Time")
plt.ylabel("Heart Rate (BPM)")
plt.grid(True)
plt.show()

plt.figure(figsize=(14,4))
plt.plot(df.index, df["heart_rate"], label="Heart Rate")
plt.scatter(
    df[df["exercise"]].index,
    df[df["exercise"]]["heart_rate"],
    color="red",
    label="Exercise"
)
plt.legend()
plt.title("Exercise Detection")
plt.show()

df["state"].value_counts().plot(kind="bar")
plt.title("Sleep vs Active Periods")
plt.ylabel("Samples")
plt.show()
