# CI Best Practices: 

## Gt Actions Bests Practices:  

### 1- Keep Actions Minimal.
It's important to keep your build actions light and fast. For instance, if you are using docker image to run your actions make sure that you are using smallest image possible. Use only the necessary actions in order to keep your building time minimal.

###2- Avoid unnecessary dependencies.
To keep your build fast make sure that you only install what you need and nothing extra. Every time you run your build the machine is downloading the dependencies in order to be able to carry on the next steps and this is added to the total build time. 

###3- Avoid Hardcoding Secrets and Passwords.
You can use Github encrypted secret handling and use your secret keys as variables in your workflow. 

###4- Automate Workflow.
Make sure that your workflow is automated on specific triggers without running manually. You can trigger your workflow on certain events such as push and pull.

###5- Break Your Jobs into Clear Named Steps.
Use steps in order to breakdown your jobs. Using conventionally named steps make it easier to track your workflow, and understand where and why it failed in case an error happened.
