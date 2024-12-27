# Linux Resources Calculator and Monitoring

This project is a simple application designed to monitor Linux system resources (CPU usage, memory usage, disk usage, and network statistics) and present this data through a web interface. It is containerized using Docker for easy deployment and scaling.

## Docker Image

The Docker image for this project is hosted on Docker Hub. You can pull the image and run it on your machine or server using the following commands.

### Docker Image URL:
[Docker Hub: maihanafi/linux-resource-monitor](https://hub.docker.com/repository/docker/maihanafi/linux-resource-monitor/general)

### Pull the Docker Image:
To pull the latest image from Docker Hub, run the following command:

```bash
docker pull maihanafi/linux-resource-monitor:latest


### How to Run the Application ?
Once you have pulled the Docker image, you can run the application in a Docker container, using the following command:

```bash
docker run -d -p 5000:5000 --name linux-resource-monitor maihanafi/linux-resource-monitor


### Access the Web Interface:
Once the container is running, To be able to see the system resources data displayed on the web page, Open your browser and navigate to:

```bash
http://localhost:5000


### Technologies Used
- Python 3 for the application.
- Flask for the web framework.
- psutil for retrieving system resource data.
- Docker for containerization.
