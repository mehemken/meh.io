pipeline {
    agent any
    triggers {
        pollSCM 'H/10 * * * *'
    }
    stages {
        stage('Integration') {
            steps {
                git pull
            }
        }
        stage('Delivery') {
            steps {
                sudo cp -r files /var/www/meh.io/files
            }
        }
    }
    post {
        always {
            sudo nginx -s reload
        }
    }
}
