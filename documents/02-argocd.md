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
