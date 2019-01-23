# remix-blueprints
The "Infrastructure as Code" repo for all pieces or the Remix service. Will contain CloudFormation Templates, Ansible playbooks, deploy scripts, etc for all components of the service.

Note: It is highly recommended you use something like https://github.com/awslabs/git-secrets to prevent pushing AWS secrets to the repo

# Requirements
Before you begin, check that you have the following:
  - A role with permissions to deploy cloudformations. In most cases, will require permissions to create IAM roles/policies (see [Permissions Required to Access IAM Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html))
  - An existing SSL Certificate in the AWS Account you are deploying to
  - Must have awscli installed if using the example deploy commands

# Deploy

### Application Infrastructure Stack

```console
aws cloudformation deploy \
  --template-file deploy/cloudformation/app-infrastructure.yml \
  --stack-name remix-app-infrastructure \
  --tags ProjectName=remix Name='testaccount-remix-dev' Contact='me@myhost.org' Owner='myid' \
    Description='brief-description-of-purpose'
```

### Remix Pre-production Environment

```console
aws cloudformation deploy \
 --template-file deploy/cloudformation/static-host.yml \
 --capabilities CAPABILITY_IAM \
 --stack-name remix-prep-service
 --tags ProjectName=remix Name='testaccount-remix-prep' \
    Contact='me@myhost.org' Owner='myid' \
    Description='brief-description-of-purpose' \
 --parameter-overrides EnvType='dev' FQDN='fqdn-prep.domain.com' \
    AcmCertificateArn='arn-of-cert'
```
### Remix Production Environment

```console
aws cloudformation deploy \
 --template-file deploy/cloudformation/static-host.yml \
 --capabilities CAPABILITY_IAM \
 --stack-name remix-prod-service
 --tags ProjectName=remix Name='testaccount-remix-prod' \
    Contact='me@myhost.org' Owner='myid' \
    Description='brief-description-of-purpose' \
 --parameter-overrides EnvType='dev' FQDN='fqdn-prod.domain.com' \
    AcmCertificateArn='arn-of-cert'
```

### CI/CD Pipeline

``` console
aws cloudformation deploy \
  --template-file deploy/cloudformation/static-host-pipeline \
  --capabilities CAPABILITY_IAM \
  --stack-name remix-pipeline
  --tags ProjectName=remix Name='testaccount-remix-dev-pipeline' \
     Contact='me@myhost.org' Owner='myid' \
     Description='brief-description-of-purpose' \  
  --parameter-overrides Approvers='approvers@myhost.com' \
      SourceRepoOwner='RepoOwner' \
      SourceRepoName='RepoWithSouceCode' \
      CDBranchName='NameOfBranchToWatchForDeploy' \
      ConfigurationSourceRepoOwner='ConfigRepoOwner' \
      ConfigurationSourceRepoName='ConfigRepoName' \
      ConfigurationCDBranchName='NameOfBranchThatHasConfig' \
      OAuth='MyOAuthToken' \
      ProdStackName='NameOfProdHostStack' \
      TestStackName='NameOfTestHostStack'  
```
TODO:
* [ ] Determine if Lambda should exist in this stack or live elsewhere for reusability.
* [ ] Add enhanced monitoring to pipeline per /deploy/cloudformation/pipeline-monitoring.yml
