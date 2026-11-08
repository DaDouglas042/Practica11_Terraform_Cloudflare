# Práctica 11 - Terraform con Cloudflare

Proyecto de Infrastructure as Code (IaC) con **Terraform** y el provider de
**Cloudflare**. Despliega tres recursos mediante módulos:

| Módulo | Recurso | Descripción |
|--------|---------|-------------|
| `modules/worker` | `cloudflare_workers_script` | Worker que responde a peticiones **GET** con JSON |
| `modules/d1` | `cloudflare_d1_database` | Base de datos D1 |
| `modules/subdomain` | `cloudflare_workers_script_subdomain` | Habilita el Worker en workers.dev |

## Estructura

```
terraform/
├── main.tf          # Raíz: invoca los 3 módulos
├── versions.tf      # Provider cloudflare ~> 5.28
├── variables.tf     # account_id, api_token, worker_name, d1_database_name
├── outputs.tf       # Salidas expuestas desde los módulos
└── modules/
    ├── worker/
    ├── d1/
    └── subdomain/
```

## Uso

```bash
terraform init
terraform plan
terraform apply -auto-approve
# Prueba del Worker:
curl -i https://<worker_name>.<subdominio>.workers.dev
terraform destroy -auto-approve
```

## Variables

- `account_id` — ID de la cuenta de Cloudflare
- `api_token` — API token (sensitive) con permisos *Workers Scripts Edit* y *D1 Edit*
- `worker_name` — nombre del Worker
- `d1_database_name` — nombre de la base de datos D1

> Las variables sensibles se configuran en **Terraform Cloud** (workspace
> variables) o en `terraform.tfvars` (no versionado, ver `.gitignore`).
