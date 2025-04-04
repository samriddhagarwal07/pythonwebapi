pipeline {
    agent any
    environment {
        AZURE_CREDENTIALS = credentials('azure-service-principal')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/samriddhagarwal07/pythonwebapi.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        // Example Unix build command (Replace with actual commands)
                        sh 'echo "Building the project on a Unix system"'
                    } else {
                        // Example Windows build command (Replace with actual commands)
                        bat 'echo "Building the project on a Windows system"'
                    }
                }
            }
        }

        stage('Publish') {
            steps {
                script {
                    if (isUnix()) {
                        // Example Unix publish command (Replace with actual commands)
                        sh 'echo "Publishing on Unix"'
                    } else {
                        // Example Windows publish command (Replace with actual commands)
                        bat 'echo "Publishing on Windows"'
                    }
                }
            }
        }

        stage('Deploy to Azure') {
            steps {
                script {
                    // Ensure that credentials are injected correctly
                    withCredentials([string(credentialsId: 'azure-service-principal', variable: 'AZURE_CREDENTIALS_JSON')]) {
                        def azureCredentials = readJSON text: AZURE_CREDENTIALS_JSON
                        
                        // Ensure correct credentials and tenant
                        def clientId = azureCredentials.clientId
                        def clientSecret = azureCredentials.clientSecret
                        def tenantId = azureCredentials.tenantId
                        
                        if (isUnix()) {
                            // Example Unix command to login and deploy to Azure
                            sh """
                            echo "Logging into Azure..."
                            az login --service-principal -u $clientId -p $clientSecret --tenant $tenantId
                            echo "Deploying to Azure from Unix..."
                            az webapp deploy --resource-group myResourceGroup --name myWebApp --src-path ./dist
                            """
                        } else {
                            // Example Windows command to login and deploy to Azure
                            bat """
                            echo "Logging into Azure..."
                            az login --service-principal -u $clientId -p $clientSecret --tenant $tenantId
                            echo "Deploying to Azure from Windows..."
                            az webapp deploy --resource-group myResourceGroup --name myWebApp --src-path .\\dist
                            """
                        }
                    }
                }
            }
        }
    }
}
