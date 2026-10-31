# AI381 MLOps Lab 2 - FastAPI & Docker CI/CD Pipeline

![CI Pipeline](https://github.com/Rattchanoo/ai381-portfolio/actions/workflows/ci.yml/badge.svg)

## 📌 Project Overview
This repository contains the setup for **MLOps Lab 2** for the **AI381** course at Jordan University of Science and Technology (JUST). It serves a trained Machine Learning model using **FastAPI**, fully containerized with **Docker**, and features an automated **GitHub Actions CI/CD pipeline** for testing and container image building.

---

## 🚀 One-Command Quickstart
To build and run the application container with a single command, execute the following in your terminal:

```bash
docker run -d -p 8000:8000 --name mlops-app $(docker build -q .)
