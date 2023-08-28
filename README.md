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

## Interview
Please see [INTERVIEW.md](INTERVIEW.md) for instructions.
