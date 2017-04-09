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
	        sh 'cp files/ /home/ubuntu/deployment/'
            }
        }
    }
}
