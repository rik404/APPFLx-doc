# Endpoint Installation

This page describes how to install a [funcX](https://funcx.org) compute endpoint for federated learning (FL) clients on their local computing resources. 

## Conda Environment

We highly recommend to create new conda virtual environment and install the required packages for setting funcX endpoint.

```
$ conda create -n funcx python=3.8
$ conda activate funcx
```

## Installation

Clone the APPFL+funcX repository, and install required packages.

```
$ git clone https://github.com/Zilinghan/FL-as-a-Service.git appflx && cd appflx && git checkout funcx
```

```
$ pip install -r requirements.txt
$ pip install -e .
```

## Create Globus Account
If you do not have a globus account yet, please create a [Globus](https://app.globus.org/) account here. 

@ShellyRiver: The following content should be a note.

Note: If you can find your institution in Globus, it is highly recommeneded to simply use your institution account to log in to Globus as it makes it easier for your collaborator to verify your identity. Otherwise, you can register a Globus account using your email address.

## Set up a funcX Endpoint
Setup funcX endpoint using the following command. Please replace `<ENDPOINT_NAME>` with your own name `anl-aws-gpu`.

You might be required to login with [Globus](https://app.globus.org/). Please follow the prompt instructions and finish the authentication steps.

```
$ funcx-endpoint configure <ENDPOINT_NAME>
```
## Configure the Endpoint
The command above will create a configuration file `$HOME/.funcx/<ENDPOINT_NAME>/config.py`. You should update this file with appropriate configurations for the computing resource you are using before start the endpoint. We provide few suggestions on setting this configuration file.

@ShellyRiver: Please make the following points as a list of bullet points
1. If you are using your own computer or some virtual machines provided by cloud service provider such as AWS EC2 or Azure virtual machines, you probably do not need change much of the `config.py` file. You just need to specify the number of blocks you want to allocate to the endpoint.

2. If you are using any supercomputer as your computing resources which uses some scheduler such as Slurm to allocate resources, you can find some example configurations for various supercomputers [here](https://funcx.readthedocs.io/en/latest/endpoints.html#example-configurations). We also provide two example configurations for allocating [CPU](https://github.com/Zilinghan/FaaS-web/blob/main/docments/config-cpu.py)/[GPU](https://github.com/Zilinghan/FaaS-web/blob/main/docments/config-gpu.py) resources on a supercomputer using Slurm scheduler.

@ShellyRiver: I want the following thing to be a note

1. If you have further questions about setting up funcX endpoint, please join the [funcX Slack](https://join.slack.com/t/funcx/shared_invite/zt-gfeclqkz-RuKjkZkvj1t~eWvlnZV0KA) for help.

2. Now funcX changes name to Globus Compute, so sometimes you may see term Globus Compute instead of funcX in the document of funcX, but they actually refers to the same thing.

## Start the Endpoint
Run the following command by replacing `<ENDPOINT_NAME>` with your endpoint name.
```
funcx-endpoint start <ENDPOINT_NAME>
```

## Get your Endpoint Id
The following command with print the id of your created endpoint.

```
funcx-endpoint list
```
## A Simple Test
You can create a python script (e.g. `test.py`) by copy the following codes to test if you have successfully set up a funcX endpoint. You need to put your own endpoint id into the script and you should see the printed result computed by your endpoint.

@ShellyRiver: I want the code to be display like code [here](https://appfl.readthedocs.io/en/latest/users/user_run.html)

```
from funcx import FuncXExecutor

def double(x):
    return x * 2

endpoint_id = '' #YOUR-ENDPOINT-ID
with FuncXExecutor(endpoint_id=endpoint_id) as fxe:
    fut = fxe.submit(double, 7)
    print(fut.result())
```


