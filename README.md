# aws-infra-deployment

# AWS Infrastructure Automation Project: Tartela

## Overview
This project demonstrates the deployment of a secure, scalable, and highly available AWS infrastructure for a web application using a combination of **Terraform**, **CloudFormation**, **AWS Lambda**, **Boto3**, and **GitHub**. The infrastructure is built to support autoscaling, secure network segregation, event-driven logging, and version-controlled infrastructure as code.

## Architecture Components

The architecture includes:

- **VPC** with both **Public and Private Subnets**
- **EC2 Instances** behind an **Application Load Balancer (ALB)**
- **Relational Database**: RDS (or EC2-hosted MySQL/PostgreSQL)
- **S3 Bucket** for storing static files, logs, and backups
- **AWS Lambda** triggered by S3 uploads to log events to CloudWatch
- **Auto Scaling Group** for the web servers
- **Security Groups** for ALB, EC2, RDS, and Lambda
- **CloudFormation** for provisioning core services
- **Terraform** for networking setup
- **GitHub Integration** for version control and CI/CD via GitHub Actions

See the [Architecture Diagram] for a visual layout.


## Repository Structure

