pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'python ret_val.py'
                bat 'echo "Hello world!"'
            }
        }
        stage('deploy') {
            steps {
                bat 'copy ret_val.py "C:\Users\Jozef Zivcic\Desktop"'
            }
        }
    }
}
