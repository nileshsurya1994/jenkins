pipeline {
    agent any
    stages {
        stage("clone") {
            steps {
                echo "Cloning Stage..."
                git url: "https://github.com/nileshsurya1994/jenkins.git", branch: "main"
            }
        }
        stage("build") {
            steps {
                echo "Building image Stage..."
                sh "docker build -t todoapp ."
            }
        }
        stage("deploy") {
            steps {
                echo "Stopping existing container"
                sh "docker stop $(docker ps -qf 'name=serene_lederberg')"
                echo "Removing existing container"
                sh "docker rm $(docker ps -aqf 'name=serene_lederberg')"
                echo "Deploying the updated container"
                sh "docker run -d -p 5000:5000 --name todoapp todoapp:latest"
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
