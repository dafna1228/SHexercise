# SHexercise
## Includes:

### In charts- helm charts for:
1. A deployment that runs the container for the app (dafna/fibi)
2. A service for the deployment
3. An ingress to route the requests to the service
4. a horizonal autoscaler

### In K8S: a yaml to deploy the self hosted runners. to set self hosted runners, run:
```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.3/cert-manager.crds.yaml
helm repo add jetstack https://charts.jetstack.io
helm install my-release -n arc-systems --version v1.12.3 jetstack/cert-manager
kubectl create secret generic controller-manager -n arc-systems --from-literal=github_token='${PAT}'
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm repo update
helm upgrade --install -n arc-systems --wait actions-runner-controller actions-runner-controller/actions-runner-controller --set syncPeriod=1m
kubectl create -f .\K8S\self_hosted_runners.yml -n arc-systems
```

### In python:
1. the main.py python code given to me + implementation of the fibonacci function + logging + healthcheck endpoint
2. logger.py containing the logger class (implemented json logs for easier parsing)
3. tests.py for unit tests for the fibonacci function
4. the dockerfile that builds the image

### In ./github/workflows: a Github Actions  CI/CD process that:
1. Tests the python fibonacci functionality
2. Builds the image with it
3. Runs the image to check container health
4. Uploads it to dockerhub
5. helm upgrades the local kubernetes deployment with the charts. (they're configured to always pull the new image.)

## What I would add:
At this point, my laptop has less than 5 free GB and was very laggy and unreactive, so I chose to stop, being pretty satisfied with what I did. If I had more time and resources, I would add:
- Current flow runs on push to main branch, but it's not good practice. I'd have a flow for pushing to branches that does linting, python tests
- There's no staging/ testing environment. On branch push, I'd like to auto create a small testing env for that branch, then on PR to master deploys to staging environment, then after approvals, deploys to production
- Given multiple kubernetes environments, I'd probably handle the deployment with ArgoCD instead of just 'helm upgrade' 
- There's logs, but no monitoring- I'd add a log collector + tracing + metrics, probably with OpenTelemetry, collect all this data and create dashboards and alerts for it
- Some minor things are not fully automated, like kubernetes setup, namespace creation, etc, so I would manage it as code with terraform (if it was running in the cloud)

## Interview
Please see [INTERVIEW.md](INTERVIEW.md) for instructions.
