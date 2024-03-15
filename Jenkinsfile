pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("my-flask-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kube-config', serverUrl: 'http://127.0.0.1:36557/']) {
                        sh 'kubectl apply -f k8s/deployment.yaml'
                    }
                }
            }
        }
    }
}
