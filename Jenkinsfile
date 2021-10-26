

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('testing') {
            steps {
                sh 'python --version'
                sh 'cd ./flaskapp'
                sh 'python3 unitest.py'
            }
        }
    }
}

