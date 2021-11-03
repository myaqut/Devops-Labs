pipeline {
        environment {
        DOCKERHUB_CREDENTIALS = credentials('docher-hub-secret')
        }

    agent { label 'master' }

    stages {
        stage('Clone and test') {
            agent { docker { image 'python:3.9.6-alpine3.14' } }
            steps {
                git branch: 'main', credentialsId: 'f707ba26-5c29-4630-a9a4-32b64edd7d10', url: 'https://github.com/myaqut/devops.git'

                sh '''python -m pip install --upgrade pip
                pip install -r ./flaskapp/requirements.txt
                python3 ./flaskapp/unitest.py
                '''
            }
        }
        stage('Building our image') {
            steps {
                sh '''
                docker build -t yaqot/timeappjenkins:latest .
                '''
            }
        }

        stage('Login and push ') {
            steps {
                sh'''echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push yaqot/timeappjenkins:latest
                    '''
            }
        }
    }
}
