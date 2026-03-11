Power-BI-Analytics-Project

A real-time system monitoring dashboard that collects CPU, Memory, Disk, and Network statistics using Python, stores them in SQL Server, and visualizes the data in Power BI.

This project demonstrates how system performance data can be collected, stored, and analyzed using modern data visualization tools.

📊 Dashboard Preview

The dashboard displays:

CPU Usage

Disk Usage

Memory Usage

Network Traffic

CPU Calls & Interruptions

Memory Usage Distribution

All metrics are visualized using Power BI gauges, charts, and graphs.

⚙️ Technologies Used
Technology	Purpose
Python	Collect system metrics
psutil	System monitoring library
SQL Server	Store performance data
pyodbc	Python database connection
Power BI	Data visualization dashboard
🗂️ Project Architecture
Power-BI-Analytics-Project
│
├── cpu_performance.py      # Python script to collect system metrics
├── SQL Server Database
│      └── performance table
│
└── Power BI Dashboard
       └── Real-time system monitoring visuals
       
🗄️ Database Schema

| Column           | Type          | Description                  |
| ---------------- | ------------- | ---------------------------- |
| Time             | datetime      | Timestamp of data collection |
| cpu              | numeric(5,2)  | CPU usage percentage         |
| memory           | numeric(5,2)  | Memory usage percentage      |
| cpu-interruption | numeric(18,0) | CPU interrupts               |
| cpu-calls        | numeric(18,0) | CPU calls                    |
| memory_used      | numeric(18,0) | Used memory                  |
| memory_free      | numeric(18,0) | Free memory                  |
| bytes_send       | numeric(18,0) | Network bytes sent           |
| bytes_received   | numeric(18,0) | Network bytes received       |
| disk_usage       | numeric(5,2)  | Disk usage percentage        |

🐍 Python Data Collector

The Python script collects system performance metrics every 1 second and stores them in SQL Server.

Script file:
📄 

cpu_performance

Key features:

Uses psutil to capture system metrics

Inserts data into SQL Server

Runs continuously for real-time monitoring

Example metrics collected:

CPU Usage

Memory Usage

Disk Usage

Network Traffic

CPU Interruptions

CPU Calls

🔄 Data Flow
System Metrics
      │
      ▼
Python Script (psutil)
      │
      ▼
SQL Server Database
      │
      ▼
Power BI Dashboard
      │
      ▼
Real-Time Performance Visualization

🚀 How to Run the Project
1️⃣ Install Python Libraries
pip install psutil
pip install pyodbc
2️⃣ Create SQL Server Database

Create a database named:

system

Create the performance table.

3️⃣ Configure Database Connection

Update the server name in the Python script:

Server=YOUR_SERVER_NAME

Example:

Server=MOHAMED_ABRAR\ABRAR
4️⃣ Run the Python Script
python cpu_performance.py

This will start collecting system metrics every 1 second.

5️⃣ Connect Power BI

Open Power BI Desktop

Click Get Data

Select SQL Server

Connect to the database

Load the performance table

📈 Power BI Dashboard Components

The dashboard includes:

Gauges

CPU Performance

Disk Performance

Memory Performance

Charts

Network Bytes Sent vs Received

CPU Calls vs Interruptions

Memory Used vs Free

🎯 Project Use Cases

This system can be used for:

Server performance monitoring

Data center monitoring

System diagnostics

Infrastructure analytics

DevOps monitoring dashboards

🔮 Future Improvements

Real-time streaming dashboard

Alert system for high CPU usage

Email notifications

Historical trend analysis

Cloud deployment

👨‍💻 Author

Mohamed Abrar

Project:Power-BI-Analytics-Project

