

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('testing') {
            steps {
                sh 'python --version'

                sh 'python3 ./flaskapp/unitest.py'
            }
        }
    }
}

