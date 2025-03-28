pipeline {
    agent { label 'a1' }
    stages {
        stage('checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/DEVCOMSzkolenia/DEVOPS1.git'
            }
        }        
        stage('run tests') {
            steps {
               sh 'pytest'
            }
        }

        stage('Deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'docker build -t moja-apka . && docker push moja-apka'
            }
        }
        post {
            failure {
                echo 'Testy nie przeszły'
            }
            success {
                echo 'aplikcja zdeplojowana!'
            }
        }
    }
}