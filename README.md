# Financial Anti-Crime Data Normalization and Ingestion System

## Project Status: In Progress

### Overview
This project aims to develop a system to normalize and ingest financial transaction data into a PostgreSQL database on AWS. The system will help detect and prevent financial crimes such as money laundering, fraud, and other suspicious activities.

### Objective
The main objective is to create a robust system capable of processing large volumes of financial transaction data, normalizing it, and storing it in a structured manner for further analysis.

### Project Components
- **Data Source:** Simulated financial transaction data
- **Data Normalization:** Cleaning and standardizing the data
- **Data Ingestion:** Loading the normalized data into a PostgreSQL database on AWS
- **Data Processing:** Using Java and Scala for processing the data
- **Automation:** Utilizing Unix utilities for scheduling and automating tasks

### Next Steps
1. **Setup AWS Environment**
   - Configure Amazon RDS for PostgreSQL, Amazon S3 for data storage, and optionally AWS Lambda for serverless processing.

2. **Simulate Financial Transaction Data**
   - Create a Python script to generate simulated financial transaction data with various attributes.

3. **Data Normalization**
   - Utilize Unix utilities such as awk, sed, and grep for initial data cleansing and transformation.
   - Develop Java and Scala applications for further cleaning and normalization tasks.

4. **Data Ingestion**
   - Store raw and normalized data files in Amazon S3.
   - Write SQL scripts to create necessary tables and ingest data into PostgreSQL.

5. **Data Processing and Analysis**
   - Use SQL queries to analyze the data and identify patterns indicative of financial crimes.
   - Develop Java and Scala applications for complex data processing and report generation.

6. **Automation and Scheduling**
   - Schedule data generation, normalization, and ingestion tasks using Unix Cron Jobs.
   - Write shell scripts to automate the execution of Java and Scala programs.

7. **Documentation and GitHub**
   - Write a comprehensive README file explaining the project, its structure, and how to run it.
   - Ensure all code is well-commented and push all code, documentation, and relevant files to a GitHub repository.

### Contact
For any questions or feedback, please contact [project owner's name] at [email address].

