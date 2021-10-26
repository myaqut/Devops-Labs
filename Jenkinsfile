

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('testing') {
            steps {
                sh 'python --version'
                sh ' pip install -r ./flaskapp/requirements.txt '
                sh 'python3 ./flaskapp/unitest.py'
            }
        }
    }
}

