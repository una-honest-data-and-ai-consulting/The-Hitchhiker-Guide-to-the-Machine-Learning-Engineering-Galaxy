# Hands-on with ML serving pipelines

In order to answer the question "How to deploy a model?" we need to understand how end users are going to interact with our model:
- interactive or non-interactive
- single record or batch
- synchronous or asynchronous
- real-time or non-real-time

Today we will explore 3 flavours of model deployments:
- Batch serving
- Online serving near real-time
- Real-time serving with embedded model

Each flavour has its own dedicated repository.

------
## Batch serving

**Batch inference** is about using data distributed processing infrastructure to carry out inference asynchronously on a large number of instances at once.


**What to optimize**: throughput, not latency-sensitive

**End user**: usually no direct interactions with a model. User interacts with the predictions stored in a data storage as a result of the batch jobs.

**Validation**: offline


To [GitHub repo](https://github.com/EzheZhezhe/ML-Batch-Serving)

-------

## Online serving near real-time

Online inference is definitely more challenging than batch inference. Why? Due to the latency restrictions on our systems.

**Online inference** is about responding with a prediction to the request of the end user with a low latency.

**What to optimize**: latency

**End user**: usually interacts with a model directly available through an API

**Validation**: offline and online via A/B testing

To [GitHub repo](https://github.com/EzheZhezhe/ML-Online-Near-real-time-Serving)

_______

## Real-time serving with embedded model

**Real-time serving with embedded model** is about distributed event-at-a-time processing with millisecond latency and high throughput.

**What to optimize**: latency and throughput

**End user**: usually no direct interactions with a model

**Validation**: offline and online via A/B testing

To [GitHub repo](https://github.com/EzheZhezhe/ML-Real-time-serving-with-Embedded-Model)
_______

## Favourite open-source tools
- [miniconda](https://docs.conda.io/en/latest/miniconda.html) - Package, dependency and environment management for any language: Python, R,
Ruby, Scala, Java, JavaScript, C/ C++
- [DVC](https://dvc.org/) - Data versioning, Version control system for ML Projects
- [Pachyderm](https://www.pachyderm.com/) - Data lineage, e2e pipelines on k8s
- [mlflow](https://mlflow.org/) - Experiment tracking, Model registry, Conda based Projects
- [Seldon core](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/) - ML models serving as REST/GRPS microservices running on k8s
- [TensorFlow Extended](https://www.tensorflow.org/tfx) - e2e production ML pipelines

---

## Where to go next?

- [MLOps](https://ml-ops.org/)
- [Awesome MLOps](https://github.com/visenger/awesome-mlops)
- [Awseome Production ML](https://github.com/EthicalML/awesome-production-machine-learning)
- [Fighting Machine Learning Technical Debt](https://matthewmcateer.me/blog/machine-learning-technical-debt/)
- [Model serving flavours](https://github.com/schmidtbri)
- [Monitoring ML models](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)
