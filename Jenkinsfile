pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "maihanafi/linux-resource-monitor:latest"
        PROD_SERVER = "107.23.124.136"
        PROD_USER = "ubuntu"
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    script {
                        echo "Pulling Docker image from Docker Hub..."
                        sh '''
                            echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                            docker pull $DOCKER_IMAGE
                        '''
                    }
                }
            }
        }

        stage('Deploy to Production Server') {
            steps {
                sshagent(['prod-server-ssh-key']) {
                    script {
                        echo "Deploying Docker container on production server..."
                        sh '''
                            ssh -o StrictHostKeyChecking=no $PROD_USER@$PROD_SERVER << EOF
                                sudo docker pull $DOCKER_IMAGE
                                sudo docker stop linux-resource-monitor || true
                                sudo docker rm linux-resource-monitor || true
                                sudo docker run -d --name linux-resource-monitor -p 5000:5000 $DOCKER_IMAGE
                            EOF
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
        failure {
            echo "There was an error during deployment."
        }
    }
}
