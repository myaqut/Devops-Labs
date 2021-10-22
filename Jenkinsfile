pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            sh'sudo apt-get update'
            sh'sudo apt-get install python3'
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
