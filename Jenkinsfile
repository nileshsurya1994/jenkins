pipeline {
    agent any
    stages {
        stage("clone") {
            steps {
                echo "Cloning Stage"
                git url: "https://github.com/nileshsurya1994/jenkins.git", branch: "main"
            }
        }
        stage("build") {
            steps {
                echo "Building image Stage"
                sh "docker build -t todoapp ."
            }
        }
        stage("push-to-docker") {
            steps {
                echo "Pushing image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "dockerhub", passwordVariable: "dockerhubpass", usernameVariable: "dockerhubuser")]) {
                    sh "docker tag todoapp ${env.dockerhubuser}/todoapp:latest"
                    sh "echo ${env.dockerhubpass} | docker login -u ${env.dockerhubuser} --password-stdin"
                    sh "docker push ${env.dockerhubuser}/todoapp:latest"
                }
            }
        }
        stage("deploy") {
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
