pipeline {
    agent any
    stages {
        stage("Install Docker") {
            steps {
                echo "Installing Docker..."
                sh "sudo apt update"
                sh "sudo apt install -y docker.io"
                sh "sudo systemctl start docker"
                sh "sudo systemctl enable docker"
                sh "sudo usermod -aG docker jenkins"
            }
        }
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
        stage("remove existing container") {
            steps {
                echo "Removing Container..."
                sh "docker stop todoapp"
                sh "docker rm todoapp"
            }
        }
        stage("deploy") {
            steps {
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
