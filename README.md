# remix-blueprints
The "Infrastructure as Code" repo for all pieces or the Remix service. Will contain CloudFormation Templates, Ansible playbooks, deploy scripts, etc for all components of the service.

Note: It is highly recommended you use something like https://github.com/awslabs/git-secrets to prevent pushing AWS secrets to the repo

# Requirements
Before you begin, check that you have the following:
  - A role with permissions to deploy cloudformations. In most cases, will require permissions to create IAM roles/policies (see [Permissions Required to Access IAM Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html))
  - An existing SSL Certificate in the AWS Account you are deploying to
  - Must have awscli installed if using the example deploy commands

# Deploy

### Remix Application Stack

```console
aws cloudformation deploy \
  --capabilities CAPABILITY_IAM \
  --template-file deploy/cloudformation/remix-stack.yml \
  --stack-name remix-dev \
  --tags ProjectName=remix Name='testaccount-remix-dev' Contact='me@myhost.org' Owner='myid' \
    Description='brief-description-of-purpose'
  --parameter-overrides OAuthToken=my_oauth_key \
    RemixCertificateArn=arn-of-valid-cert \
    FQDN=fqdn-of-service EnvType='dev'
```

TODO:
* [ ] Determine if Lambda should exist in this stack or live elsewhere for reusability.
