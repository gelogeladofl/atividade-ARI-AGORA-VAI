from http.server import HTTPServer, BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        # Responde com sucesso (OK)
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Servidor WEB funcionando".encode('utf-8'))

    def do_POST(self):
       
        tamanho = int(self.headers.get('Content-Length', 0))
        
        if tamanho > 0:
            dados = self.rfile.read(tamanho)
            print(f"Dados recebidos: {dados.decode('utf-8')}")
        else:
            print("Nenhum dado recebido no corpo do POST.")

        
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Post recebido com sucesso!".encode('utf-8'))


endereco = ("0.0.0.0", 8000)
httpd = HTTPServer(endereco, Servidor)

print(f"Servidor rodando em http://localhost:{endereco[1]}")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServidor finalizado pelo usuário.")
    httpd.server_close()