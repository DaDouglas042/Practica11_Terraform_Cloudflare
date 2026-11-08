# =============================================================
# modules/worker/main.tf
# Cloudflare Worker que responde a peticiones GET
# =============================================================

resource "cloudflare_workers_script" "worker" {
  account_id  = var.account_id
  script_name = var.worker_name

  content = <<-EOT
    addEventListener("fetch", (event) => {
      event.respondWith(handleRequest(event.request));
    });

    async function handleRequest(request) {
      const url = new URL(request.url);

      // Responde a cualquier peticion GET
      if (request.method === "GET") {
        return new Response(
          JSON.stringify({
            message: "Hola desde Terraform + Cloudflare Worker",
            method: request.method,
            path: url.pathname,
            status: 200,
            timestamp: new Date().toISOString(),
          }),
          {
            status: 200,
            headers: { "content-type": "application/json; charset=UTF-8" },
          }
        );
      }

      // Cualquier otro metodo no esta permitido
      return new Response("Metodo no permitido", { status: 405 });
    }
  EOT
}
