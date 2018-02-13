pipeline {
    agent { docker 'python:2.7.10' }
    stages {
        stage('build') {
            steps {
                bat 'python --version'
                bat 'echo "Hello world"'
            }
        }
    }
}
