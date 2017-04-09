pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Integration') {
            steps {
	        sh 'cp -r ./files ~/git/meh.io/files'
            }
        }
    }
}
