# Hands-on with AI-pipelines

In order to answer the question "How to deploy a model?" we need to understand how end users are going to interact with the predictions from our model.

There are multiple factors to consider when determining how to deploy a machine learning model:
- frequency of predictions
- how predictions will be generated (single request or batch)
- which applications will use our model
- latency requrements

Today we will explore 2 types of model deployment:
- Offline serving – batch
- Online serving - near real-time

------
## Offline serving – batch

**Batch inference** is about running prediction jobs on schedule: once a week, once a day, once an hour.

**What to optimize**: throughput

**End user**: usually no direct interactions with a model. User interacts with the predictions stored in a data storage as a result of the batch jobs.

-------

## Online serving - near real-time

Online inference is definitely more challenging than batch inference. Why? Due to the latency restrictions on our systems.

**Online inference** is about responding with a prediction to the request of the end user with a latency measured in miliseconds.

**What to optimize**: latency

**End user**: usually directly interacts with a model exposed via API.
