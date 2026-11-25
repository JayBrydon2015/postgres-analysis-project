# postgres-analysis-project

Analysis of a dataset using SQL, PostgreSQL, and Python. *Currently a work in progress.*

# Dataset

This project uses the New Zealand Transport Agency's (NZTA) Crash Analysis System (CAS) dataset, which contains information about traffic crashes reported to NZTA by the New Zealand Police.

The dataset includes information such as crash location, year, severity, road conditions, weather conditions, and vehicles involved.

The dataset can be accessed through the [NZTA Open Data Portal](https://opendata-nzta.opendata.arcgis.com/datasets/8d684f1841fa4dbea6afaefc8a1ba0fc/about).

The dataset is provided under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence.

The original dataset is not included in this repository. Download it from the source above and place `CAS_Data_public.csv` in the `datasets/` directory before running the import script.

## Requirements

- Anaconda or Miniconda
- PostgreSQL
- pgAdmin 4

Create the Conda environment using:

```bash
conda env create -f environment.yml
