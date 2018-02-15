pipeline {
    agent { label 'docker' }
    stages {
        stage('build') {
            steps {
                sh 'python ret_val.py'
            }
        }
    }
}
