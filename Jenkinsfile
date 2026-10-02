pipeline {
    agent any

    environment {
        APP_NAME = 'jenkins-practice'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out ${env.BRANCH_NAME} @ ${env.GIT_COMMIT}"
            }
        }
        stage('Build') {
            steps {
                echo "Building ${APP_NAME}..."
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest discover -s . -p "test_*.py" -v'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging app...'
                sh 'tar -czf app.tar.gz app.py Jenkinsfile README.md'
                archiveArtifacts artifacts: 'app.tar.gz', fingerprint: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Simulating deploy... (echo only, safe to experiment)'
                sh 'python3 app.py & sleep 1; kill %1 || true'
            }
        }
    }

    post {
        always  { echo 'Pipeline finished.' }
        success { echo 'SUCCESS - build is green.' }
        failure { echo 'FAILED - check console output above.' }
    }
}
