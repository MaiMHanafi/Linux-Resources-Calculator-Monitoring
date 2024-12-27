import psutil

def get_resource_data():
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_info": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "network_stats": psutil.net_io_counters()._asdict(),
    }
    return data

if __name__ == "__main__":
    resource_data = get_resource_data()
    print(resource_data)
