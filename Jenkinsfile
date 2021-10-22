node('main') {
    checkout scm
    stage('time app') {
        docker.image('python:3.5.1').inside {
            sh 'python --version'
        }
    }
}
