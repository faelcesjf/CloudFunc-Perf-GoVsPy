from DecParana import DecParana


def main(request):
    try:
        if request.method == 'POST':
            data = request.get_json()
            login = data.get('login')
            senha = data.get('senha')

            scraping = DecParana(login=login, senha=senha)
            response = scraping.dec_parana()

            return response, 200

        else:
            return 'Método não suportado', 405

    except Exception as ex:
        raise Exception
