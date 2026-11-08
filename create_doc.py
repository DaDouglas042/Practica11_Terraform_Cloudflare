# -*- coding: utf-8 -*-
"""Genera el documento de la Práctica 11 - Terraform con Cloudflare."""
import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(BASE, 'capturas')

AZUL = RGBColor(0, 51, 102)
GRIS = RGBColor(0x59, 0x59, 0x59)

doc = Document()

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)


def code(text, size=8.5):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Consolas'
    run.font.size = Pt(size)
    return p


def caption(text):
    c = doc.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = c.add_run(text)
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = GRIS


def image(name, width=5.9):
    path = os.path.join(CAP, name)
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Inches(width))


# ---------- Encabezado ----------
logo = os.path.join(CAP, 'logo_iteso.jpeg')
if os.path.exists(logo):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(logo, width=Inches(1.1))

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('PRÁCTICA 11 - TERRAFORM CON CLOUDFLARE')
run.bold = True
run.font.size = Pt(18)
run.font.color.rgb = AZUL

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Infrastructure as Code: Worker (GET), base D1 y subdominio')
run.font.size = Pt(12)
run.font.color.rgb = AZUL

info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = info.add_run(
    'Alumno: Francisco Delgado Carrasco\n'
    'Matrícula: [Tu matrícula]\n'
    'Fecha: 1 de Noviembre de 2026\n'
    'Materia: IPDC'
)
run.font.size = Pt(11)

# ---------- 1. Objetivo ----------
doc.add_heading('1. Objetivo', level=1)
doc.add_paragraph(
    'Crear un proyecto en Terraform que despliegue recursos de Cloudflare mediante código: un '
    'Worker que responde a peticiones GET, una base de datos D1 y el subdominio workers.dev del '
    'script, usando el provider de Cloudflare y las variables solicitadas. Se ejecutó el ciclo '
    'completo: terraform plan, terraform apply y, al finalizar, terraform destroy para dejar todo '
    'limpio.'
)

# ---------- 2. Estructura ----------
doc.add_heading('2. Estructura del proyecto', level=1)
code(
    'Practica11_Terraform_Cloudflare/\n'
    '└── terraform/\n'
    '    ├── versions.tf      # Provider de Cloudflare\n'
    '    ├── variables.tf     # Variables: account_id, api_token, worker_name, d1_database_name\n'
    '    ├── worker.tf        # Recurso del Worker (responde GET)\n'
    '    ├── d1.tf            # Recurso de la base de datos D1\n'
    '    ├── subdomain.tf     # Recurso del subdominio workers.dev\n'
    '    ├── outputs.tf       # Salidas del proyecto\n'
    '    └── .gitignore       # Excluye tfvars, state y .terraform'
)

# ---------- 3. Archivos ----------
doc.add_heading('3. Archivos de configuración', level=1)

doc.add_heading('3.1 versions.tf (provider de Cloudflare)', level=2)
code(
    'terraform {\n'
    '  required_version = ">= 1.5.0"\n'
    '  required_providers {\n'
    '    cloudflare = {\n'
    '      source  = "cloudflare/cloudflare"\n'
    '      version = "~> 5.28"\n'
    '    }\n'
    '  }\n'
    '}\n'
    '\n'
    'provider "cloudflare" {\n'
    '  api_token = var.api_token\n'
    '}'
)

doc.add_heading('3.2 variables.tf', level=2)
code(
    'variable "account_id"        { type = string }\n'
    'variable "api_token"         { type = string, sensitive = true }\n'
    'variable "worker_name"       { type = string }\n'
    'variable "d1_database_name"  { type = string }'
)

doc.add_heading('3.3 worker.tf (Worker que responde GET)', level=2)
code(
    'resource "cloudflare_workers_script" "worker" {\n'
    '  account_id  = var.account_id\n'
    '  script_name = var.worker_name\n'
    '\n'
    '  content = <<-EOT\n'
    '    addEventListener("fetch", (event) => {\n'
    '      event.respondWith(handleRequest(event.request));\n'
    '    });\n'
    '\n'
    '    async function handleRequest(request) {\n'
    '      const url = new URL(request.url);\n'
    '      // Responde a cualquier peticion GET\n'
    '      if (request.method === "GET") {\n'
    '        return new Response(\n'
    '          JSON.stringify({\n'
    '            message: "Hola desde Terraform + Cloudflare Worker",\n'
    '            method: request.method,\n'
    '            path: url.pathname,\n'
    '            status: 200,\n'
    '            timestamp: new Date().toISOString(),\n'
    '          }),\n'
    '          { status: 200,\n'
    '            headers: { "content-type": "application/json; charset=UTF-8" } }\n'
    '        );\n'
    '      }\n'
    '      return new Response("Metodo no permitido", { status: 405 });\n'
    '    }\n'
    '  EOT\n'
    '}'
)

doc.add_heading('3.4 d1.tf y subdomain.tf', level=2)
code(
    'resource "cloudflare_d1_database" "db" {\n'
    '  account_id = var.account_id\n'
    '  name       = var.d1_database_name\n'
    '}\n'
    '\n'
    'resource "cloudflare_workers_script_subdomain" "subdomain" {\n'
    '  account_id  = var.account_id\n'
    '  script_name = cloudflare_workers_script.worker.script_name\n'
    '  enabled     = true\n'
    '}'
)

# ---------- 4. Variables ----------
doc.add_heading('4. Variables utilizadas', level=1)
table = doc.add_table(rows=1, cols=3)
table.style = 'Light Grid Accent 1'
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = table.rows[0].cells
for i, t in enumerate(['Variable', 'Descripción', 'Valor']):
    hdr[i].text = t
    hdr[i].paragraphs[0].runs[0].bold = True

rows = [
    ('account_id', 'ID de la cuenta de Cloudflare', '444a559ce6a687ee1f3ac34dd5f25b2c'),
    ('api_token', 'Token con permisos Workers Scripts Edit y D1 Edit (marcada como sensitive: Terraform la oculta en las salidas)', '(valor oculto)'),
    ('worker_name', 'Nombre del Worker y del subdominio', 'tf-practica11-worker'),
    ('d1_database_name', 'Nombre de la base de datos D1', 'practica11_db'),
]
for r in rows:
    cells = table.add_row().cells
    for i, t in enumerate(r):
        cells[i].text = t
        for para in cells[i].paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)

# ---------- 5. Ejecución ----------
doc.add_heading('5. Ejecución del proyecto', level=1)
doc.add_paragraph(
    'Se ejecutó terraform init (descarga el provider cloudflare v5.28.1) y terraform validate '
    '(configuración válida) antes de planificar.'
)

doc.add_heading('5.1 terraform plan', level=2)
doc.add_paragraph(
    'El plan muestra los 3 recursos que se crearán (Worker, D1 y subdominio) y los outputs '
    'resultantes:'
)
image('01_terraform_plan_parte1.png')
caption('Captura 1. terraform plan (parte 1): recursos cloudflare_d1_database y cloudflare_workers_script que serán creados.')
image('02_terraform_plan_parte2.png')
caption('Captura 2. terraform plan (parte 2): recurso del subdominio y resumen "Plan: 3 to add, 0 to change, 0 to destroy".')

doc.add_heading('5.2 terraform apply', level=2)
doc.add_paragraph(
    'Se ejecutó terraform apply -auto-approve. Los 3 recursos se crearon correctamente en '
    'Cloudflare y se mostraron los outputs (id de la base D1, subdominio habilitado y nombre del '
    'Worker):'
)
image('03_terraform_apply.png')
caption('Captura 3. terraform apply: "Apply complete! Resources: 3 added, 0 changed, 0 destroyed" con los outputs del proyecto.')

doc.add_heading('5.3 Prueba del Worker (respuesta GET)', level=2)
doc.add_paragraph(
    'Con el Worker desplegado y el subdominio habilitado, se hizo una petición GET a '
    'https://tf-practica11-worker.frankdelgado455.workers.dev con curl -i:'
)
image('04_worker_get_respuesta.png')
caption('Captura 4. Respuesta HTTP/1.1 200 OK con JSON: "message": "Hola desde Terraform + Cloudflare Worker", "method": "GET".')

doc.add_heading('5.4 terraform destroy', level=2)
doc.add_paragraph(
    'Finalmente se destruyó todo lo creado con terraform destroy -auto-approve:'
)
image('05_terraform_destroy.png')
caption('Captura 5. terraform destroy: "Destroy complete! Resources: 3 destroyed" - los 3 recursos fueron eliminados.')

# ---------- 6. Resultados ----------
doc.add_heading('6. Resultados', level=1)
for t in [
    'Se creó el proyecto completo con el provider de Cloudflare en versions.tf y las 4 variables solicitadas.',
    'terraform plan: 3 recursos a crear (Worker, D1 y subdominio).',
    'terraform apply: 3 recursos creados exitosamente (Apply complete! Resources: 3 added).',
    'El Worker respondió una petición GET con HTTP 200 y un mensaje en JSON.',
    'terraform destroy: 3 recursos destruidos; terraform state list quedó vacío (infraestructura limpia, sin costos residuales).',
]:
    doc.add_paragraph(t, style='List Bullet')

out = os.path.join(BASE, 'Practica11_Terraform_Cloudflare_FranciscoDelgado.docx')
doc.save(out)
print('OK:', out)
