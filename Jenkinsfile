pipeline {
    agent { label 'a1' }
    stages {
        stage('git') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/DEVCOMSzkolenia/DEVOPS1.git'
            }
        }        
        stage('pytest test') {
            steps {
               sh 'pytest'
            }
        }
    }
}