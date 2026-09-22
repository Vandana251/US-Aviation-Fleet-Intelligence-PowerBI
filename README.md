# Aviation Fleet Maintenance & Delay Root-Cause Tracker (2024)

An enterprise-grade Power BI business intelligence and root-cause analysis solution built on the **2024 Bureau of Transportation Statistics (BTS) Airline On-Time Performance dataset** (~7.08 Million flights).

---

## 🛫 Project Overview
Commercial airlines and fleet managers face significant operational and financial losses due to flight delays and cancellations. This project establishes a multi-dimensional analytics model to track:
1. **On-Time Performance (OTP) Benchmarks** across 16 major US carriers.
2. **Delay Root-Cause Attribution** (Carrier/Maintenance vs. Inbound Late Aircraft vs. ATC/NAS vs. Weather vs. Security).
3. **Ripple Effect Tracking** (how early morning maintenance delays cascade through fleet schedules).
4. **Geographic & Route Bottlenecks** across 348 commercial airports and thousands of routes.

---

## 📁 Repository Structure
```
├── flight_data_2024_backup.csv      # Untouched original dataset backup (1.3 GB, 7.08M rows)
├── flight_data_2024_cleaned.csv     # Cleaned full dataset with 6 derived fields (1.57 GB, 7.08M rows)
├── flight_data_2024_powerbi.csv     # 1,000,064-row stratified representative sample for Power BI (226 MB)
├── dim_airlines.csv                 # Airline code to airline name dimension lookup (16 carriers)
├── dim_airports.csv                 # Airport code, city, and state dimension lookup (348 airports)
├── dim_calendar.csv                 # Full 2024 leap-year date dimension table (366 days)
├── aviation_theme.json              # Custom modern dark Power BI theme
├── cleaning_report.txt              # Complete ETL & data transformation audit trail
└── README.md                        # Project documentation
```

---

## 🛠️ Data Pipeline & Engineering
- **Deduplication:** 0 duplicate records identified; 100% data integrity verified.
- **Handling Missing Values:** Maintained null values for cancelled and diverted flight times to preserve true arithmetic flight metrics; filled categorical delay cause breakdowns cleanly with zero.
- **Stratified Sampling:** 1,000,064 records extracted via multi-dimensional stratification across `Month` $\times$ `Airline` $\times$ `DelayStatus` $\times$ `DelayReason` (all category variances $\le 0.03\%$).
- **Derived Analytics Fields:**
  - `Route`: Origin-Destination airport pair (e.g. `JFK-LAX`).
  - `MonthName` & `DayOfWeekName`: Calendar time-series dimensions.
  - `TotalDelayMinutes`: Attributable positive delay minutes.
  - `DelayStatus`: FAA-standard operational classification (`Early`, `On Time`, `Delayed` $\ge 15$m, `Cancelled`, `Diverted`).
  - `DelayReason`: Granular operational root cause (`Carrier Delay`, `Late Aircraft Delay`, `NAS Delay`, `Weather Delay`, `Security Delay`, `Cancelled - Reason`).

---

## 📊 Core DAX Measures
- **On-Time Performance (OTP) %:**
  $$\text{OTP \%} = \frac{\text{On-Time Flights + Early Flights}}{\text{Completed Flights}}$$
- **Delay Rate %:**
  $$\text{Delay Rate \%} = \frac{\text{Delayed Flights (}\ge 15\text{ min)}}{\text{Completed Flights}}$$
- **Carrier / Maintenance Delay Share %:**
  $$\text{Carrier Delay Share \%} = \frac{\text{Carrier Delay Minutes}}{\text{Total Delay Minutes}}$$

---

## 📑 10-Page Operational Intelligence Dashboard Architecture

The dashboard is structured across **10 specialized analytical views**:

| Page # | Page Title | Core Purpose & Key Visuals |
|---|---|---|
| **Page 1** | **Executive Overview (C-Suite)** | Macro KPIs, Monthly Volume vs. Delay Rate dual-axis trend, FAA flight status breakdown |
| **Page 2** | **Delay Root-Cause Attribution** | Decomposition of Carrier, Late Aircraft, NAS, Weather & Security hours + monthly stacked trends |
| **Page 3** | **Fleet Maintenance & Reliability** | Controllable Carrier delay hours, maintenance share benchmark %, turnaround agility rating |
| **Page 4** | **Delay Cascade & Ripple Effect** | Time-of-day propagation (00:00-23:00), morning buffer erosion, inbound compounding curve |
| **Page 5** | **Airline Carrier Benchmarking** | 16-carrier head-to-head leaderboard (OTP%, Delay Rate%, Cancellation%, Taxi-out) |
| **Page 6** | **Airport Hub Operations** | Top 25 congested origin/destination hubs, departure delays, NAS vs Weather ground stops |
| **Page 7** | **Route Network Intelligence** | Top congested city pairs (DFW-SFO, SAN-SFO, etc.), Haul distance delay matrix |
| **Page 8** | **Temporal Peak-Hour Heatmaps** | Day-of-Week volume/delays (Mon-Sun), peak business vs leisure turnaround windows |
| **Page 9** | **Weather Impact & Cancellations** | FAA Cancellation Codes (A, B, C, D), winter blizzards vs summer convective storms |
| **Page 10** | **Taxi Times & Runway Efficiency** | Gate-to-takeoff duration, % flights taxiing $\ge$ 20 min, airport surface gridlock score |

---

## 📈 Key Insights & Findings (2024)
- **National OTP:** 78.41% on-time arrival rate; 21.59% delay rate; 1.44% cancellation rate.
- **Leading Major Carrier:** **Delta Air Lines (DL)** achieved top legacy performance with **82.02% OTP**, with regional leader **Republic Airways (YX)** achieving **84.36% OTP**.
- **Lagging Major Carrier:** **American Airlines (AA)** and **Frontier (F9)** experienced higher delay rates (25.65% and 28.05%).
- **Primary Delay Driver:** **Inbound Late Aircraft Ripple Effect** caused **40.97%** of all lost delay hours, followed by **Carrier / Maintenance Issues (32.17%)** and **Air Traffic Control / NAS (19.95%)**.
- **Peak Delay Season:** **July 2024** was the most delayed month (28.66% delay rate) with an average arrival delay of 17.98 minutes.

