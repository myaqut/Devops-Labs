

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('testing') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --upgrade pip'
                sh 'python3 ./flaskapp/unitest.py'
            }
        }
    }
}

