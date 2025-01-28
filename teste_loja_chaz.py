import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class TestRegistrationForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configura o WebDriver e abre o navegador."""
        print("Iniciando o navegador...")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.cadastrodeclientesonline.com.br/wizard.aspx")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def preencher_campo(self, id_elemento, valor):
        """Método auxiliar para preencher campos do formulário."""
        campo = self.driver.find_element(By.ID, id_elemento)
        campo.clear()
        campo.send_keys(valor)
        time.sleep(0.5)  # Pequena pausa para garantir o preenchimento

    def clicar_prosseguir(self):
        """Método atualizado para clicar no botão de prosseguir corretamente."""
        try:
            # Localiza o botão
            botao = self.wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnSave")))
            # Rolagem para garantir visibilidade
            self.driver.execute_script("arguments[0].scrollIntoView();", botao)
            # Força o clique via JavaScript, garantindo que seja executado
            self.driver.execute_script("arguments[0].click();", botao)
            time.sleep(2)  # Pequena pausa para permitir o processamento
        except TimeoutException:
            self.fail("Erro: Não foi possível clicar no botão 'Prosseguir'")

    def verificar_mensagem_erro(self, id_div):
        """Método auxiliar para verificar se mensagem de erro está visível."""
        div_erro = self.driver.find_element(By.ID, id_div)
        return div_erro.is_displayed()

    def test_1_campos_vazios(self):
        """Teste 1: Verificar mensagens de erro ao submeter formulário vazio."""
        print("\nIniciando teste de campos vazios...")
        
        # Clica em prosseguir sem preencher nada
        self.clicar_prosseguir()

        # Lista de IDs das mensagens de erro esperadas
        mensagens_erro = ["divNome", "divEmail1", "divSenha1"]
        
        for msg_id in mensagens_erro:
            erro_visivel = self.verificar_mensagem_erro(msg_id)
            self.assertTrue(erro_visivel, f"Erro: Mensagem de {msg_id} não apareceu!")
            if erro_visivel:
                print(f"✓ Mensagem de {msg_id} exibida corretamente")

    def test_2_emails_diferentes(self):
        """Teste 2: Verificar validação de confirmação de email."""
        print("\nIniciando teste de confirmação de email...")
        
        # Preenche dados com emails diferentes
        self.preencher_campo("ctl00_ContentPlaceHolder1_name", "Teste da Silva")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email", "teste@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email2", "outro@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", "Senha@123")
        self.preencher_ccampo("ctl00_ContentPlaceHolder1_senha2", "Senha@123")
        
        self.clicar_prosseguir()
        
        erro_email = self.verificar_mensagem_erro("divEmail2")
        self.assertTrue(erro_email, "Erro: Sistema não detectou emails diferentes!")
        if erro_email:
            print("✓ Validação de emails diferentes funcionando corretamente")

    def test_3_formato_email(self):
        """Teste 3: Verificar validação de formato de email."""
        print("\nIniciando teste de formato de email...")
        
        emails_invalidos = [
            "emailinvalido",  # Sem @
            "@semdominio.com",  # Sem usuário
            "sem@.com",  # Sem domínio
            "teste@dominio",  # Sem .com
        ]
        
        for email in emails_invalidos:
            self.preencher_campo("ctl00_ContentPlaceHolder1_name", "Teste da Silva")
            self.preencher_campo("ctl00_ContentPlaceHolder1_email", email)
            self.preencher_campo("ctl00_ContentPlaceHolder1_email2", email)
            self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", "Senha@123")
            self.preencher_campo("ctl00_ContentPlaceHolder1_senha2", "Senha@123")
            
            self.clicar_prosseguir()
            
            erro_formato = self.verificar_mensagem_erro("divFormatoEmail")
            self.assertTrue(erro_formato, f"Erro: Email inválido não detectado: {email}")
            if erro_formato:
                print(f"✓ Formato inválido detectado: {email}")
            
            time.sleep(1)
            self.driver.refresh()
            time.sleep(1)

    def test_4_senhas_diferentes(self):
        """Teste 4: Verificar validação de confirmação de senha."""
        print("\nIniciando teste de confirmação de senha...")
        
        self.preencher_campo("ctl00_ContentPlaceHolder1_name", "Teste da Silva")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email", "teste@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email2", "teste@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", "Senha@123")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha2", "Senha@456")
        
        self.clicar_prosseguir()
        
        erro_senha = self.verificar_mensagem_erro("divSenha2")
        self.assertTrue(erro_senha, "Erro: Sistema não detectou senhas diferentes!")
        if erro_senha:
            print("✓ Validação de senhas diferentes funcionando corretamente")

    def test_5_cadastro_valido(self):
        """Teste 5: Realizar um cadastro com dados válidos."""
        print("\nIniciando teste de cadastro válido...")
        
        # Preenche todos os campos corretamente
        self.preencher_campo("ctl00_ContentPlaceHolder1_name", "Maria Silva")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email", "maria@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_email2", "maria@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", "Senha@123")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha2", "Senha@123")
        
        # Marca os checkboxes
        checkbox1 = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_CheckBox1")
        checkbox2 = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_CheckBox2")
        
        if not checkbox1.is_selected():
            checkbox1.click()
        if not checkbox2.is_selected():
            checkbox2.click()
        
        self.clicar_prosseguir()
        
        # Verifica se não há mensagens de erro
        mensagens_erro = ["divNome", "divEmail1", "divEmail2", "divSenha1", "divSenha2", "divFormatoEmail"]
        sem_erros = True
        
        for msg_id in mensagens_erro:
            if self.verificar_mensagem_erro(msg_id):
                print(f"✗ Erro inesperado: {msg_id} está visível")
                sem_erros = False
        
        if sem_erros:
            print("✓ Cadastro realizado com sucesso!")
        
        self.assertTrue(sem_erros, "Erro: Cadastro válido apresentou mensagens de erro!")

    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após os testes."""
        print("\nFechando o navegador...")
        time.sleep(2)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2)
