pipeline {
    agent { docker { image 'python:3.9.6-alpine3.14' } }
    stages {
        stage('testing') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r ./flaskapp/requirements.txt'
                sh 'python3 ./flaskapp/unitest.py'
            }
        }
    }
}

