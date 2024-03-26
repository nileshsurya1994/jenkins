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
                echo "Building image Stage"
                sh "docker build -t todoapp ."
            }
        }
        stage("deploy") {
            steps {
               echo "Stopping existing container"
        script {
            CONTAINER_ID = sh(script: 'docker ps -qf "name=serene_lederberg"', returnStdout: true).trim()
            if (CONTAINER_ID) {
                CONTAINER_NAME = sh(script: 'docker inspect --format "{{.Name}}" $CONTAINER_ID', returnStdout: true).trim()
                sh "docker stop $CONTAINER_NAME"
                echo "Removed existing container: $CONTAINER_NAME"
            } else {
                echo "No existing container found"
            }
        }

        echo "Deploying the updated container"
        sh "docker run -d -p 5000:5000 --name serene_lederberg todoapp:latest"
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
