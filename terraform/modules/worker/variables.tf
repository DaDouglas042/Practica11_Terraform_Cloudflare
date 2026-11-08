# =============================================================
# modules/worker/variables.tf
# =============================================================

variable "account_id" {
  description = "ID de la cuenta de Cloudflare"
  type        = string
}

variable "worker_name" {
  description = "Nombre del Cloudflare Worker"
  type        = string
}
