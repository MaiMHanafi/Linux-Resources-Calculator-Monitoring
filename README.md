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
6. [Repository Links](#Repository-Links)

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

## **Repository Links**
- [GitHub Repository](https://github.com/MaiMHanafi/Linux-Resources-Calculator-Monitoring)
- [Docker Hub](https://hub.docker.com/repository/docker/maihanafi/linux-resource-monitor/general)
