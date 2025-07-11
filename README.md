# URL Shortener

A simple URL shortener using Flask for the backend and NGINX for the static frontend. Both services run in Docker containers and are connected via Docker Compose.

## Current Progress

- Backend (Flask) returns shortened URLs
- Frontend (HTML/CSS/JS) served through NGINX
- Services run locally via Docker Compose

## Next Steps

- Push Docker images to AWS ECR
- Provision infrastructure using Terraform:
  - Set up VPC, ALB, and security groups
  - Deploy containers with ECS
  - Route traffic through an Application Load Balancer
- Configure HTTPS and optional domain routing
