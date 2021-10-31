# CI Best Practices: 

## Gt Actions Bests Practices:  

### 1- Keep Actions Minimal.
It's important to keep your build actions light and fast. For instance, if you are using docker image to run your actions make sure that you are using smallest image possible. Use only the necessary actions in order to keep your building time minimal.

### 2. Avoid unnecessary dependencies.
To keep your build fast make sure that you only install what you need and nothing extra. Every time you run your build the machine is downloading the dependencies in order to be able to carry on the next steps and this is added to the total build time. 

### 3. Avoid Hardcoding Secrets and Passwords.
You can use Github encrypted secret handling and use your secret keys as variables in your workflow. 

### 4. Automate Workflow.
Make sure that your workflow is automated on specific triggers without running manually. You can trigger your workflow on certain events such as push and pull.

### 5. Break Your Jobs into Clear Named Steps.
Use steps in order to breakdown your jobs. Using conventionally named steps make it easier to track your workflow, and understand where and why it failed in case an error happened.

## Jenkins Best Practices 

### 1. Backups and Updates
Make sure to keep updating jenkins to maintain performance and security as jenkins releases updates periodically. Also make sure to take updates of your jenkins server to avoid losing data. 
### 2. Optimize Builds on Master Node
Avoid adding unnecessary builds on your master node to optimize performance. Adding unnecessary builds to master node will consume more CPU and memory resources.
### 3. Optimize Builds-Up History
Optimize your job configuration to limit the history of old builds. Having very big history will result to save many  old builds in file system. 
### 4. Optimize Plugins
Make sure to only use needed plugins. Be careful while adding new plugins and only use them if needed. Usually plugins increase the build time, so having many plugins will result in slowing down your jobs.
### 5. Use Multiple Jenkins Masters
It's recommended to have more than one master while having different projects. Doing so will insure that changes on one project is not going to affect the others and only plugins added on one master won't be added on the other. 
### 6. Breakdown Your Jobs
Try to breakdown your jobs to smaller jobs. Doing so will make it easier for you to track your stages and debug your project in case of failure. 
