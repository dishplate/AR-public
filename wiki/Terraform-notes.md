Basic start here: https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build

# Cheatsheet
az login
Set your subscription
az account set --subscription "35akss-subscription-id"
### Next, create a Service Principal. 
~~~
A Service Principal is an application within Azure Active Directory with the authentication 
tokens Terraform needs to perform actions on your behalf. 
Update the <SUBSCRIPTION_ID> with the subscription ID you specified in the previous step.
~~~
~~~
az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/<SUBSCRIPTION_ID>"
~~~
# SSH Keys
Azure uses rsa keys and not ecdsa it seems?
ssh-keygen -t rsa
