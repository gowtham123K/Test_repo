pipeline {
    agent any
    stages {
        stage ('Checkout code'){
            steps {
                git url:"https://github.com/gowtham123K/Test_repo.git",branch:"main"
            }
        }
        stage ('Install dependencies') {
            steps {
                bat'''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }
 
        stage ('Test'){
            steps {
                bat'''
                    call venv\\Scripts\\activate
                    python test.py
                    '''
            }
        }
    }
}