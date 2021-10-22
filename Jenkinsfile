pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sudo apt-get update
                sudo apt-get install python3.8
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
