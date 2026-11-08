# =============================================================
# outputs.tf (raíz)
# Salidas expuestas desde los módulos
# =============================================================

output "worker_script_name" {
  description = "Nombre del Worker desplegado"
  value       = module.worker.script_name
}

output "worker_dev_enabled" {
  description = "Worker habilitado en workers.dev (responde con GET)"
  value       = module.subdomain.enabled
}

output "d1_database_id" {
  description = "ID de la base de datos D1 creada"
  value       = module.d1.database_id
}
