node('timeapp') {
    checkout scm
    stage('build') {
        docker.image('python:3.5.1').inside {
            sh 'python --version'
        }
    }
}
