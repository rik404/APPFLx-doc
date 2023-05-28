Endpoint Installation
============

This page describes how to install a `funcX <https://funcx.org/>`_ compute endpoint for federated learning (FL) clients on their local computing machines.

.. note::

	funcX endpoint is only supported on linux machine.

Conda environment
-----------------

We highly recommend to create a new conda virtual environment to install all the required packages for setting funcX endpoint.

.. code-block:: console

    	$ conda create -n funcx python=3.8
	$ conda activate funcx

Package Installation
-----------------

Clone our Github repository containing the source code for APPFL+funcX package. Specifically, this package handles the local training and the communication with the FL orchestration server on behave of the client. Then install all required packages by running the following commands.

.. code-block:: console

    	$ git clone https://github.com/Zilinghan/FL-as-a-Service.git appflx && cd appflx && git checkout funcx

.. code-block:: console

	$ pip install -r requirements.txt
	$ pip install -e .

Create Globus Account
-----------------

If you do not have a globus account yet, please create a Globus account `here <https://app.globus.org/>`.

.. note::

	If you can find your organization in Globus, it is highly recommeneded to use your organization account to log in to Globus as that makes it easier for your collaborators to verify your identity. Otherwise, you can register a Globus account using your email address.

Set up a funcX Endpoint
-----------------

Setup a funcX endpoint using the following command. Please replace ``<ENDPOINT_NAME>`` with your own name such as ``anl-aws-gpu-01``.

You might be required to login with Globus when configuring the endpoint. Please follow the prompt instructions and finish the authentication steps.

.. code-block:: console

	$ funcx-endpoint configure <ENDPOINT_NAME>

Configure the Endpoint
-----------------

The command above will create a configuration file ``$HOME/.funcx/<ENDPOINT_NAME>/config.py``. You should update this file with appropriate configurations for the computing resource you are using before start the endpoint. We provide few suggestions on setting this configuration file.

	- If you are using your own linux machine or some virtual machines provided by cloud service provider such as AWS EC2 or Azure virtual machine, you probably do not need change most part of the config.py file. You just need to specify the number of blocks you want to allocate to the endpoint.

	- If you are using any supercomputer as your computing resources which uses some scheduler such as Slurm to allocate resources, you can find some example configurations for various supercomputers `here <https://funcx.readthedocs.io/en/latest/endpoints.html#example-configurations>`_. We also provide two example configurations for allocating `CPU <https://github.com/Zilinghan/FaaS-web/blob/main/docments/config-cpu.py>`_/`GPU <https://github.com/Zilinghan/FaaS-web/blob/main/docments/config-gpu.py>`_ resources on a supercomputer using Slurm scheduler.

.. note::

	- If you have further questions about setting up funcX endpoints, please join the `funcX Slack <https://join.slack.com/t/funcx/shared_invite/zt-gfeclqkz-RuKjkZkvj1t~eWvlnZV0KA>`_ for help.

	- Now funcX changes name to Globus Compute, so sometimes you may see term Globus Compute instead of funcX in the funcX document, but they actually refers to the same thing.

Start the Endpoint
-----------------

Before starting the funcX endpoint, you need to first change to a certain directory you want, which will be the root directory for funcX when accessing your file system or writing output files. Please select that root directory carefully. When you are in your desired directory, run the following command by replacing ``<ENDPOINT_NAME>`` with your endpoint name to start the funcX endpoint.

.. code-block:: console

	funcx-endpoint start <ENDPOINT_NAME>

.. note::

	If you want to change the funcX root directory or change the configuration file, you should first stop the endpoint by running ``funcx-endpoint stop <ENDPOINT_NAME>`` in any directory and then start it again by ``running funcx-endpoint start <ENDPOINT_NAME>`` in the desired directory.

Get your Endpoint Id
-----------------

The following command will print the id of your created endpoint.

.. code-block:: console

	funcx-endpoint list


Run A Simple Test
-----------------

You can create a python script (e.g. ``test.py``) by copying the following codes to test if you have successfully set up a funcX endpoint. You need to put your own endpoint id into the script, and you should see the printed result computed by your endpoint.

.. code-block:: python
    :linenos:

	from funcx import FuncXExecutor

	def double(x):
    		return x * 2

	endpoint_id = '' #YOUR-ENDPOINT-ID
	with FuncXExecutor(endpoint_id=endpoint_id) as fxe:
    		fut = fxe.submit(double, 7)
   		print(fut.result())
