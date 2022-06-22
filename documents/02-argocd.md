# How to install ArgoCD

1. Install Argo CD

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

2. Download Argo CD CLI

```shell
brew install argocd
```

3. Add git repo credential with key

```shell
argocd repo add <URL_GTI> \
--name <NAME> \
--ssh-private-key-path=<KEY_PATH>
```

4. Apply app

```shell
kubectl create -f deployment
```
