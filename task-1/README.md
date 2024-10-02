# Kubernetes Multi-Container Application with Dynamic Scaling

## Objective

This lab orchestrates a multi-container application composed of three microservices (A, B, and C) in Kubernetes. The main objectives include:

- Dynamic scaling of Service A using HPA based on CPU utilization.
- Dynamic scaling of Service B based on the custom metrics of Service A's CPU utilization.
- Scheduling Service C on nodes with GPU resources.
- Secure inter-service communication within the cluster.

## Prerequisites

- A Kubernetes cluster with Metrics Server and GPU nodes.
- Prometheus and Prometheus Adapter for custom metrics scaling.
- Helm for deploying Prometheus and related components.

## File Structure

- `manifests/`
  - `deployment-service-a.yaml`
  - `deployment-service-b.yaml`
  - `deployment-service-c.yaml`
  - `hpa-service-a.yaml`
  - `hpa-service-b.yaml`

## Deployment Steps

1. Apply the manifests for deploying the services:
   ```bash
   kubectl apply -f manifests/deployment-service-a.yaml
   kubectl apply -f manifests/hpa-service-a.yaml
   kubectl apply -f manifests/deployment-service-b.yaml
   kubectl apply -f manifests/hpa-service-b.yaml
   kubectl apply -f manifests/deployment-service-c.yaml

## Explanation:
### 1. Service A (Standard Metrics - CPU, Memory)
- **Metrics Server**:
  - **Purpose**: Provides CPU and memory metrics to the Horizontal Pod Autoscaler (HPA) for scaling.
  - **Installation**:
    ```bash
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    ```
  - **How it Works**: Collects metrics from nodes and pods, enabling the HPA to monitor and scale Service A based on its CPU and memory usage.

### 2. Service B (Custom Metrics - CPU of Service A)
- **Prometheus**:
  - **Purpose**: Collects custom metrics such as the CPU usage of Service A.
  - **Installation**:
    ```bash
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm install prometheus prometheus-community/prometheus
    ```
- **Prometheus Adapter**:
  - **Purpose**: Converts Prometheus metrics into Kubernetes custom metrics, which the HPA uses to scale Service B.
  - **Installation**:
    ```bash
    helm install prometheus-adapter prometheus-community/prometheus-adapter
    ```
  - **How it Works**: Prometheus gathers the custom metrics from the cluster. The Prometheus Adapter exposes these metrics to the HPA, allowing Service B to scale based on the CPU usage metrics of Service A.

## Why CPU and Memory Metrics Are Not Always Ideal

- **Not Always Reflective**: CPU and memory usage do not always represent the true workload, especially for event-driven or I/O-intensive applications.
- **Reactive Scaling**: Scaling based on CPU/memory can be slow, leading to delays in handling sudden workload spikes.
- **Application-Specific Needs**: Metrics like queue length or request rates are often more relevant than CPU/memory for certain applications.

## How KEDA Helps with Event-Driven Patterns

- **Event-Based Scaling**: KEDA enables scaling applications based on real-time events (e.g., message queues, HTTP requests) rather than just CPU and memory usage.
- **Custom Metrics**: Supports scaling using custom metrics, offering better control tailored to the application's specific needs.
- **Proactive Scaling**: Triggers scaling based on events, allowing for faster and more efficient handling of workload changes.