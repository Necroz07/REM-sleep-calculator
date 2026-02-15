# REM Sleep Cycle Calculator

A simple Python script that helps you plan your sleep by estimating when your REM cycles will occur. You input how long you take to fall asleep and how many REM cycles you want to track, and it outputs the expected times and total hours slept.

Features
- Estimates REM cycles using 90-minute intervals
- Accounts for your personal fall-asleep time
- Shows cycle time + hours slept
- Lightweight, no external libraries

## How to run

```python remsleep.py```

## How It Works
- Assumes each REM cycle ≈ 90 minutes
- Adds your sleep latency (time to fall asleep)
- Calculates future cycle timestamps
