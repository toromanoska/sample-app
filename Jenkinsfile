pipeline
{
    options {
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }
    agent any
    environment {
        registry = "saska/sample-app"
        registryCredential = "dockerhub"
    }
    stages {
        stage('Build preparations') {
            steps {
                script {
                    imageVersion = "${BUILD_ID}"
                    image = "$registry:$imageVersion"
                }
            }
        }
        stage('Pull the code') {
          steps {
              git 'https://github.com/toromanoska/sample-app.git'
          }
        }
        stage('Build the image from the Dockerfile') {
            steps {
                script {
                    // Build the docker image
                    docker.build(image,"./")
                }
            }
        }
        stage('Push the image to hub.docker') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    docker.image(image).push()
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
