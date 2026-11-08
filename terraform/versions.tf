# =============================================================
# versions.tf
# Configuración de Terraform y del provider de Cloudflare
# =============================================================

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 5.28"
    }
  }
}

provider "cloudflare" {
  api_token = var.api_token
}
