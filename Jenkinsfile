pipeline {
    agent any

    environment {
        PROD_KEY = credentials('prod-dockerhub-credentials')
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    echo "Pulling Docker image from Docker Hub..."
                    sh 'docker pull maihanafi/linux-resource-monitor:latest'
                }
            }
        }
        stage('Deploy to Production Server') {
            steps {
                sshagent(['ubuntu']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@107.23.124.136 << 'EOF'
                        set -e  # Exit immediately if a command exits with a non-zero status
                        echo "Pulling the latest Docker image..."
                        docker pull maihanafi/linux-resource-monitor:latest
                        
                        echo "Stopping existing container if it exists..."
                        docker stop linux-resource-monitor || true
                        
                        echo "Removing existing container if it exists..."
                        docker rm linux-resource-monitor || true
                        
                        echo "Starting a new container..."
                        docker run -d --name linux-resource-monitor -p 8080:8080 maihanafi/linux-resource-monitor:latest
                        
                        echo "Deployment successful!"
                        EOF
                    """
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'There was an error during deployment.'
        }
    }
}
