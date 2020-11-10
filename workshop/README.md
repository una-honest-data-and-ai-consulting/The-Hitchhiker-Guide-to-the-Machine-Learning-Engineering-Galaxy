# Hands-on with AI-pipelines

In order to answer the question "How to deploy a model?" we need to understand how end users are going to interact with the predictions from our model.

There are multiple factors to consider when determining how to deploy a machine learning model:
- interactive or non-interactive use
- single record or batch
- synchronous or asynchronous
- real-time or near real-time or non-real-time

Today we will explore 2 types of model deployment:
- Offline serving – batch
- Online serving - near real-time

------
## Offline serving – batch

**Batch inference** is about running prediction jobs on schedule: once a week, once a day, once an hour.

**What to optimize**: throughput

**End user**: usually no direct interactions with a model. User interacts with the predictions stored in a data storage as a result of the batch jobs.

**Validation**: offline

-------

## Online serving - near real-time

Online inference is definitely more challenging than batch inference. Why? Due to the latency restrictions on our systems.

**Online inference** is about responding with a prediction to the request of the end user with a latency measured in miliseconds.

**What to optimize**: latency

**End user**: usually interacts with a model directly available through an API

**Validation**: offline and online via A/B testing

_______

## Where to go next?

- [Full Stack Deep Learning Deployment](https://fullstackdeeplearning.com/)
- [Fighting Machine Learning Technical Debt](https://matthewmcateer.me/blog/machine-learning-technical-debt/)
- [Monitoring ML models](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)
- [Model serving flavours](https://github.com/schmidtbri)
- [Productionizing NLP models](https://medium.com/modern-nlp/productionizing-nlp-models-9a2b8a0c7d14)

## Favourite open-source tools
- [miniconda](https://docs.conda.io/en/latest/miniconda.html) - Package, dependency and environment management for any language: Python, R,
Ruby, Scala, Java, JavaScript, C/ C++
- [DVC](https://dvc.org/) - Data versioning, Version control system for ML Projects
- [Pachyderm](https://www.pachyderm.com/) - Data lineage, e2e pipelines on k8s
- [mlflow](https://mlflow.org/) - Experiment tracking, Model registry, Conda based Projects
- [Seldon core](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/) - ML models serving as REST/GRPS microservices running on k8s
- [TensorFlow Extended](https://www.tensorflow.org/tfx) - e2e production ML pipelines