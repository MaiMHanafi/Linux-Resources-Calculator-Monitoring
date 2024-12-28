pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "maihanafi/linux-resource-monitor:latest"
        PROD_SERVER = "107.23.124.136"
        PROD_USER = "ubuntu" // SSH username on the production server
        PROD_KEY = credentials('prod-ssh-key') // Jenkins credentials for SSH key
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    echo "Pulling Docker image from Docker Hub..."
                    sh "docker pull ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Deploy to Production Server') {
            steps {
                script {
                    echo "Deploying Docker container on production server..."
                    sshagent (credentials: ['prod-ssh-key']) {
                        sh """
                        ssh ${PROD_USER}@${PROD_SERVER} <<EOF
                        docker pull ${DOCKER_IMAGE}
                        docker stop linux-resource-monitor || true
                        docker rm linux-resource-monitor || true
                        docker run -d --name linux-resource-monitor -p 5000:5000 ${DOCKER_IMAGE}
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
        failure {
            echo 'There was an error during deployment.'
        }
    }
}
