pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            sh'apt-get update'
            sh'apt-get install python3'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
