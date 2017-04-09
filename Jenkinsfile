pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Integration') {
            steps {
                git pull
	        sh 'sudo cp -r ./files /var/www/fanoftal2.io/html/meh.io/files'
	        sh 'sudo chown -R $USER:$USER /var/www/fanoftal2.io/html/meh.io'
            }
        }
    }
}
