pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "njagan04/jenkins-cici-repo"
        DOCKER_TAG = "${env.GIT_COMMIT?.take(7) ?: 'latest'}"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {

                        dockerImage.push()
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}