pipeline {
    agent any
    stages {
        stage('clone'){
            steps{
           git credentialsId: 'myaqut', url: 'https://github.com/myaqut/devops.git'

            }
        }
        stage('testing') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r ./flaskapp/requirements.txt'
                sh 'python3 ./flaskapp/unitest.py'
            }
        }
    }
}
