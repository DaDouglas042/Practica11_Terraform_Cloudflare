# =============================================================
# variables.tf
# Variables requeridas para el proyecto
# =============================================================

variable "account_id" {
  description = "ID de la cuenta de Cloudflare"
  type        = string
}

variable "api_token" {
  description = "API token de Cloudflare con permisos D1 Edit y Workers Edit"
  type        = string
  sensitive   = true
}

variable "worker_name" {
  description = "Nombre del Cloudflare Worker y del subdominio workers.dev"
  type        = string
}

variable "d1_database_name" {
  description = "Nombre de la base de datos D1"
  type        = string
}
