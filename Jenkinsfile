pipeline{
    agent any
    stages{
        stage('Development Environment'){
            steps{
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
    }
}