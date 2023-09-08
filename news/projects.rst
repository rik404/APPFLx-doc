Active Projects
===============

**1. Federated Fine-Tuning of Large Language Models such as LLaMa using Parameter-Efficient Fine-Tuning (PEFT) Methods**

**Abstract:**

Federated learning (FL) is a machine learning paradigm where multiple clients collaboratively train a machine learning model under the orchestration of a central server by sharing the local model trained on the local data. As FL enables training a model by utilizing datasets from multiple clients without explicitly sharing the data, it becomes a promising approach to train a robust and generalized model in scenarios where local datasets cannot be shared due to data privacy, such as in healthcare, smart grid, and insurance domains. Our objective is to fine-tune a Large Language Model (LLM), such as `LLaMa <https://arxiv.org/pdf/2302.13971.pdf>`_, using federated learning techniques. One significant challenge is the large size of LLMs, typically on the order of gigabytes, which makes the process of federated learning both resource-intensive and costly due to the model transfer requirements. To mitigate this, we propose leveraging Parameter-Efficient Fine-Tuning (PEFT) techniques, such as `LoRA <https://arxiv.org/pdf/2106.09685.pdf>`_. PEFT enables efficient adaptation of pre-trained language models to various applications without fine-tuning all the model's parameters. PEFT methods only fine-tune a small number of (extra) model parameters, thereby greatly decreasing the computational and storage costs. In this project, we want to investigate how to utilize PEFT to reduce the transferred model size and finally make federated fine-tuning of LLM feasible and efficient.

**Requirements:**

- Familiar with Python programming and have basic machine learning knowledge.

- Familiar with PyTorch and HuggingFace Transformer libraries is preferred.

**Contact**: Zilinghan Li (zl52@illinois.edu)


**2. Genome-scale Language Models Fine-Tuning using Federated Learning**

