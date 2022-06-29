# Vault

1. Create namespace

```shell
kubectl create namespace vault
```

2. Helm repo

```shell
helm repo add hashicorp https://helm.releases.hashicorp.com
helm search repo hashicorp/vault
```

3. Install the latest version of the Vault Helm chart with Integrated Storage

```shell
cat > helm-vault-raft-values.yml <<EOF
server:
  affinity: ""
  ha:
    enabled: true
    raft:
      enabled: true
EOF

helm install vault hashicorp/vault --values helm-vault-raft-values.yml
```

4. Unseal

```shell
jq -r ".unseal_keys_b64[]" cluster-keys.json
VAULT_UNSEAL_KEY=$(jq -r ".unseal_keys_b64[]" cluster-keys.json)
kubectl exec vault-0 -n vault -- vault operator unseal $VAULT_UNSEAL_KEY
kubectl exec -ti vault-1 -n vault -- vault operator raft join http://vault-0.vault-internal:8200
kubectl exec -ti vault-2 -n vault -- vault operator raft join http://vault-0.vault-internal:8200
kubectl exec -ti vault-1 -n vault -- vault operator unseal $VAULT_UNSEAL_KEY
kubectl exec -ti vault-2 -n vault -- vault operator unseal $VAULT_UNSEAL_KEY
```
