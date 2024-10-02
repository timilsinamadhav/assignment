# Kubernetes Multi-Container Application

This repository contains Kubernetes manifests for deploying a simple multi-container application consisting of a frontend web server (nginx) and a backend API server (FastAPI).

## Prerequisites

- Kubernetes cluster
- kubectl configured to communicate with your cluster

## Structure

The application consists of the following components:

- Frontend: Nginx web server
- Backend: FastAPI API server
- Kubernetes resources: Deployments, Services, and Ingress

## Deployment Files

- `frontend-deployment.yaml`: Deployment for the frontend Nginx server
- `backend-deployment.yaml`: Deployment for the backend FastAPI server
- `frontend-service.yaml`: Service to expose the frontend deployment
- `backend-service.yaml`: Service to expose the backend deployment
- `ingress.yaml`: Ingress resource to expose the frontend service externally

## Deployment Instructions


1. Apply the Kubernetes manifests:
   ```
   kubectl apply -f frontend-deployment.yaml
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-service.yaml
   kubectl apply -f backend-service.yaml
   kubectl apply -f ingress.yaml
   ```

2. Verify the deployments:
   ```
   kubectl get deployments
   kubectl get pods
   kubectl get services
   kubectl get ingress
   ```

## Accessing the Application

- The frontend is exposed via the Ingress resource. Get the Ingress IP or hostname:
  ```
  kubectl get ingress
  ```
  Use this IP or hostname (mti.local in this example) in your web browser to access the frontend.

- The backend is accessible internally at `http://backend-service`.

## Testing Internal Communication

To test if the frontend can communicate with the backend:

```
kubectl exec -it $(kubectl get pod -l app=frontend -o jsonpath="{.items[0].metadata.name}") -- curl backend-service
```

## Customization

### Frontend

The frontend uses the official Nginx image. To customize:

1. Create your own Nginx configuration and Dockerfile.
2. Build and push your custom image to a container registry.
3. Update `frontend-deployment.yaml` to use your custom image.

### Backend

The backend uses a FastAPI image. To customize:

1. Create your FastAPI application (example provided in `backend-app.py`).
2. Build a Docker image with your application.
3. Push the image to a container registry.
4. Update `backend-deployment.yaml` to use your custom image.

## Cleanup

To remove all the resources created by this application:

```
kubectl delete -f .
```
