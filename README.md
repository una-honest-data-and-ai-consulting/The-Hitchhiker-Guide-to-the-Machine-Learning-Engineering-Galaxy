# The Hitchhiker's Guide to the Machine Learning Engineering Galaxy

A presentation on how to start with MLOps for [ML Conf EU 2020](https://mlconf.eu/).

Updated for LINKIT Virtual Roadtrip "Defrost Your Data".

## Intro
Are you a Software Engineer who got tasked to deploy a machine learning model for the first time in your life? Are you wondering what steps to take and how AI-powered software is different from traditional software? Then it is the right presentation to attend.

The internet offers thousands of articles and free of charge courses, showing how it is easy to train and deploy a simple ML model. At the same time in reality it is difficult to integrate a real model into the current infrastructure, debug, test, deploy, and monitor it properly. In this presentation, I will guide you through this process by sharing tips, tricks, and favorite open source tools that will make your life much easier. So, at the end of the presentation, you will know where to start your deployment journey, what tools to use, and what questions to ask.

## Table of contents

- Traditional vs AI-powered software
- MLOps
- ML serving pipelines

## Presentation level
Great for software engineers who got tasked with ML model deployment for the first time. No ML knowledge is assumed.

## Prerequisites 
No Machine Learning background is assumed.

## How to use
1. Start with this [presentation](presentation/MLOps_presentation.pdf).
2. Continue with ML serving pipelines part

---

## ML serving pipelines

In order to answer the question "How to deploy a model?" we need to understand how end users are going to interact with our model:
- interactive or non-interactive
- single record or batch
- synchronous or asynchronous
- real-time or non-real-time

Today we will explore 3 flavours of model deployments:
- Batch serving
- Online serving (near real-time)
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

## Online serving (near real-time)

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
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) - Package, dependency and environment management for any language: Python, R,
Ruby, Scala, Java, JavaScript, C/ C++
- [MLflow](https://mlflow.org/) - Experiment tracking, Model registry, Conda based Projects
- [DVC](https://dvc.org/) - Data versioning, Version control system for ML Projects
- [Pachyderm](https://www.pachyderm.com/) - Data lineage, e2e pipelines on k8s
- [Seldon core](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/) - ML models serving as REST/GRPS microservices running on k8s
- [TensorFlow Extended](https://www.tensorflow.org/tfx) - e2e production ML pipelines

---

## Where to go next?

- [MLOps](https://ml-ops.org/)
- [Awesome MLOps](https://github.com/visenger/awesome-mlops)
- [Awesome Production ML](https://github.com/EthicalML/awesome-production-machine-learning)
- [Fighting Machine Learning Technical Debt](https://matthewmcateer.me/blog/machine-learning-technical-debt/)
- [Monitoring ML models](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)

