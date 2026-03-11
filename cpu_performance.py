import psutil
import time
import pyodbc

con = pyodbc.connect(
    r'Driver={SQL Server};'
    r'Server=MOHAMED_ABRAR\ABRAR;'
    r'Database=system;'
    r'Trusted_Connection=yes;'
)

cursor = con.cursor()

l = 1
while l == 1:
    CPU = psutil.cpu_percent()
    memory = psutil.virtual_memory()[2]

    cpu_interruption = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]

    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]

    cursor.execute('insert into performance values (GETDATE(),'
                   + str(CPU) + ' , '
                   + str(memory) + ' , '
                   + str(cpu_interruption) + ' , '
                   + str(cpu_calls) + ' , '
                   + str(memory_used) + ' , '
                   + str(memory_free) + ' , '
                   + str(bytes_sent) + ' , '
                   + str(bytes_received) + ' , '
                   + str(disk_usage) + ')'
                   )
    con.commit()
    print(CPU)
    time.sleep(1)
