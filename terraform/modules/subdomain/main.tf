# =============================================================
# modules/subdomain/main.tf
# Habilita el Worker en el subdominio workers.dev de la cuenta
# =============================================================

resource "cloudflare_workers_script_subdomain" "subdomain" {
  account_id  = var.account_id
  script_name = var.script_name
  enabled     = true
}
