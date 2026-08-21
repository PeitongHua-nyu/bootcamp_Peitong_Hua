\# Homework 02 — Project Setup



\## Project Overview



This project analyzes apartment options in Downtown Brooklyn for incoming NYU Tandon students. The goal is to help students compare housing options based on factors such as rent, proximity to campus, apartment type, and building amenities.



\## Project Structure



\- `data/raw/` — raw project data

\- `data/processed/` — cleaned and processed data

\- `notebooks/` — Jupyter notebooks for analysis

\- `src/` — reusable Python code and configuration

\- `docs/` — project documentation

\- `reports/` — project outputs and reports

\- `model/` — model-related files



\## Environment Setup



The project uses environment variables stored in a local `.env` file.



Example configuration:



API\_KEY=dummy\_key\_123  

DATA\_DIR=./data



The `.env` file is excluded from Git using `.gitignore`. A `.env.example` file is included as a template.



\## Current Setup



The project currently includes:



\- A reproducible Python environment

\- A NumPy demonstration notebook

\- Environment variable loading with `python-dotenv`

\- A reusable configuration file in `src/config.py`

\- Git ignore rules for secrets, cache files, and notebook checkpoints

