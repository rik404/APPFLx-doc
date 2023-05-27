# Start Federated Learning Experiments

This page describes how the FL group (federation) leader can start an FL experiment on the web application.

1. Log in to the [web application](https://appflx.link)  by following the instructions. @ShellyRiver: link the signin page.

2. You will see a dashboard after logging in. The dashboard lists your **Federations** and your **Sites**. Specifically, federation refers to the FL group that you created and you are the group leader who can start FL experiments and access the experiment results. Site refers to the FL group that you are a member of. The federation leader is also a site of his own federation.

3. Click **Create New Experiment** button next to the federation for which you want to start the experiment. This will lead you to the **Federation Configuration** page.

4. **Client Endpoints** at the top of the page shows the status of client (site) funcX endpoints. Click the icon to see the details of the endpoint status. Only clients (sites) with active endpoint can join the FL experiment. You can contact the client via email by clicking the email icon if the client endpoint is not active.

5. For **Federation Algorithm**, we support the following federated learning algorithms. Choose one algorithm that you want to use.

@ShellyRiver: The following should be a list

[Federated Average](https://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf): Communication-Efficient Learning of Deep Networks from Decentralized Data

[Federated Average Momentum](https://arxiv.org/pdf/1909.06335.pdf): Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification

[Federated Adagrad/Adam/Yogi](https://arxiv.org/pdf/2003.00295.pdf): Adaptive Federated Optimization

[Federated Asynchronous](https://arxiv.org/pdf/1903.03934.pdf): Asynchronous Federated Optimization

6. For **Experiment Name**, please provide a name of your choice for this FL experiment.

7. For **Server Training Epochs**, enter the number of global aggregations for the FL experiment.

8. For **Client Training Epochs**, enter the number of local training epochs for each client (site) before sending model back to the server.

9. For **Server Validation Set for Benchmarking**, select **None** if you are doing your own experiment. Select **MNIST** only if your FL group is using the provided MNIST dataloader for testing, and this will enable the orchestration server to download the MNIST dataset and perform server validation.

10. **Privacy Budget**, **Clip Value** and **Clip Norm** are used for preserving privacy, enter 0 to disable this.

11. Upload the training model architecture by either selecting a **Template Model**, uploading a **Custom Model** or choose a custom model by **Uploading from Github**.

12. For **Client Optimizer**, choose either SGD or Adam, and specify the local learning rate of each client in **Client Learning Rate**. For different client local training round, you can choose to decrease the learning rate by entering a value between 0 and 1 in **Client Learning Rate Decay**. 

13. For **Client Weights**, **Proportional to Sample Size** means applying different weights to client local models during global aggregation by calculating the weights proportional to client sample size, and **Equal for All Clients** means applying the same weights to all client local models.

14. After carefully choosing all configurations and hyperparameters for the FL experiment, you can start the experiment by clicking **Start**. Then the web application will launch an orchestration server which trains a federated learning model by collaborating with all active client endpoints.