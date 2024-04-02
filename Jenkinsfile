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
