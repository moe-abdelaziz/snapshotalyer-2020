# snapshotalyer
Demo project to manage AWS EC2 instance snapshots

## About
This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

analyser uses the configuration file created by the AWS Cli

## Running

'pipenv run python analyser/analyser.py'



## Add user with no permission
## configure AWS CLI for the user
aws configure --profile analyser
## install pipenv 3
install pipenv --three
## install Boto3
pipenv install boto3
## install ipython
pipenv install -d ipython
## run ipython inside pipenv
pipenv run ipython
## Import boto3
import boto3
## Create session
session = boto3.Session(profile_name='analyser')
## Connect to resource via session
ec2 = session.resource('ec2')
## perform scripts against your ec2 resource
 for i in ec2.instances.all():
     print(i)

## use history of codes you typed by using %history
%history

