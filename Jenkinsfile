pipeline {
    agent {
        node {
            label 'master'
        }
    }
    triggers {
        pollSCM('*/5 * * * *')
    }
    stages {
        stage('Integration') {
            steps {
	        sh 'echo "foo bar baz"'
            }
        }
    }
}
