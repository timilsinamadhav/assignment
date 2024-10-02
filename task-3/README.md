# Modern Web Application CI/CD Pipeline

This README provides an overview of the CI/CD pipeline setup for our modern web application in a Linux environment.

## Table of Contents
1. [Dockerfile](#dockerfile)
2. [Jenkins Pipeline](#jenkins-pipeline)
3. [Code Analysis and Vulnerability Checking](#code-analysis-and-vulnerability-checking)

## Dockerfile

We use a multistage Dockerfile to optimize our Docker image build:

- **Build Stage**: Uses `node:14-alpine` to build the application
- **Production Stage**: Creates a minimal production image

Key features:
- Efficient layer caching
- Smaller final image size
- Improved security by minimizing the attack surface

How our dockerfile is efficient:
In Docker, layering works by caching each instruction in the Dockerfile as a separate layer. Each layer is immutable, so if a layer changes, Docker rebuilds only the changed layer and subsequent layers. Efficient Dockerfiles place frequently changed code (like source files) in the last layer to avoid rebuilding everything.

In our dockerfile:

Multi-stage build: The first stage builds the app, and the second stage creates a lightweight production image by only copying essential files (dist, node_modules). This results in a smaller final image.
Without multi-stage, the final image would include unnecessary build tools, increasing its size and complexity.

## Jenkins Pipeline

Our CI/CD pipeline is defined in a Jenkinsfile with the following stages:

1. Checkout
2. SonarQube Analysis
3. Build Docker Image
4. Run Tests
5. Trivy Scan
6. Push to Registry
7. Deploy to Kubernetes

Environment variables and credentials are managed securely through Jenkins.

## Code Analysis and Vulnerability Checking

We integrate two tools for ensuring code quality and security:

1. **SonarQube**: 
   - Performs static code analysis
   - Identifies code smells, bugs, and security vulnerabilities

2. **Trivy**:
   - Scans Docker images for vulnerabilities
   - Checks OS packages and application dependencies

The pipeline includes quality gates that can fail the build if certain thresholds are exceeded.

## Getting Started

To use this setup:

1. Ensure Docker, Jenkins, SonarQube, and Trivy are installed in your environment
2. Configure Jenkins with necessary plugins and credentials
3. Set up a local Docker registry
4. Adjust the Jenkinsfile as needed for your specific project requirements
