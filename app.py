import psutil
from flask import Flask, render_template

app = Flask(__name__)

def convert_to_mb_with_unit(value_in_bytes):
    """Convert bytes to megabytes and append the unit."""
    return f"{round(value_in_bytes / (1024 * 1024), 2)} MB"

@app.route('/')
def display_resource_data():
    # Fetch raw data
    raw_memory_info = psutil.virtual_memory()._asdict()
    raw_disk_usage = psutil.disk_usage('/')._asdict()

    # Convert memory and disk data to human-readable format with units
    memory_info = {key: (convert_to_mb_with_unit(value) if isinstance(value, (int, float)) else value)
                   for key, value in raw_memory_info.items()}
    disk_usage = {key: (convert_to_mb_with_unit(value) if isinstance(value, (int, float)) else value)
                  for key, value in raw_disk_usage.items()}

    # Prepare the final data dictionary
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_info": memory_info,
        "disk_usage": disk_usage,
        "network_stats": psutil.net_io_counters()._asdict(),
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
