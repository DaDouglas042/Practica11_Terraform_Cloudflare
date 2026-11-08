# =============================================================
# modules/d1/variables.tf
# =============================================================

variable "account_id" {
  description = "ID de la cuenta de Cloudflare"
  type        = string
}

variable "d1_database_name" {
  description = "Nombre de la base de datos D1"
  type        = string
}
