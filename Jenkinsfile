pipeline {
    agent any
    stages ('Checkout out') {
        stage {
            steps {
                git url:"https://github.com/gowtham123K/Test_repo.git",branch:"main"
            }
        }
    stages ('Install dependencies') {
        stage {
            steps {
                bat'''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }
    }
    stages ('Test') {
        steps {
            bat'''
                call venv\\Scripts\\activate
                python test.py
                '''
        }
    }

    
    }
}