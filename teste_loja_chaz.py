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
        cls.driver.get(
            "https://www.cadastrodeclientesonline.com.br/wizard.aspx")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def preencher_campo(self, id_elemento, valor):
        """Método auxiliar para preencher campos do formulário."""
        campo = self.driver.find_element(By.ID, id_elemento)
        campo.clear()
        campo.send_keys(valor)
        time.sleep(0.5)

    def clicar_prosseguir(self):
        """Método auxiliar para clicar no botão de prosseguir."""
        botao = self.driver.find_element(
            By.ID, "ctl00_ContentPlaceHolder1_btnSave")
        self.driver.execute_script("arguments[0].scrollIntoView();", botao)
        time.sleep(0.5)
        botao.click()

    def marcar_checkbox(self, id_elemento):
        """Método auxiliar para marcar checkbox."""
        checkbox = self.driver.find_element(By.ID, id_elemento)
        if not checkbox.is_selected():
            checkbox.click()

    def test_1_campos_vazios(self):
        """Teste 1: Verificar erro ao submeter formulário com campos vazios."""
        print("Iniciando teste de campos vazios...")
        self.clicar_prosseguir()

        # Verifica se as mensagens de erro aparecem
        elementos_erro = ["divNome", "divEmail1", "divSenha1"]
        for elemento in elementos_erro:
            div_erro = self.driver.find_element(By.ID, elemento)
            self.assertTrue(div_erro.is_displayed(),
                            f"Mensagem de erro para {elemento} não apareceu")

    def test_2_validacao_interface(self):
        """Teste 2: Verificar elementos e comportamento da interface."""
        print("Iniciando teste de interface...")

        # Verifica presença de elementos principais
        elementos = [
            "ctl00_ContentPlaceHolder1_name",
            "ctl00_ContentPlaceHolder1_email",
            "ctl00_ContentPlaceHolder1_email2",
            "ctl00_ContentPlaceHolder1_senha1",
            "ctl00_ContentPlaceHolder1_senha2",
            "ctl00_ContentPlaceHolder1_CheckBox1",
            "ctl00_ContentPlaceHolder1_CheckBox2"
        ]

        for elemento in elementos:
            self.assertTrue(
                self.driver.find_element(By.ID, elemento).is_displayed(),
                f"Elemento {elemento} não está visível"
            )

        # Verifica se o placeholder está correto
        nome_field = self.driver.find_element(
            By.ID, "ctl00_ContentPlaceHolder1_name")
        self.assertEqual(nome_field.get_attribute("placeholder"), "Nome")

    def test_3_formato_email(self):
        """Teste 3: Verificar diferentes formatos de email."""
        print("Iniciando teste de formatos de email...")

        emails_invalidos = [
            "emailsememail.com",  # Sem @
            "@email.com",         # Sem local-part
            "email@.com",         # Sem domínio
            "email@email.",       # TLD incompleto
            "email@email"         # Sem TLD
        ]

        for email in emails_invalidos:
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_name", "Teste Silva")
            self.preencher_campo("ctl00_ContentPlaceHolder1_email", email)
            self.preencher_campo("ctl00_ContentPlaceHolder1_email2", email)
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_senha1", "senha123")
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_senha2", "senha123")

            self.clicar_prosseguir()

            div_formato_email = self.driver.find_element(
                By.ID, "divFormatoEmail")
            self.assertTrue(div_formato_email.is_displayed(),
                            f"Email inválido não detectado: {email}")

    def test_4_cadastro_completo(self):
        """Teste 4: Simular um cadastro completo com dados válidos."""
        print("Iniciando teste de cadastro completo...")

        # Preenche todos os campos corretamente
        self.preencher_campo("ctl00_ContentPlaceHolder1_name", "Maria Silva")
        self.preencher_campo(
            "ctl00_ContentPlaceHolder1_email", "maria@email.com")
        self.preencher_campo(
            "ctl00_ContentPlaceHolder1_email2", "maria@email.com")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", "Senha@123")
        self.preencher_campo("ctl00_ContentPlaceHolder1_senha2", "Senha@123")

        # Marca os checkboxes
        self.marcar_checkbox("ctl00_ContentPlaceHolder1_CheckBox1")
        self.marcar_checkbox("ctl00_ContentPlaceHolder1_CheckBox2")

        # Submete o formulário
        self.clicar_prosseguir()

        try:
            # Aguarda mudança de página ou mensagem de sucesso
            # Ajuste o seletor conforme necessário
            self.wait.until(lambda driver: driver.current_url !=
                            "https://www.cadastrodeclientesonline.com.br/wizard.aspx")
            print("Cadastro realizado com sucesso!")
        except TimeoutException:
            self.fail("Cadastro não foi concluído com sucesso")

    def test_5_validacao_senha(self):
        """Teste 5: Verificar diferentes formatos e requisitos de senha."""
        print("Iniciando teste de validação de senha...")

        # Lista de senhas para testar
        senhas_teste = [
            ("123", False),           # Muito curta
            ("12345678", True),       # Tamanho adequado
            ("senha com espaço", False),  # Contém espaço
            ("Senha@123", True),      # Formato válido
        ]

        for senha, esperado_valido in senhas_teste:
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_name", "Teste Silva")
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_email", "teste@email.com")
            self.preencher_campo(
                "ctl00_ContentPlaceHolder1_email2", "teste@email.com")
            self.preencher_campo("ctl00_ContentPlaceHolder1_senha1", senha)
            self.preencher_campo("ctl00_ContentPlaceHolder1_senha2", senha)

            self.clicar_prosseguir()

            # Verifica se o comportamento corresponde ao esperado
            div_senha = self.driver.find_element(By.ID, "divSenha2")
            if esperado_valido:
                self.assertFalse(div_senha.is_displayed(),
                                 f"Senha válida foi rejeitada: {senha}")
            else:
                self.assertTrue(div_senha.is_displayed(),
                                f"Senha inválida foi aceita: {senha}")

    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após os testes."""
        print("Fechando o navegador...")
        time.sleep(2)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
