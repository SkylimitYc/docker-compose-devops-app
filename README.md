# 🚀 Docker Compose DevOps Application

A complete hands-on **DevOps CI/CD project** demonstrating how to containerize a multi-service application, connect it with PostgreSQL, automate testing using GitHub Actions, publish Docker images to GitHub Container Registry (GHCR), and validate a production-style Docker Compose deployment.

> **Project Status:** ✅ Docker + PostgreSQL + CI/CD + GHCR completed  
> **Next Phase:** ☁️ AWS EC2 deployment

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Application Services](#-application-services)
- [Database](#-database)
- [API Endpoints](#-api-endpoints)
- [Running the Application Locally](#-running-the-application-locally)
- [Production Docker Compose](#-production-docker-compose)
- [CI Pipeline](#-ci-pipeline)
- [CD Pipeline](#-cd-pipeline)
- [Docker Images and GHCR](#-docker-images-and-ghcr)
- [Health Checks](#-health-checks)
- [Verification](#-verification)
- [Troubleshooting](#-troubleshooting)
- [DevOps Concepts Demonstrated](#-devops-concepts-demonstrated)
- [AWS Deployment - Next Phase](#-aws-deployment---next-phase)
- [Project Learning Outcomes](#-project-learning-outcomes)

---

# 📖 Project Overview

This project is designed as a practical DevOps implementation of a containerized application.

The application consists of three main services:

1. **Frontend** - Nginx-based web interface
2. **Backend** - Python Flask REST API
3. **Database** - PostgreSQL

Docker Compose is used to run and connect all services.

GitHub Actions is used to automate:

- Docker image builds
- Application startup
- API testing
- Database connectivity testing
- Docker image publishing
- Production-style deployment validation

Docker images are published to **GitHub Container Registry (GHCR)**.

---

# 🏗️ Architecture

```text
                         GitHub Repository
                                │
                                │ Push / Pull Request
                                ▼
                     ┌──────────────────────┐
                     │   GitHub Actions CI  │
                     └──────────┬───────────┘
                                │
                         Build & Test
                                │
                                ▼
                     ┌──────────────────────┐
                     │       GHCR           │
                     │ GitHub Container     │
                     │      Registry        │
                     └──────────┬───────────┘
                                │
                         Docker Images
                                │
                                ▼
                     ┌──────────────────────┐
                     │   GitHub Actions CD  │
                     └──────────┬───────────┘
                                │
                                ▼
                 Production Docker Compose
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
   ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
   │  Frontend   │       │   Backend   │       │ PostgreSQL  │
   │   Nginx     │──────▶│   Flask     │──────▶│     DB      │
   │    :80      │       │    :5000    │       │    :5432    │
   └─────────────┘       └─────────────┘       └─────────────┘
          │                     │                     │
          │                     │                     │
          └────────── Application Network ────────────┘