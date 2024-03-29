
pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'vivek1592/flaskapp'
        DOCKER_IMAGE_TAG = 'first'
        DOCKER_HUB_CREDENTIALS_ID = 'docker-hub-credentials-id'
        KUBE_CONFIG_CREDENTIALS_ID = 'kube-config'
        K8S_NAMESPACE = 'default'
        DOCKER_USERNAME ="${env.DOCKER_USERNAME}"
        DOCKER_PASSWORD = "${env.DOCKER_PASSWORD}"
    }

   
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry("https://index.docker.io/v2/", "DOCKER_USERNAME", "DOCKER_PASSWORD") {
                           
                            def dockerImage = docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                            echo "Pushing Docker image..."
                            dockerImage.push()
                            echo "Docker image pushed successfully"

                            
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: KUBE_CONFIG_CREDENTIALS_ID, serverUrl: 'http://127.0.0.1:36557/']) {
                        sh 'kubectl apply -f k8s/deployment.yaml --namespace=${K8S_NAMESPACE}'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}






