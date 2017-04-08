pipeline {
    agent any 

    stages {
        stage('Build') { 
            steps { 
                sh git pull #static site files
            }
        }
        stage('Test'){
            steps {
                sh pytest #run tests
            }
        }
        stage('Deploy') {
            steps {
                sh build script
            }
        }
    }
}
