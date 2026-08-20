# Library ETL Project

## Business Scenario
A library stores information about:

- Books borrowed by customers
- Customer details

The source CSV files contained several data quality issues, including:

- Missing values
- Blank records
- Duplicate entries
- Date fields stored as text
- Invalid borrowing periods
- Customer IDs that may not exist in the customer master data

To ensure reliable reporting and analysis, an ETL pipeline was developed to cleanse, validate, and standardise the data before loading it into SQL Server.

## Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) process using Python, Pandas, SQL Server, and Unit Testing.
The objective is to build a reusable ETL pipeline that:

- Extracts raw data from CSV files
- Cleans and validates the data
- Applies business transformations
- Tracks Data Engineering metrics
- Loads the transformed data into SQL Server
- Provides a reporting layer for Power BI

## Stakeholders/End users
- The primary stakeholders for this solution are:
- Library Management, who require accurate reporting on book borrowing activity.
- Library Staff, who maintain customer and book records.
- Data Analysts, who use the cleansed data for reporting and analysis.
- Data Engineers, who monitor pipeline performance and data quality through operational metrics.

## Solution Architecture Diagram in Project Folder

SQL Server Outputs

The ETL pipeline loads three tables into SQL Server: 
1. Systembook_Clean (Contains cleansed and transformed book transaction data.)
2. Customer_Clean (Contains cleansed customer master data.)
3. Pipeline_Metrics (Contains operational and data quality metrics generated during each pipeline execution.)

### DE Metrics
To improve observability and provide operational reporting, the pipeline captures Data Engineering metrics during every execution.

Each pipeline run generates:
- Run ID
- Run Timestamp
- Source System
- Metric Name
- Metric Value
- Metrics Captured


## Technologies Used
- Python
- Pandas
- SQLAlchemy
- SQL Server (LocalDB)
- PyODBC
- unittest
- Power BI

## Future Improvements

- Advanced error handling
- Additional data validation rules
- Audit tables
- CI/CD integration with GitHub Actions
- Automated scheduling
- Enhanced Power BI operational monitoring dashboards