# =============================================================
# modules/subdomain/variables.tf
# =============================================================

variable "account_id" {
  description = "ID de la cuenta de Cloudflare"
  type        = string
}

variable "script_name" {
  description = "Nombre del Worker que se habilita en workers.dev"
  type        = string
}
