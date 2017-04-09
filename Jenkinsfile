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
	        sh 'cp -r files/ /home/ubuntu/deployment/'
            }
        }
    }
}
