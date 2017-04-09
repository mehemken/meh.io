pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Integration') {
            steps {
	        sh 'echo foo'
            }
        }
    }
}
