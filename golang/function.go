package function

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/http/cookiejar"
	"regexp"
	"strings"
	"time"

	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
)

func init() {
	functions.HTTP("dec-parana", main)
}

func main(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Método não permitido, apenas POST é suportado", http.StatusMethodNotAllowed)
		return
	}

	var credenciais Credentials
	err := json.NewDecoder(r.Body).Decode(&credenciais)
	if err != nil {
		http.Error(w, "Erro ao decodificar corpo da requisição JSON", http.StatusBadRequest)
		return
	}

	fmt.Println("Inciando cloud function dec_parana GOLANG!")

	userAgent := "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"

	client := &http.Client{
		Timeout: time.Second * 60,
	}

	jar, _ := cookiejar.New(nil)
	client.Jar = jar

	getPortal(client, userAgent)

	postLogin(client, userAgent, credenciais.Login, credenciais.Senha)

	htmlText, err := getCaixaPostal(client, userAgent)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	getJson(client, userAgent, htmlText)

	w.WriteHeader(http.StatusOK)

	fmt.Println("Fim Execução cloud function dec_parana GOLANG!")
}

func getPortal(client *http.Client, userAgent string) {
	req, err := http.NewRequest("GET", "https://receita.pr.gov.br/login", nil)
	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
	req.Header.Set("Accept-Language", "en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7")
	req.Header.Set("Cache-Control", "max-age=0")
	req.Header.Set("Connection", "keep-alive")
	req.Header.Set("Referer", "https://receita.pr.gov.br/caixa_postal")
	req.Header.Set("Sec-Fetch-Dest", "document")
	req.Header.Set("Sec-Fetch-Mode", "navigate")
	req.Header.Set("Sec-Fetch-Site", "same-origin")
	req.Header.Set("Sec-Fetch-User", "?1")
	req.Header.Set("Upgrade-Insecure-Requests", "1")
	req.Header.Set("User-Agent", userAgent)
	req.Header.Set("sec-ch-ua", `"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"`)
	req.Header.Set("sec-ch-ua-mobile", "?1")
	req.Header.Set("sec-ch-ua-platform", `"Android"`)
	resp, err := client.Do(req)

	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
}

func postLogin(client *http.Client, userAgent string, login string, senha string) {
	requestBody := fmt.Sprintf("cpfusuario=%s&senha=%s", login, senha)
	var data = strings.NewReader(requestBody)
	req, err := http.NewRequest("POST", "https://receita.pr.gov.br/login", data)

	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
	req.Header.Set("Accept-Language", "en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7")
	req.Header.Set("Cache-Control", "max-age=0")
	req.Header.Set("Connection", "keep-alive")
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Set("Origin", "https://receita.pr.gov.br")
	req.Header.Set("Referer", "https://receita.pr.gov.br/login")
	req.Header.Set("Sec-Fetch-Dest", "document")
	req.Header.Set("Sec-Fetch-Mode", "navigate")
	req.Header.Set("Sec-Fetch-Site", "same-origin")
	req.Header.Set("Sec-Fetch-User", "?1")
	req.Header.Set("Upgrade-Insecure-Requests", "1")
	req.Header.Set("User-Agent", userAgent)
	req.Header.Set("sec-ch-ua", `"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"`)
	req.Header.Set("sec-ch-ua-mobile", "?1")
	req.Header.Set("sec-ch-ua-platform", `"Android"`)

	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
}

func getCaixaPostal(client *http.Client, userAgent string) ([]byte, error) {
	req, err := http.NewRequest("GET", "https://receita.pr.gov.br/caixa_postal", nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
	req.Header.Set("Accept-Language", "en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7")
	req.Header.Set("Cache-Control", "max-age=0")
	req.Header.Set("Connection", "keep-alive")
	req.Header.Set("Sec-Fetch-Dest", "document")
	req.Header.Set("Sec-Fetch-Mode", "navigate")
	req.Header.Set("Sec-Fetch-Site", "none")
	req.Header.Set("Sec-Fetch-User", "?1")
	req.Header.Set("Upgrade-Insecure-Requests", "1")
	req.Header.Set("User-Agent", userAgent)
	req.Header.Set("sec-ch-ua", `"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"`)
	req.Header.Set("sec-ch-ua-mobile", "?1")
	req.Header.Set("sec-ch-ua-platform", `"Android"`)

	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	return body, nil
}

func getMensagens(value string, client *http.Client, userAgent string) []Mensagem {
	var result []Mensagem
	offset := 0
	limit := 20

	for {
		req, err := http.NewRequest("GET", fmt.Sprintf("https://receita.pr.gov.br/portal/v1.0/mensagens?_limit=%d&_offset=%d&tipo=0&filtro=%s", limit, offset, value), nil)
		if err != nil {
			log.Fatal(err)
		}
		req.Header.Set("Accept", "*/*")
		req.Header.Set("Accept-Language", "en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7")
		req.Header.Set("Connection", "keep-alive")
		req.Header.Set("Referer", "https://receita.pr.gov.br/caixa_postal")
		req.Header.Set("Sec-Fetch-Dest", "empty")
		req.Header.Set("Sec-Fetch-Mode", "cors")
		req.Header.Set("Sec-Fetch-Site", "same-origin")
		req.Header.Set("User-Agent", userAgent)
		req.Header.Set("X-Requested-With", "XMLHttpRequest")
		req.Header.Set("sec-ch-ua", `"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"`)
		req.Header.Set("sec-ch-ua-mobile", "?1")
		req.Header.Set("sec-ch-ua-platform", `"Android"`)
		resp, err := client.Do(req)
		if err != nil {
			log.Fatal(err)
		}

		var mensagens []Mensagem
		err = json.NewDecoder(resp.Body).Decode(&mensagens)
		if err != nil {
			log.Fatal(err)
		}

		if len(mensagens) == 0 {
			break
		}

		for _, mensagem := range mensagens {
			if mensagem.StatusMensagemId == 7 {
				mensagem = detalhesMensagem(mensagem, client, userAgent)
			}
			result = append(result, mensagem)
		}

		result = nil
		offset += limit
	}

	return result
}

func detalhesMensagem(mensagem Mensagem, client *http.Client, userAgent string) Mensagem {
	req, err := http.NewRequest("GET", fmt.Sprintf("https://receita.pr.gov.br/portal/v1.0/mensagens/%d", mensagem.Id), nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Accept", "*/*")
	req.Header.Set("Accept-Language", "en,pt-BR;q=0.9,pt;q=0.8,en-US;q=0.7")
	req.Header.Set("Connection", "keep-alive")
	req.Header.Set("Referer", "https://receita.pr.gov.br/caixa_postal")
	req.Header.Set("Sec-Fetch-Dest", "empty")
	req.Header.Set("Sec-Fetch-Mode", "cors")
	req.Header.Set("Sec-Fetch-Site", "same-origin")
	req.Header.Set("User-Agent", userAgent)
	req.Header.Set("X-Requested-With", "XMLHttpRequest")
	req.Header.Set("sec-ch-ua", `"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"`)
	req.Header.Set("sec-ch-ua-mobile", "?1")
	req.Header.Set("sec-ch-ua-platform", `"Android"`)
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	bodyText, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	var detalhes DetalhesMensagem
	if err := json.Unmarshal(bodyText, &detalhes); err != nil {
		log.Fatal(err)
	}

	mensagem.DataLido = detalhes.DataLido
	mensagem.DataArquivado = detalhes.DataArquivado
	mensagem.DataExcluido = detalhes.DataExcluido
	mensagem.DataExcluidoDefinitivamente = detalhes.DataExcluidoDefinitivamente
	mensagem.Corpo = detalhes.Corpo
	mensagem.DataSms = detalhes.DataSms
	mensagem.DataEmail = detalhes.DataEmail
	mensagem.DataExpiracao = detalhes.DataExpiracao
	mensagem.ConfirmarLeitura = detalhes.ConfirmarLeitura
	mensagem.ConfirmacaoLeitura = detalhes.ConfirmacaoLeitura
	mensagem.TempoRetencao = detalhes.TempoRetencao
	mensagem.Sms = detalhes.Sms
	mensagem.Email = detalhes.Email
	mensagem.Prioridade = detalhes.Prioridade

	return mensagem
}

func getJson(client *http.Client, userAgent string, htmlText []byte) {
	re := regexp.MustCompile(`<option\s+value="([^"]+?)">\d+\s*-\s*(.+?)</option>`)

	matches := re.FindAllStringSubmatch(string(htmlText), -1)

	for _, match := range matches {
		if len(match) > 1 {
			getMensagens(match[1], client, userAgent)
		}
	}
}

// DTOS
type EmpresaMensagens struct {
	IdEmpresa   string     `json:"id_empresa"`
	RazaoSocial string     `json:"razao_social"`
	Mensagens   []Mensagem `json:"mensagens"`
}

type DetalhesMensagem struct {
	DataLido                    string  `json:"dt_lido"`
	DataArquivado               *string `json:"dt_arquivado"`
	DataExcluido                *string `json:"dt_excluido"`
	DataExcluidoDefinitivamente *string `json:"dt_excluido_definitivamente"`
	Corpo                       *string `json:"corpo"`
	DataSms                     *string `json:"dt_sms"`
	DataEmail                   *string `json:"dt_email"`
	DataExpiracao               *string `json:"dt_expiracao"`
	ConfirmarLeitura            *int    `json:"confirmar_leitura"`
	ConfirmacaoLeitura          *string `json:"confirmacao_leitura"`
	TempoRetencao               *string `json:"tempo_retencao"`
	Sms                         *int    `json:"sms"`
	Email                       *int    `json:"email"`
	Prioridade                  *int    `json:"prioridade"`
}

type Mensagem struct {
	Id                          int     `json:"id"`
	StatusMensagemId            int     `json:"status_mensagem_id"`
	Assunto                     string  `json:"assunto"`
	TipoEmissorId               int     `json:"tipo_emissor_id"`
	TipoEmissorDescricao        string  `json:"tipo_emissor_descricao"`
	TipoMensagemId              int     `json:"tipo_mensagem_id"`
	DataEnvio                   string  `json:"dt_envio"`
	DataNotificado              string  `json:"dt_notificado"`
	Link                        *string `json:"link"`
	NomeAutorMensagem           string  `json:"nm_autor_mensagem"`
	DataLido                    string  `json:"dt_lido"`
	DataArquivado               *string `json:"dt_arquivado"`
	DataExcluido                *string `json:"dt_excluido"`
	DataExcluidoDefinitivamente *string `json:"dt_excluido_definitivamente"`
	Corpo                       *string `json:"corpo"`
	DataSms                     *string `json:"dt_sms"`
	DataEmail                   *string `json:"dt_email"`
	DataExpiracao               *string `json:"dt_expiracao"`
	ConfirmarLeitura            *int    `json:"confirmar_leitura"`
	ConfirmacaoLeitura          *string `json:"confirmacao_leitura"`
	TempoRetencao               *string `json:"tempo_retencao"`
	Sms                         *int    `json:"sms"`
	Email                       *int    `json:"email"`
	Prioridade                  *int    `json:"prioridade"`
}

type Credentials struct {
	Login string `json:"login"`
	Senha string `json:"senha"`
}
