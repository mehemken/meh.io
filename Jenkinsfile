pipeline {
    agent {
        node {
            label 'master'
            customWorkspace '~/git/meh.io'
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
