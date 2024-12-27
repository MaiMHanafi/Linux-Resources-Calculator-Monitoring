# Linux Resources Calculator and Monitoring
This project monitors key Linux system resources (CPU, memory, disk usage, and network statistics) and displays them in a simple web interface using Flask. It is containerized using Docker for easy deployment on any machine.

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Prerequisites](#Prerequisites)
3. [Setup Instructions](#Setup-Instructions)
   - [Clone the Repository](#Clone-the-Repository)
   - [Install Dependencies](#Install-Dependencies)
   - [Run the Application Locally](#Run-the-Application-Locally)
4. [Dockerization](#Dockerization)
   - [Docker Image Creation](#Docker-Image-Creation)
   - [Run the Docker Container](#Run-the-Docker-Container)
   - [Push to Docker Hub](#Push-to-Docker-Hub)
5. [Technologies Used](#Technologies-Used)
6. [How to use - Guide](#How-to-use---Guide)
7. [Repository Links](#Repository-Links)

## **Project Overview**
This project calculates and displays system resource data like:
 
  - CPU usage
  - Memory usage (total, available, used, free, etc.)
  - Disk usage (total, used, free)
  - Network statistics (bytes sent/received, packets sent/received)

The system resource data is captured using the psutil Python library and displayed in a web interface via the Flask framework. The app is containerized with Docker for easy deployment on any server or machine.


## **Prerequisites**
Before setting up the project, make sure you have the following installed:

  - **Python 3.7+**: The application is developed in Python.
  - **pip**: Python's package installer.
  - **Docker**: For containerization of the app.
  - **Git**: To clone the repository.

## **Steps to install prerequisites:**
**1.  Install Python (if not installed)**
On Ubuntu:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
**2. Install Docker** On Ubuntu:
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl enable --now docker
```
***3. Install Git** On Ubuntu:
```bash
sudo apt update
sudo apt install git
```

## **Setup Instructions**

**1. Organize Your Project Directory**

Set up your project directory with the following structure:
```bash
RESOURCES_CALCULATION/
│
├── static/
│   └── styles.css
├── templates/
│   └── index.html
└── app.py
```
- **static/**: Contains static assets such as CSS files.
  - **styles.css**: The CSS file used for styling the web interface.
  
- **templates/**: Contains HTML templates used by Flask for rendering views.
  - **index.html**: The HTML template used to display the system resource data.

- **app.py**: The main Python file where the Flask app runs, retrieves system resources data, and renders the HTML template.


**2. Create the python script**

Create the **app.py** file, Use the **psutil** library to fetch Linux resource data.

**3. Create the HTML file**

Create the **html.index** file inside the templates/ Directory.

**4. Create the CSS File**

Create the **styles.css** file inside the static/ directory and add your styles.

**5. Create the requirements.txt File**

Create the **requirements.txt** file that contains the following Python dependencies:

- **Flask:** Web framework to serve the data.
- **psutil:** To gather system resource data.

## Testing the App Locally
```bash
python3 app.py
```
By default, the app will be available at http://localhost:5000.


## **Dockerization** (Containerization your App)
### **Docker Image Creation**
To make the application easier to deploy, we containerized it using Docker. This allows it to run on any system without worrying about dependencies.

1- Create a **Dockerfile** in the root of the project.
2- Build the Docker image by running the following command in the same directory as the Dockerfile:

```bash
docker build -t <Your-Chosen-Image-Tag> .
```
3- Run the Docker Container
```bash
docker run -d -p 5000:5000 --name <Docker-Conatiner-Name> <Your-Chosen-Image-Tag>
```
This will run the container in detached mode and expose the web interface on port 5000.

4- Push to Docker Hub
To push the Docker image to Docker Hub (for sharing or deployment), you must first authenticate with Docker Hub using:

```bash
docker login
```
After authenticating, you can push the image:
```bash
docker push <DockerHub-Username>/<Your-Image-Name>:<Image-Tag>
```

## **Technologies Used**
- **Python 3**: For the application’s logic.
- **Flask**: A lightweight web framework to display the system resource data.
- **psutil**: To retrieve system information such as CPU, memory, disk, and network stats.
- **Docker**: To containerize the application for easy deployment.
- **Git**: To manage and version control the source code.
#How to use Guide

## **How to use - Guide**
## Docker Image
The Docker image for this project is hosted on Docker Hub. You can pull the image and run it on your machine or server using the following commands.

### Docker Image URL:
[Docker Hub: maihanafi/linux-resource-monitor](https://hub.docker.com/repository/docker/maihanafi/linux-resource-monitor/general)

### Pull the Docker Image:

To pull the latest image from Docker Hub, run the following command:

```bash
docker pull maihanafi/linux-resource-monitor:latest
```
### How to Run the Application ?
Once you have pulled the Docker image, you can run the application in a Docker container, using the following command:
```bash
docker run -d -p 5000:5000 --name linux-resource-monitor maihanafi/linux-resource-monitor
```
### Access the Web Interface:
Once the container is running, To be able to see the system resources data displayed on the web page, Open your browser and navigate to:

```bash
http://localhost:5000
```

### Contributing
If you'd like to contribute to this project, please fork the repository, make your changes, and create a pull request. All contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push to your fork.
6. Open a pull request.

## **Repository Links**
- [LinkedIn Profile](https://linkedin.com/in/mai-mohamed-hanafi-388b131b5)
- [Docker Hub](https://hub.docker.com/repository/docker/maihanafi/linux-resource-monitor/general)
