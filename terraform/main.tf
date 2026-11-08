# =============================================================
# main.tf (raíz)
# Invocación de los módulos de la Práctica 11
# =============================================================

module "worker" {
  source = "./modules/worker"

  account_id  = var.account_id
  worker_name = var.worker_name
}

module "d1" {
  source = "./modules/d1"

  account_id        = var.account_id
  d1_database_name = var.d1_database_name
}

module "subdomain" {
  source = "./modules/subdomain"

  account_id  = var.account_id
  script_name = module.worker.script_name
}
