# Exercise 8 — Jenkins Hello World Job

## Objective
Create and execute a simple shell script using a Jenkins Freestyle project.

## Technologies Used
- Jenkins
- Git and GitHub
- Bash shell scripting

## Project Structure
```text
Exercise-8-Jenkins-Hello-World-Job/
├── hello-world.sh
├── README.md
├── transcript.txt
└── Screenshots/
    └── jenkins-hello-world-success.png
```

## Shell Script
The `hello-world.sh` script contains:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Configuration
1. Created a Freestyle project named `HelloWorld`.
2. Configured Git source control using the `kubernetes-exercises` repository.
3. Set the branch specifier to `*/main`.
4. Added the build command:
   `sh Exercise-8-Jenkins-Hello-World-Job/hello-world.sh`
5. Saved the configuration and clicked **Build Now**.

## Result
The Jenkins build completed successfully and printed:

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Conclusion
Successfully configured a Jenkins Freestyle job to check out a GitHub repository and execute a shell script.