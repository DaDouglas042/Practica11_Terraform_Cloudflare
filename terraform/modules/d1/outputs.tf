# =============================================================
# modules/d1/outputs.tf
# =============================================================

output "database_id" {
  description = "ID de la base de datos D1"
  value       = cloudflare_d1_database.db.id
}

output "uuid" {
  description = "UUID de la base de datos D1"
  value       = cloudflare_d1_database.db.uuid
}
