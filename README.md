# Linux Production Lab

## About This Project

Linux Production Lab is a hands-on project created to simulate real production environments and real-time Linux issues that DevOps Engineers, Site Reliability Engineers (SREs), Cloud Engineers, and Linux Administrators face in their day-to-day work.

Instead of learning Linux commands in isolation, this project focuses on understanding how production incidents occur, how to investigate them, and how to resolve them using standard Linux troubleshooting techniques.

The goal is to provide a practical learning environment where anyone can reproduce common production issues on their own machine and practice solving them just like they would in a real organization.

This repository is continuously updated with new scenarios, troubleshooting guides, and interview-focused examples.

---

# Project Architecture

```
                 Browser
                     |
             http://localhost
                     |
                  Nginx
                     |
           Flask Demo Application
                     |
             Application Log Files
                     |
                Ubuntu Linux
```

The application is intentionally kept simple so that the primary focus remains on Linux administration and troubleshooting rather than application development.

---

# Technologies Used

- Ubuntu (WSL)
- Python
- Flask
- Nginx
- Bash
- Git
- GitHub
- VS Code

---

# Current Features

- Flask Demo Application
- Nginx Reverse Proxy
- Application Logging
- Linux Environment Setup
- Production-like Project Structure

---

# Real-Time Production Scenarios

The following scenarios will be implemented step by step.

## Linux Troubleshooting

- High CPU Usage
- Memory Leak
- Disk Full
- High Load Average
- Read-only Filesystem
- Permission Denied
- File Deleted
- Process Killed
- SSH Service Down
- Cron Job Failed
- Zombie Processes
- Out of Memory (OOM Killer)
- Log File Analysis
- Service Startup Failure

---

## Nginx Troubleshooting

- 502 Bad Gateway
- 504 Gateway Timeout
- Nginx Service Stopped
- Incorrect Nginx Configuration
- Reverse Proxy Failure
- Port Already in Use
- SSL Configuration Issues

---

## Application Troubleshooting

- Backend Application Crashed
- Application Running on Wrong Port
- Slow Application Response
- Application Log Analysis
- Health Check Failure

---

## File System Scenarios

- Disk Space Analysis
- Inode Exhaustion
- Directory Permission Issues
- File Ownership Problems
- Missing Configuration Files

---

## Process Management

- Finding High CPU Processes
- Finding High Memory Processes
- Killing Stuck Processes
- Restarting Services
- Monitoring Running Processes

---

## Monitoring and Performance

- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Network Monitoring
- Process Monitoring
- System Performance Analysis

---

# Repository Structure

```
Linux-Lab
│
├── app
│   ├── app.py
│
├── nginx
│   └── demo.conf
│
├── logs
│
├── scripts
│
├── docs
│
├── screenshots
│
├── README.md
│
└── requirements.txt
```

---

# Learning Objectives

By following this project, you will learn how to:

- Build a Linux troubleshooting environment
- Investigate production incidents
- Read and analyze Linux logs
- Troubleshoot Nginx issues
- Manage Linux services
- Understand process management
- Analyze CPU, memory, and disk utilization
- Resolve common production problems
- Prepare for Linux, DevOps, and SRE interviews

---

# Future Improvements

This project will continue to grow with additional production scenarios, automation scripts, monitoring integrations, and real-world troubleshooting exercises.

The objective is to build a practical Linux learning repository that can be used by beginners as well as experienced engineers preparing for interviews or improving their troubleshooting skills.

---

# Contributing

Suggestions, improvements, and new production scenarios are always welcome. If you have an idea for a real-world Linux issue or troubleshooting exercise, feel free to open an issue or submit a pull request.

---

# Author

Srikanth Mergu

Cloud | DevOps | Kubernetes | Terraform | CI/CD
