# Install Docker Desktop

1. Download [docker-desktop](https://www.docker.com/products/docker-desktop/)
2. Go to **docker-desktop** => **Preferences**
3. Check ✅ **Enable Kubernetes**

![enable kubenetes](/assets/images/docker-desktop.png)

## Install Ingress-Nginx

```shell
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```
