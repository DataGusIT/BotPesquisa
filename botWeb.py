import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def responder_pesquisa(url_formulario, num_respostas=100):
    """
    Função para responder a pesquisa de satisfação pós-venda
    
    Args:
        url_formulario (str): URL do Google Forms
        num_respostas (int): Número de vezes para responder o formulário
    """
    # Configurar o driver do navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    print(f"Iniciando bot para responder pesquisa de satisfação {num_respostas} vezes...")
    
    for i in range(num_respostas):
        try:
            # Inicializar o navegador
            driver = webdriver.Chrome(options=options)
            driver.get(url_formulario)
            
            # Esperar o formulário carregar
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
            )
            
            # Pergunta 1: Escala de 0 a 10 (probabilidade de recomendar)
            # Distribuição tendendo para valores mais altos (6-10) com maior frequência
            nps_opcoes = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[0]
            nps_valores = nps_opcoes.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            
            # Distribuição com tendência para notas altas (mais realista)
            pesos_nps = [1, 1, 1, 2, 2, 3, 5, 8, 10, 10, 8]  # Pesos para cada opção de 0 a 10
            nps_escolhido = random.choices(nps_valores, weights=pesos_nps, k=1)[0]
            nps_escolhido.click()
            
            # Pergunta 2: Tempo de resposta
            tempo_resposta = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[1]
            tempo_opcoes = tempo_resposta.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição mais realista: Muito rápido (40%), Razoável (40%), Demorado (15%), Muito demorado (5%)
            pesos_tempo = [4, 4, 1.5, 0.5]
            tempo_escolhido = random.choices(tempo_opcoes, weights=pesos_tempo, k=1)[0]
            tempo_escolhido.click()
            
            # Pergunta 3: Resolução satisfatória
            resolucao = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[2]
            resolucao_opcoes = resolucao.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição: Sim (70%), Parcialmente (20%), Não (10%)
            pesos_resolucao = [7, 2, 1]
            resolucao_escolhida = random.choices(resolucao_opcoes, weights=pesos_resolucao, k=1)[0]
            resolucao_escolhida.click()
            
            # Pergunta 4: Motivo do contato
            motivo_contato = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[3]
            motivo_opcoes = motivo_contato.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            motivo_escolhido = random.choice(motivo_opcoes)
            motivo_escolhido.click()
            
            # Se "Outros" for selecionado, preencher o campo
            if motivo_escolhido == motivo_opcoes[-1]:
                outros_campo = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
                motivos_outros = ["Problemas com pagamento", "Informações sobre garantia",
                                  "Agendamento de instalação", "Consulta sobre frete",
                                  "Reclamação sobre embalagem"]
                outros_campo.send_keys(random.choice(motivos_outros))
            
            # Pergunta 5: Qualidade do atendimento
            qualidade = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[4]
            qualidade_opcoes = qualidade.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição: Excelente (40%), Bom (40%), Regular (10%), Ruim (7%), Péssimo (3%)
            pesos_qualidade = [4, 4, 1, 0.7, 0.3]
            qualidade_escolhida = random.choices(qualidade_opcoes, weights=pesos_qualidade, k=1)[0]
            qualidade_escolhida.click()
            
            # Pergunta 6: Tempo para resolução
            tempo_resolucao = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[5]
            tempo_resolucao_opcoes = tempo_resolucao.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            tempo_resolucao_escolhido = random.choice(tempo_resolucao_opcoes)
            tempo_resolucao_escolhido.click()
            
            # Pergunta 7: Contato mais de uma vez
            contato_repetido = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[6]
            contato_repetido_opcoes = contato_repetido.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição: Sim (30%), Não (70%)
            pesos_contato = [3, 7]
            contato_escolhido = random.choices(contato_repetido_opcoes, weights=pesos_contato, k=1)[0]
            contato_escolhido.click()
            
            # Pergunta 8: Clareza das informações
            clareza = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[7]
            clareza_opcoes = clareza.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição: Muito claras (50%), Razoavelmente claras (35%), Confusas (10%), Muito confusas (5%)
            pesos_clareza = [5, 3.5, 1, 0.5]
            clareza_escolhida = random.choices(clareza_opcoes, weights=pesos_clareza, k=1)[0]
            clareza_escolhida.click()
            
            # Pergunta 9: Atendimento às expectativas
            expectativas = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")[8]
            expectativas_opcoes = expectativas.find_elements(By.CSS_SELECTOR, "div[role='radio']")
            # Distribuição: Superou (25%), Atendeu (50%), Não atendeu (20%), Muito abaixo (5%)
            pesos_expectativas = [2.5, 5, 2, 0.5]
            expectativas_escolhida = random.choices(expectativas_opcoes, weights=pesos_expectativas, k=1)[0]
            expectativas_escolhida.click()
            
            # Botão de enviar
            submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][jsname]")
            submit_button.click()
            
            # Esperar confirmação de envio
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'resposta foi registrada') or contains(text(), 'response has been recorded')]"))
            )
            
            print(f"Resposta {i+1} enviada com sucesso!")
            
            # Fechar navegador
            driver.quit()
            
            # Esperar um tempo aleatório para evitar detecção
            time.sleep(random.uniform(2, 5))
            
        except Exception as e:
            print(f"Erro ao enviar resposta {i+1}: {str(e)}")
            if 'driver' in locals():
                driver.quit()
            time.sleep(1)

if __name__ == "__main__":
    # URL do seu formulário Google Forms
    url_formulario = "https://docs.google.com/forms/d/e/1FAIpQLSekaK_0_gu9Kvi2QPqA7hi61IsdUXpuYiJICZdm5iZpQfY4zQ/viewform"
    
    # Número de respostas a serem enviadas
    num_respostas = 100
    
    responder_pesquisa(url_formulario, num_respostas)