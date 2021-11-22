# Terraform Best Practices
Listed below some of the best practices you can take into consideration while working with terraform. 
### 1. Follow Proper Directory Structure 
While working on big infrastructure you would need to break your terraform files in proper directory. For instance if you have terraform files for staging you would add it in it's own folder. The following examples shows a proper directory structure.
```
```markup
terraform_project/
├── dev
│ ├── main.tf
│ ├── outputs.tf
│ └── variables.tf
├── modules
│ ├── ec2
│ │ ├── ec2.tf
│ │ └── main.tf
│ └── vpc
│ ├── main.tf
│ └── vpc.tf
├── prod
│ ├── main.tf
│ ├── outputs.tf
│ └── variables.tf
└── stg
├── main.tf
├── outputs.tf
└── variables.tf
```
### 2. Naming Conventions
Make sure to use simple and clear names for your files as it really helps while working on complex projects. Having clear names for your files and folder makes it easy for your colleagues and you to keep track of everything. 

### 3. Use Official Modules
Use the official modules created by terraform. Remaking already made modules by terraform is not efficient and more time consuming. Click the following [link](https://registry.terraform.io/) to check the available modules for terraform. 

### 4. Version Updates
Terraform regularly releases updates. Make sure to update your terraform version in order to maintain the security and performance.

### 5. Lock State Files
Normally more than one developer are working on the same project. So it's more likely to corrupt the state file if more than one developer trying to configure terraform at the same time. locking state files will prevent it from happening as it locks the terraform state to only the current developer who is doing the edits.

### 6. Use Var Files
You can use var files to pass some information to your main.tf file. This helps you avoiding adding any data you don't want to add to the configuration file such as access keys.
