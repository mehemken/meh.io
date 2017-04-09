pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Integration') {
            steps {
	        sh 'cp -r ./files /var/www/fanoftal2.io/html/meh.io/files'
	        sh 'chown -R $USER:$USER /var/www/fanoftal2.io/html/meh.io'
            }
        }
    }
}
