# =============================================================
# modules/worker/versions.tf
# El source del provider se declara en cada módulo; la versión
# se controla en la raíz (versions.tf)
# =============================================================

terraform {
  required_providers {
    cloudflare = {
      source = "cloudflare/cloudflare"
    }
  }
}
