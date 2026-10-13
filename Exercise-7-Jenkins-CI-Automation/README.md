# Exercise 7 — Jenkins CI Automation

## Objective
Set up Jenkins using Docker and configure a Freestyle job to automate a basic Continuous Integration (CI) workflow.

## Tools Used
- Docker Desktop
- Jenkins LTS
- Git and GitHub

## Implementation
1. Started Jenkins in a Docker container.
2. Installed the suggested Jenkins plugins.
3. Created the first Jenkins administrator account.
4. Configured a Freestyle job named `Jenkins-CI-Automation`.
5. Connected the job to the GitHub repository.
6. Configured an Execute Shell build step to display repository details and validate the checkout.
7. Ran the Jenkins build and checked the console output.

## Validation
The initial Jenkins build completed successfully. The console output was captured as evidence.

## Screenshots
See the `Screenshots` folder for evidence of the Jenkins setup and successful build.

## Result
Successfully set up Jenkins and ran a basic CI job that checks out source code from GitHub and executes shell commands.