
# Bot para Preenchimento de Pesquisas com Selenium

> Automação em Python que preenche formulários Google Forms de forma massiva e realista, simulando respostas humanas para geração de dados de teste para dashboards e análises.

[![Status](https://img.shields.io/badge/Status-Concluído-success)](https://github.com/seu-usuario/powerbi-rh-dashboard)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Web_Automation-43B02A)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

## Sobre o Projeto

Este projeto é um bot desenvolvido em Python com a biblioteca **Selenium** para automatizar o preenchimento de uma pesquisa de satisfação no Google Forms. O principal diferencial deste bot é sua capacidade de gerar respostas que simulam tendências humanas, utilizando pesos e probabilidades para selecionar opções de forma mais realista, em vez de puramente aleatória.

O objetivo é popular rapidamente uma base de dados com um volume significativo de respostas, ideal para testar dashboards (como os de Power BI), relatórios e outras ferramentas de análise de dados sem a necessidade de preenchimento manual.

## ✨ Funcionalidades

-   **Automação com Selenium:** Controla um navegador Chrome em modo *headless* (sem interface gráfica) para navegar e interagir com a página do formulário.
-   **Geração de Respostas Realistas:** Utiliza `random.choices` com pesos para simular um comportamento humano mais autêntico. Por exemplo, as notas de satisfação tendem a ser mais altas, e as respostas sobre a resolução de problemas são majoritariamente positivas.
-   **Execução em Lote:** O script é configurado para preencher o formulário um número predefinido de vezes (ex: 100 respostas), ideal para gerar grandes volumes de dados.
-   **Comportamento Humanizado:** Inclui pausas aleatórias (`time.sleep`) entre os envios para evitar sobrecarregar o servidor ou ser detectado como um bot malicioso.
-   **Tratamento de Campos Condicionais:** Identifica quando a opção "Outros" é selecionada e preenche o campo de texto correspondente com uma resposta aleatória.

## Tecnologias

### Core
-   **Python 3.9+** - Linguagem principal da automação.

### Ferramentas de Automação
-   **Selenium WebDriver** - Para controle do navegador e automação de interações web.

## Pré-requisitos

-   Python 3.9 ou superior instalado.
-   Google Chrome instalado na máquina.
-   **ChromeDriver** correspondente à sua versão do Google Chrome. O ChromeDriver é o executável que permite ao Selenium controlar o navegador.

## Instalação e Uso

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/seu-usuario/selenium-form-bot.git
    cd selenium-form-bot
    ```

2.  **Instale as dependências**
    ```bash
    pip install selenium
    ```

3.  **Baixe e configure o ChromeDriver**
    -   Verifique a versão do seu Google Chrome (em `Configurações` > `Sobre o Google Chrome`).
    -   Baixe o **ChromeDriver** correspondente à sua versão em [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/).
    -   Extraia e coloque o arquivo `chromedriver.exe` (ou `chromedriver` em Linux/macOS) **na mesma pasta do seu script Python**.

4.  **Configure o script**
    -   Abra o arquivo `main.py` (ou o nome do seu script).
    -   Altere a variável `url_formulario` para a URL do Google Forms que você deseja automatizar.
    -   Ajuste a variável `num_respostas` para a quantidade de envios desejada.

5.  **Execute a automação**
    ```bash
    python main.py
    ```
    O script começará a enviar as respostas e exibirá o progresso no console.

## ⚠️ Avisos Importantes

-   **Uso Ético:** Esta ferramenta foi criada para fins educacionais e para geração de dados de teste em formulários que você possui ou tem permissão para testar. **Não utilize para spam**, manipulação de pesquisas ou qualquer atividade maliciosa.
-   **Estrutura do Formulário:** A automação depende da estrutura HTML do Google Forms. Se o Google alterar a forma como os elementos são organizados, os seletores (CSS ou XPath) no código podem quebrar e precisar de atualização.
-   **Possível Bloqueio:** O envio de um número muito grande de requisições em um curto período de tempo pode levar ao bloqueio temporário do seu endereço IP pelo Google. Use com moderação.

## Suporte e Contato

-   **Email**: [g.moreno.souza05@gmail.com](mailto:g.moreno.souza05@gmail.com)
-   **LinkedIn**: [Gustavo Moreno](https://www.linkedin.com/in/gustavo-moreno-8a925b26a/)

## Licença

Este projeto está licenciado sob uma Licença Proprietária.

**Uso Restrito**: Este software é de propriedade exclusiva do autor. Uso comercial ou redistribuição requer autorização expressa.

---

<div align="center">
  Desenvolvido por Gustavo Moreno
  <br><br>
  <a href="https://www.linkedin.com/in/gustavo-moreno-8a925b26a/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" alt="LinkedIn"/>
  </a>
</div>
