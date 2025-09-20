
"""
Performance logging utilities for memory, CPU, and response time.
"""
from app_core.utils.imports import *

def log_performance(time_taken):
    """
    Log memory usage, CPU usage, and response time to a file for each chat interaction.
    """
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss
    memory_usage_mb = memory_usage / (1024 * 1024)
    cpu_usage = psutil.cpu_percent(interval=1)
    with open(st.session_state.filename, 'a', encoding='utf-8') as f:
        f.write('\n')
        write_txt = 'Memory Consumed: ' + str(round(memory_usage_mb, 2)) + ' MB' + '\n'
        f.write(write_txt)
        write_txt = 'CPU Usage: ' + str(cpu_usage) + '%' + '\n'
        f.write(write_txt)
        write_txt = 'Time Taken: ' + str(round(time_taken, 2)) + 's' + '\n'
        f.write(write_txt)
