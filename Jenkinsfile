pipeline {
    agent { docker { image 'python:3.9.6-alpine3.14' } }    
    
    stages{
        stage('clone'){
            steps{
                
git branch: 'main', credentialsId: 'f707ba26-5c29-4630-a9a4-32b64edd7d10', url: 'https://github.com/myaqut/devops.git'
            }
        }
        stage('Building our image') { 

            steps { 
                sh """
                docker build -t first_one .
                
                """

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
