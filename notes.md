# Notes

This is where I'll record my thoughts and learnings. This repository seems like a lot is done for you, but in case you haven't figured it out by now, I have preferences. I'll create a kind of master TODO list here, and I'll add daily notes below. Be aware that this TODO list will change drastically as I progress.

## TODO
* [ ] Run the data engineering stuff on my data
* [ ] Get everything running via Docker Compose for local dev
* [ ] Set up OpenStack on my server to treat it like a cloud
* [ ] Kubernetes-ify everything that's not on Kubernetes
* [ ] Install [CometML/Opik on Kubernetes](https://www.comet.com/docs/opik/self-host/kubernetes/)
* [ ] Set up a self-hosted model registry instead of Hugging Face

### Done
* [x] Get things up and running locally with uv

## Logs

### 2025-09-28

#### Chapter 2

Learned about Poe the Poet. I'd been hoping for a task runner in the Python ecosystem like NPM can do. Seems tightly coupled to Poetry and uv, but I'm okay with it for now.

ZenML seems really cool, but the self-hosted versus cloud offerings have the fatal catch that all these systems have: RBAC requires their cloud offering. To me, this is a deal-breaker if you want a system like this for sensitive things like medicine. I've run into similar frustrations with Prefect, though we just threw Keycloak in front of it. I was working on completely blocking access to Prefect and having another system only be able to trigger pipelines, but I ran out of time for that.

The frustrating thing about all these tools is that they're missing some integrations and paywall some features. I understand that people need to make money, but I'd love to have an open-source, completely pluggable system for all components. I want a ZenML with RBAC that can hook up to some identity platform or that can defer RBAC to another system like Keycloak. I understand that's a hard problem to solve, but call me greedy, I guess. I suppose putting interfaces with RBAC and whatnot in front of these kinds of systems is the way to go, but it just feels like it should be unnecessary. If I actually had enough free time, I'd just build my own.

They keep talking about the stacks part of ZenML and how it was a deciding factor in their tool choice. I'm not yet sure I believe them, but maybe I should try it be re-instating the AWS bits and adding my OpenStack things as a stack in ZenML.

CometML/Opik look cool. I'm looking forward to learning about and playing with those.

I'm not using SageMaker. AWS has really nice systems and some of the best customer service I've ever experienced, but I hate Amazon as a company. I think building my own Kubernetes-based training system will be a good experience, anyway.

### Chapter 3

Decent data architecture so far. I probably would have done it the same.

But... Maybe it's because I've been out of the data game for a minute or because everyone does things on commodity hardware these days, but I don't get why everyone says systems like MongoDB or PostgreSQL can't handle millions of records. I literally just led a team to do that over the past few months on PostgreSQL, and it performs fine. Hell, we're not even using the columnar plugins that we should be using because GCP doesn't support them. Maybe there's something I don't know about, yet. We haven't used these systems to supply training data quite yet; they're more focused on analytics. I'm sure there's a good reason that I'll learn soon enough. I just don't want to pay for Snowflake or BigQuery, though I have heard that they can be cheap if you're smart about it.

I'm nearly out of time for my current session. I'm hoping I'll have some time after dinner to actually write some damn code.
