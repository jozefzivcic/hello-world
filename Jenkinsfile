pipeline {
    agent { any }
    stages {
        stage('build') {
            steps {
                bat 'echo "Hello world"'
                python ret_val.py
            }
        }
    }
}
