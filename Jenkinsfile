pipeline {
    
    	environment {
		DOCKERHUB_CREDENTIALS=credentials('eaa35e88-ec2e-4f4d-9864-f802ef697185')
	}


    agent { label "master" }  
    
    
    stages{
        stage('clone'){
            steps{
                
git branch: 'main', credentialsId: 'f707ba26-5c29-4630-a9a4-32b64edd7d10', url: 'https://github.com/myaqut/devops.git'
            }
        }
        stage('testing') {
                 agent { docker { image 'python:3.9.6-alpine3.14' } }
            steps {
                
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r ./flaskapp/requirements.txt'
                sh 'python3 ./flaskapp/unitest.py'
            }
        }
         stage('Building our image') { 

            steps { 
                sh """
                docker build -t yaqot/timeappjenkins:latest .
                
                """

            } 

        }

        stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		
		
		stage('Push') {

			steps {
				sh 'docker push yaqot/timeappjenkins:latest'
			}
		}


        
        
        }
    
}
