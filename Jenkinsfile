pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "maihanafi/linux-resource-monitor:latest"
        PROD_SERVER = "107.23.124.136"
        PROD_USER = "ubuntu" // SSH username on the production server
        PROD_KEY = credentials('prod-ssh-key') // Jenkins credentials for SSH key
        DOCKERHUB_CREDS = credentials('docker-hub-credentials') // DockerHub credentials (username/password or token)
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    echo "Pulling Docker image from Docker Hub..."
                    // Log in to Docker Hub before pulling the image
                    sh """
                    docker login -u ${DOCKERHUB_CREDS_USR} -p ${DOCKERHUB_CREDS_PSW}
                    docker pull ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Deploy to Production Server') {
            steps {
                script {
                    echo "Deploying Docker container on production server..."
                    sshagent (credentials: ['prod-ssh-key']) {
                        bash """
                        ssh ${PROD_USER}@${PROD_SERVER} <<EOF
                        set -x
                        sudo docker pull ${DOCKER_IMAGE}
                        sudo docker stop linux-resource-monitor || true
                        sudo docker rm linux-resource-monitor || true
                        sudo docker run -d --name linux-resource-monitor -p 5000:5000 ${DOCKER_IMAGE}
                        EOF
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
        success {
            echo "Docker image successfully deployed to production."
        }
        failure {
            echo "There was an error during deployment."
        }
    }
}
