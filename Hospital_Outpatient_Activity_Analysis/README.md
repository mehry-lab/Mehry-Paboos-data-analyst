How to Run This Project

This project uses Python to clean, analyse, and visualise outpatient activity data.

Requirements

Python 3.9+

pandas

numpy

matplotlib

Install dependencies:

pip install pandas numpy matplotlib

Steps

Clone or download this repository.

Navigate to the project folder:

cd Hospital_Outpatient_Activity_Analysis/python


Run the data cleaning script:

python 01_data_cleaning.py


This generates a cleaned dataset:

outpatient_activity_cleaned.csv


Run KPI analysis:

python 02_kpi_analysis.py


This generates:

kpi_by_specialty.csv
monthly_trend.csv


Run visual analysis:

python 03_visual_analysis.py


This generates charts saved as PNG files.

Note: Python scripts are executed locally.
Generated outputs are committed to this repository for demonstration purposes.
