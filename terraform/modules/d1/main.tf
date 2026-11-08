# =============================================================
# modules/d1/main.tf
# Base de datos Cloudflare D1
# =============================================================

resource "cloudflare_d1_database" "db" {
  account_id = var.account_id
  name       = var.d1_database_name
}
