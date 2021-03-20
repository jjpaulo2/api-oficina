"""
Arquivo com o método principal que sobe o servidor
`uvicorn` e inicia a aplicação.
"""
import uvicorn


def run_server():
    """
    Função que inicia o servidor da aplicação utilizando
    a biblioteca `uvicorn`
    """
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info')


if __name__ == '__main__':
    run_server()