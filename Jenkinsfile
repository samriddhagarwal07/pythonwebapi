pipeline {
    agent any
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
                    // Use the Azure Service Principal credentials binding
                    withCredentials([azureServicePrincipal(credentialsId: 'azure-service-principal')]) {
                        def clientId = env.AZURE_CLIENT_ID
                        def clientSecret = env.AZURE_CLIENT_SECRET
                        def tenantId = env.AZURE_TENANT_ID

                        // Now deploy to Azure with these credentials
                        if (isUnix()) {
                            // Unix specific commands
                            sh """
                            echo "Logging into Azure..."
                            az login --service-principal -u $clientId -p $clientSecret --tenant $tenantId
                            echo "Deploying to Azure from Unix..."
                            az webapp deploy --resource-group myResourceGroup --name myWebApp --src-path ./dist
                            """
                        } else {
                            // Windows specific commands
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
