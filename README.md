# Terraform
The following steps are for creating infrastructure using AWS EC2. 
## Steps: 

#### 1. Install Terraform
- Use the following commands to install Terraform on your Ubuntu/Debian machine. If you are using different OS please go to the following [link](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started).
``sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl``
``curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -``
``sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"``
``sudo apt-get update && sudo apt-get install terraform``

- Verify the installation by adding the following command to your terminal.
`sudo apt-get update && sudo apt-get install terraform`


#### 2. Create main Terraform File 
- create new folder for example "terraform".
- Create new file and name it "main.tf".
- Add the following content to your main.tf file.
```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

	required_version = ">= 0.14.9"
}

provider "aws" {
	profile = "default"
	region = "us-east-2"
}

resource "aws_instance" "app_server" {
	ami = "ami-0629230e074c580f2"
	instance_type = "t2.micro"
	tags = {
    Name = "ExampleAppServerInstance"
  }
}
```

#### 3. Configure AWS Credentials
- Go to IAM section in your EC2 account.
- Create new user for terraform and give it admin permission to your EC2 resources.
- Save access key ID and secret key.
- Type the following command on your terminal and enter the credentials you just saved
`aws configure`

#### 4. Initialize and Validate Terraform File
- Initiate the configuration you just added by typing the following in your terminal.
`terraform init`
- Format and validate your terraform by typing the following command.
`terraform fmt`
`terraform validate`
#### 5. Create Infrastructure 
- Finally Apply all the work you just added by typing the following.
`terraform apply`

- Open your EC2 account instances. You should find new instance being created with the name "ExampleAppServerInstance".
#### 6. Define Input Variables
- Create a new file in the same directory and name it " variables.tf .
- Add the following content to the file.
```
variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "ExampleAppServerInstance"
}
```

- Change the following section in your terraform.main file to be the following .
```
resource "aws_instance" "app_server" {

ami = "ami-0629230e074c580f2"

instance_type = "t2.micro"

tags = {

Name = var.instance_name

}

```
- Initiate Terraform again to confirm your changes.

#### 7. Query Data with Outputs
- Create new file in the same directory with the name "outputs.tf".
- Add the following content to your file.
```
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

```
- Type terraform apply and check the outputs. It should output the instance ID and IP address.
#### 8.  Store Remote State

- Create new account on [Terraform Cloud](https://www.terraform.io/cloud).
- Create new organization and workspace.
- Update your main.tf file with your terraform cloud info using the following snippet.
```
 backend "remote" 
 {
  organization = "<ORG_NAME>"+ workspaces 
  { = "Example-Workspace"
   }
    }
```
- Your main.tf file should look like the following.
```
terraform {

backend "remote" {

organization = "yaqot"

workspaces {

name = "ec2"

}

}

required_providers {

aws = {

source = "hashicorp/aws"

version = "~> 3.27"

}

}

required_version = ">= 0.14.9"

}

provider "aws" {

profile = "default"

region = "us-east-2"

}

resource "aws_instance" "app_server" {

ami = "ami-0629230e074c580f2"

instance_type = "t2.micro"

tags = {

Name = var.instance_name

}

}

```
- Login to terraform cloud.
``terraform login``
- Open the link showed in your terminal and copy the key generated.
- Paste the key in your terminal. note: the key won't be showed in your terminal once you paste it.
- Initiate terraform. Your infrastructure state should be saved now on the cloud.
- Delete the local terraform state file as you don't need it anymore.
``rm terraform.tfstate``
- Add your EC2 user credentials you created previously to terraform cloud by going to variables and creating the following two variables.
	- `AWS_ACCESS_KEY_ID`
	- `AWS_SECRET_ACCESS_KEY`
- Finally type ``terraform apply`` 
- For more details checkout the official [documentation](https://learn.hashicorp.com/tutorials/terraform/aws-remote?in=terraform/aws-get-started).

