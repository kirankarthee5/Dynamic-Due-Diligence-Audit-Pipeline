DYNAMIC DUE DILIGENCE PIPELINE: BROKERAGE RISK SIMULATOR

EXECUTIVE SUMMARY
This repository contains a full-stack Python data pipeline built for my B.Com (Hons) Capstone Project: "Impact of Dynamic Due Diligence on Brokerage Firms' Performance to Attract Investor Confidence." Traditional compliance auditing relies on manual Excel sampling, which is slow and prone to human error. To solve this, I engineered an automated ETL (Extract, Transform, Load) architecture that simulates, stores, and analyzes 100,000 retail brokerage transactions in under 2 seconds. This project demonstrates how scalable data engineering directly translates to reduced risk exposure and increased investor trust.

TECHNICAL ARCHITECTURE & TECH STACK
This project is broken into four modular stages, mimicking a true enterprise data environment:

Language: Python 3.x

Data Generation: NumPy (Vectorized Stochastic Simulation)

Database Management: SQLite3 (Relational SQL Vault)

Data Analytics: Pandas (Aggregation & Financial Modeling)

Visualization: Matplotlib & Seaborn (Executive Dashboards)

THE PIPELINE BREAKDOWN

1. Phase 1: The Stochastic Engine (1_numpy_engine.py)
Instead of flat, unrealistic data, this module uses NumPy to generate 100,000 synthetic trades mathematically modeled on a Normal Distribution (Bell Curve). It replicates actual retail market behavior (averaging 50,000 INR per trade with realistic standard deviations) and exports the raw data instantly.

2. Phase 2: The SQL Vault (2_sql_vault.py)
Raw CSVs are inefficient for financial auditing. This script uses Pandas to extract the 100,000 generated records and load them into a normalized SQLite database. It establishes a relational schema between Trades and Firms for secure querying.

3. Phase 3: The Pandas Auditor (3_pandas_auditor.py)
This is the analytical core. It executes a SQL JOIN to fuse the relational tables, pulls the data into memory, and uses Pandas' groupby() logic to instantly calculate total financial exposure (in Millions INR) for trades failing compliance checks. It outputs an audit-ready Executive_Risk_Report.csv.

4. Phase 4: The Boardroom Visual (4_visual_boardroom.py)
Executives require visual insights. This module takes the finalized audit data and renders a high-resolution, color-coded Seaborn Barplot showing exact risk distribution across major brokerage firms, proving the necessity of Dynamic Due Diligence.

BUSINESS IMPACT
By replacing standard spreadsheet auditing with a Python/SQL relational database model, this pipeline:

Increases Audit Volume: Scales from manual sampling to 100% transaction coverage (100k+ rows).

Reduces Processing Time: Completes the end-to-end extraction, calculation, and visualization in under 2.0 seconds.

Protects Investor Confidence: Instantly flags high-risk exposure outliers for immediate compliance intervention.

AUTHOR
Kiran Karthee
Finance & Data Analytics
