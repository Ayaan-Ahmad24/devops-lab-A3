pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 tests/test_app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Building the image
                sh 'docker build -t my-devops-app:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                // Stop remove old container if exists to avoid conflict, then run new
                sh 'docker rm -f devops-container || true'
                sh 'docker run -d -p 5000:5000 --name devops-container my-devops-app:latest'
            }
        }
    }
}