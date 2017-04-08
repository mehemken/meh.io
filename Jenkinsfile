pipeline {
    agent any 

    stages {
        stage('Build') { 
            steps { 
                sh deploy_scripts/build.sh
            }
        }
        stage('Test'){
            steps {
                sh pytest #run tests
            }
        }
        stage('Deploy') {
            steps {
                sh deploy_scripts/deploy.sh
            }
        }
    }
}
