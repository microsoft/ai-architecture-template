[![Build Status](https://dev.azure.com/AZGlobal/Azure%20Global%20CAT%20Engineering/_apis/build/status/AGCI%20AI/Happy%20Path%20Builds/ai-architecture-template?branchName=master)](https://dev.azure.com/AZGlobal/Azure%20Global%20CAT%20Engineering/_build/latest?definitionId=170&branchName=master)
### Authors: Fidan Boylu Uz, Yan Zhang, Mario Bourgoin, Daniel Grecoe, Daniel Ciborowski

# AI Architecture Template

## Overview
This template is meant to simplify creating new Azure ML based projects, with an easy to configure Azure DevOps CI/CD pipeline.

## Prerequisites
1. [Anaconda Python](https://www.anaconda.com/download)
1. [Docker](https://docs.docker.com/v17.12/install/linux/docker-ee/ubuntu) installed.
1. [Azure account](https://azure.microsoft.com).

---
**NOTE**
You will need to be able to run docker commands without sudo to run this tutorial. Use the following commands to do
this.

```bash
sudo usermod -aG docker $USER
newgrp docker
``` 
---

The tutorial was developed on an [Azure Ubuntu
DSVM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro),
which addresses the first three prerequisites.

## Setup
## Create new repository

First either create a new repo from the template, or create a fork of this repo.
You can use this template by selecting `Use This Template` to create a new repository based on this project 
from the repository homepage.

## Set Up Azure DevOps Pipeline
You may use the .ci/azure-pipeline.yml to configure a CI/CD build for your repostitory. Follow the directions
provided within the pipeline.

For details on the prerequistes please see [here](az-ml-realtime-score). With the Azure CLI installed, the following
script can be used to create a new pipeline in your organizations Azure DevOps instance. 

   ```bash
   #!/usr/bin/env bash
   organization="<from dev.azure.com/[organization]>"
   project="<from dev.azure.com/organization/[project]>"
   service_connection="<Name Of New or Existing Service Connection>"
   name="<pipeline name>"
   repository="[github org]/[github repoistory name]"

   az extension add --name azure-devops

   az devops configure --defaults organization=https://dev.azure.com/$organization project="$project"

   az login

   az pipelines create --name $name            \
     --description ''                          \
     --repository $repository                  \
     --branch master                           \
     --repository-type github                  \
     --yml-path .ci/azure-pipelines-v2.yml     \
     --service-connection $service_connection
  ```

## Run Locally
To set up your environment to run this notebook, please follow these steps.  They setup the notebook to use Azure
seamlessly.
1. First either create a new repo from the template, or create a fork of this repo.
1. Clone your new repository locally, or on an Azure Data Science Virtual Machine.
   ```bash
   git clone https://github.com/[your_github_username_or_org]/[your_project].git
   ```
1. Enter the local repository:
   ```bash
   cd [your_project]
   ```
1. Copy `project_sample.yml` to a new file, `project.yml`, you can fill in the fields now,
or use the UI when running from the notebook. This will keep secrets out of the source code, 
and this file will be ignored by git.
   ```bash
   cp project_sample.yml project.yml
   ```
1. Create the Python ai-architecture-template virtual environment using the environment.yml:
   ```bash
   conda env create -f environment.yml
   ```
1. Activate the virtual environment:
   ```bash
   source activate ai-architecture-template
   ```
   The remaining steps should be done in this virtual environment.
1. Login to Azure:
   ```bash
   az login
   ```
   You can verify that you are logged in to your subscription by executing
   the command:
   ```bash
   az account show -o table
   ```
1. If you have more than one Azure subscription, select it:
   ```bash
   az account set --subscription <Your Azure Subscription>
   ```
1. Start the Jupyter notebook server:
   ```bash
   jupyter notebook
   ```


# Contributing
This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


# Related projects

[Microsoft AI Github](https://github.com/microsoft/ai) Find other Best Practice projects, and Azure AI Designed patterns
 in our central repository. 
