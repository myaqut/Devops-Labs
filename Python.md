# Best Python Application Practices 

### 1- Proper Documentation.
Documentation is really important in development using any language. We need documentation in order to understand the other's work and let others understand owners. Without documentation you can't add features or edits any code written by other developers and it would take you hours. Documentation includes adding comments in your code as well as adding readme file attached to your project.

### 2- Follow Style Guides
Style guides are important for improving code quality and readability. PEP8  style guide for instance make it easier for others to read your code as well as make it easier for you to edit your own code. There are many extensions you can add to your IDE in order to apply the PEP8  style automatically while coding.

### 3- Exception Handling
Exceptions are important in order to understand the reason why you code stopped working in case something wrong happened.

### 4- Use Virtual Environments
Adding virtual environment for each project prevent module clashing as you would need different versions of modules for each project.

### 5- Avoid Creating Global Variables
Adding global variables will make your variables accessible by different functions from different places. It will be very hard for you to trace back the changes happened to your variables. In addition to that, using global variables reduces efficiency of the memory. 


# Best Unit Tests Practices 

### 1- Tests Should Be Fast:
Minimizing your tests execution time is important in order to have fast workflow.  Also having slow unit tests makes developers sometimes skip testing as it becomes a burden for them. 

### 2- Tests Should Be Readable:
Tests readability is very important in order to deliver to the developer if their code changes working fine or not. Having vague tests makes developers confused and sometimes they won't understand if there is something wrong, or it can lead to misunderstanding. 

###3- Tests Should Be Part of The Workflow Process:
The main purpose of having unit tests is to make sure that everything is working correctly before building your application after the new changes, so you should check that the new changes pass the unit tests as part of your workflow. 

###4- Tests Should Be Trustworthy: 
Make sure that your tests only fail when actually something wrong happens. Monitor your tests results many times and make sure that they provide accurate results 100% as you should rely on them before deploying your code. 

###5- Isolate Your Tests:
Unit tests should be runnable on any machine. You can provide your unit tests dependencies in your CI workflow. Also make sure that your unit tests are not affecting each other’s in order to get accurate results.

###6- Unit Tests Should Verify a Single-Use Case:
Every test should only cover 1 scenario or one use case. This structure helps with making your tests simple and more understandable. It also helps the developer debugging their code in case something wrong happened.
