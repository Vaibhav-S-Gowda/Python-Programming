import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# PARAMETERS
# =============================

DURATION_HOURS = 48
SAMPLING_SEC = 1
TOTAL_SECONDS = DURATION_HOURS * 3600

FLOW_IDLE = 0.0
NOISE_STD = 0.2
FLOW_THRESHOLD = 0.5
LEAK_FLOW = 0.6
LEAK_DURATION_HOURS = 6

np.random.seed(42)

# =============================
# TIME INDEX
# =============================

time_index = pd.date_range(
    start="2025-01-01",
    periods=TOTAL_SECONDS,
    freq="s"
)

df = pd.DataFrame(index=time_index)
df["flow_lpm"] = FLOW_IDLE

# =============================
# USAGE INJECTION
# =============================

def inject_usage(start_sec, duration_sec, flow_lpm):
    end = min(start_sec + duration_sec, TOTAL_SECONDS)
    df.iloc[start_sec:end, df.columns.get_loc("flow_lpm")] = flow_lpm

# Tap usage
for _ in range(40):
    inject_usage(
        np.random.randint(0, TOTAL_SECONDS - 120),
        np.random.randint(20, 60),
        np.random.uniform(4, 6)
    )

# Shower usage
for _ in range(10):
    inject_usage(
        np.random.randint(0, TOTAL_SECONDS - 900),
        np.random.randint(300, 600),
        np.random.uniform(8, 12)
    )

# Washing machine usage
for _ in range(6):
    inject_usage(
        np.random.randint(0, TOTAL_SECONDS - 1800),
        np.random.randint(900, 1500),
        np.random.uniform(6, 9)
    )

# =============================
# LEAK INJECTION (ADDITIVE)
# =============================

leak_start = np.random.randint(0, TOTAL_SECONDS - LEAK_DURATION_HOURS * 3600)
leak_end = leak_start + LEAK_DURATION_HOURS * 3600
df.iloc[leak_start:leak_end, df.columns.get_loc("flow_lpm")] += LEAK_FLOW

# =============================
# SENSOR NOISE
# =============================

noise = np.random.normal(0, NOISE_STD, TOTAL_SECONDS)
df.loc[df["flow_lpm"] > 0, "flow_lpm"] += noise[df["flow_lpm"] > 0]
df["flow_lpm"] = df["flow_lpm"].clip(lower=0)

# =============================
# EVENT SEGMENTATION
# =============================

df["is_flow"] = df["flow_lpm"] > FLOW_THRESHOLD
df["event_id"] = (df["is_flow"] != df["is_flow"].shift()).cumsum()

events = (
    df[df["is_flow"]]
    .groupby("event_id")
    .agg(
        start_time=("flow_lpm", lambda x: x.index.min()),
        end_time=("flow_lpm", lambda x: x.index.max()),
        duration_sec=("flow_lpm", "count"),
        avg_flow=("flow_lpm", "mean"),
        max_flow=("flow_lpm", "max")
    )
)

# =============================
# HOURLY WATER USAGE
# =============================

df["volume_liters"] = df["flow_lpm"] / 60
hourly_usage = df.resample("h")["volume_liters"].sum()

# =============================
# LEAK DETECTION
# =============================

df["low_flow"] = (df["flow_lpm"] > 0.3) & (df["flow_lpm"] < 1.5)
df["leak_flag"] = (
    df["low_flow"]
    .rolling(7200, min_periods=7200)
    .mean()
    > 0.9
)

leak_seconds = int(df["leak_flag"].sum())
total_leaked_liters = (df.loc[df["leak_flag"], "flow_lpm"] / 60).sum()

# =============================
# USAGE CLASSIFICATION
# =============================

def classify_event(row):
    if row["duration_sec"] < 120 and row["avg_flow"] < 6:
        return "Tap"
    elif row["duration_sec"] > 300 and row["avg_flow"] > 8:
        return "Shower"
    elif row["duration_sec"] > 600:
        return "Appliance"
    return "Other"

events["usage_type"] = events.apply(classify_event, axis=1)

# =============================
# VISUALIZATION PREP
# =============================

df_plot = df.resample("1min").agg({
    "flow_lpm": "mean",
    "leak_flag": "max"
})

# =============================
# VISUALIZATIONS
# =============================

# 1. Flow over time
plt.figure(figsize=(14,4))
plt.plot(df_plot.index, df_plot["flow_lpm"])
plt.title("Water Flow Rate (1-Minute Average)")
plt.xlabel("Time")
plt.ylabel("Flow (LPM)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Leak detection
plt.figure(figsize=(14,4))
plt.plot(df_plot.index, df_plot["flow_lpm"], label="Flow")
plt.scatter(
    df_plot.index[df_plot["leak_flag"]],
    df_plot.loc[df_plot["leak_flag"], "flow_lpm"],
    s=10,
    label="Leak"
)
plt.title("Leak Detection Visualization")
plt.xlabel("Time")
plt.ylabel("Flow (LPM)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Hourly usage
plt.figure(figsize=(12,4))
hourly_usage.plot(kind="bar", width=0.9)
plt.title("Hourly Water Consumption")
plt.xlabel("Hour")
plt.ylabel("Liters")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# 4. Usage distribution
plt.figure(figsize=(6,4))
events["usage_type"].value_counts().plot(kind="bar")
plt.title("Water Usage Type Distribution")
plt.ylabel("Number of Events")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# =============================
# OUTPUT SUMMARY
# =============================

print("\n--- FLOW STATISTICS ---")
print(df["flow_lpm"].describe())

print("\n--- LEAK SUMMARY ---")
print("Leak duration (hours):", round(leak_seconds / 3600, 2))
print("Total leaked water (liters):", round(total_leaked_liters, 2))
