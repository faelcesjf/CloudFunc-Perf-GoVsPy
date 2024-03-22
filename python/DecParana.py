import re
import requests
import logging


class DecParana:
    def __init__(self, login, senha):
        self.session = requests.session()
        self.empresa = {'login': login, 'senha': senha}

    def dec_parana(self):
        try:
            self.get_formulario_login()
            self.post_dados_acesso()
            response = self.get_caixa_postal()
            empresas = self.listar_empresas(response)

            for empresa in empresas:
                mensagens_empresa = self.get_mensagens(empresa)

                if mensagens_empresa:
                    status = self.verificar_situacao_leitura(mensagens_empresa)
                    if status == 'mensagem lida':
                        conteudo = self.get_conteudo_mensagem(mensagens_empresa)
                        return conteudo

                return mensagens_empresa

        except Exception as ex:
            logging.error(ex, 'DEC Parana')
            raise Exception

    def get_formulario_login(self):
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Referer': 'https://www.fazenda.pr.gov.br/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            response = self.session.get('https://receita.pr.gov.br/login', headers=headers)
            return response
        except Exception as ex:
            logging.error(ex, 'get formulario login')
            raise Exception

    def post_dados_acesso(self):
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://receita.pr.gov.br',
                'Referer': 'https://receita.pr.gov.br/login',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            data = {
                'cpfusuario': self.empresa['login'],
                'senha': self.empresa['senha'],
            }

            response = self.session.post('https://receita.pr.gov.br/login', headers=headers, data=data)
            return response
        except Exception as ex:
            logging.error(ex, 'post dados acesso')
            raise Exception

    def get_caixa_postal(self):
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Referer': 'https://receita.pr.gov.br/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            response = self.session.get('https://receita.pr.gov.br/caixa_postal', headers=headers)
            return response
        except Exception as ex:
            logging.error(ex, 'get caixa postal')
            raise Exception

    def listar_empresas(self, response):
        try:
            empresas = []
            content = response.content.decode('utf-8')
            regex = r'<option value="([^"]+)">[^-]+ - ([^<]+)<\/option>'
            matches = re.findall(regex, content)
            for match in matches:
                empresa = {
                    'id': match[0],
                    'razao_social': match[1].strip()
                }
                empresas.append(empresa)
            return empresas
        except Exception as ex:
            logging.error(ex, 'listar empresas')
            raise Exception

    def get_mensagens(self, empresa):
        try:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Referer': 'https://receita.pr.gov.br/caixa_postal',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                '_limit': '20',
                '_offset': '0',
                'tipo': '0',
                'filtro': empresa['id'],
            }

            response = self.session.get('https://receita.pr.gov.br/portal/v1.0/mensagens',
                                        params=params, headers=headers)
            return response.json()
        except Exception as ex:
            logging.error(ex, 'get mensagens')
            raise Exception

    def get_conteudo_mensagem(self, mensagens_empresa):
        try:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Referer': 'https://receita.pr.gov.br/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            response = self.session.get('https://receita.pr.gov.br/portal/v1.0/mensagens/' + str(mensagens_empresa[0]['id']), headers=headers)
            del response

        except Exception as ex:
            logging.error(ex, 'get conteudo mensagem')
            raise Exception

    def verificar_situacao_leitura(self, mensagens):
        try:
            for element in mensagens:
                if str(element['status_mensagem_id']) == '7':
                    return 'mensagem lida'
            return None

        except Exception as ex:
            logging.error(ex, 'verificar situacao leitura')
            raise Exception
