# =============================================================
# modules/worker/outputs.tf
# =============================================================

output "script_name" {
  description = "Nombre del Worker desplegado"
  value       = cloudflare_workers_script.worker.script_name
}

output "id" {
  description = "ID del Worker en Cloudflare"
  value       = cloudflare_workers_script.worker.id
}
