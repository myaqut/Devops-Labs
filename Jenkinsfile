pipeline {
  agent { docker { image 'python:3.7.2' } }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            sh'pip install -r ./flaskapp/requirements.txt'
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
