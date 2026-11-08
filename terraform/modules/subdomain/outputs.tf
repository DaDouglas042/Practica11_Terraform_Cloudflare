# =============================================================
# modules/subdomain/outputs.tf
# =============================================================

output "enabled" {
  description = "Worker habilitado en workers.dev"
  value       = cloudflare_workers_script_subdomain.subdomain.enabled
}

output "script_name" {
  description = "Worker asociado al subdominio"
  value       = cloudflare_workers_script_subdomain.subdomain.script_name
}
