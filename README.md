# ETL Pipeline for Sales Data Analysis

This project showcases an **end-to-end ETL pipeline** built using Python, Apache Airflow, and PostgreSQL to process and analyze daily sales data from multiple sources.

---

## Features

- Automated ingestion from CSV files and REST APIs
- Data transformation and loading into PostgreSQL
- Integrated **Great Expectations** for data quality checks
- Interactive Power BI dashboard for business insights

---

## Folder Structure

```
etl-pipeline-sales-analysis/
├── dags/                      # Airflow DAGs
├── sql/                       # SQL scripts
├── expectations/              # Great Expectations validations
├── dashboards/                # Power BI or mock-up dashboards
├── data/                      # Sample sales data
└── requirements.txt           # Python dependencies
```

---

## Technologies Used

- Python, Apache Airflow
- PostgreSQL
- Great Expectations
- Power BI
- REST APIs, CSV

---

## Outcome

- Automated daily ETL processing
- Real-time data validation
- Clean dashboards with **product performance** and **sales trends**

---

## How to Run (Locally Simulated)

1. Place sample sales CSVs in the `/data` folder
2. Configure and start Airflow scheduler
3. Run DAG from `/dags/sales_etl_dag.py`
4. Visualize processed data using Power BI dashboards

---

## Contact

**Sai Gayathri Makineni**  
Graduate Student – M.S. Computer Science  
University of North Texas  
Email: saigayathri18@gmail.com  
LinkedIn: https://www.linkedin.com/in/sai-gayathri-makineni/
