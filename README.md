# Testes Automatizados em Aplicações Web

## Objetivo
Aplicar conceitos de testes automatizados utilizando a biblioteca `unittest` com Selenium para validar funcionalidades de interface. Esta atividade visa simular a interação de um usuário real com um site e garantir que as funcionalidades principais estejam funcionando como esperado.

---

## Descrição do Projeto
O projeto utiliza `unittest` como framework de testes e o Selenium WebDriver para interagir com a interface de um site. O site escolhido é o "Cadastro de Clientes Online", e os testes foram desenvolvidos para verificar as principais funcionalidades, como o preenchimento de formulários, validação de dados e submissão bem-sucedida.

---

## Bibliotecas e Ferramentas Utilizadas
- **Python 3.8+**
- **unittest**: Framework para estruturação e execução de testes.
- **Selenium WebDriver**: Ferramenta de automação para simulação de interações com browsers.
- **Google Chrome** + **ChromeDriver**

---

## Funcionalidades Testadas
Foram implementados cinco testes principais para garantir a funcionalidade correta da interface e dos processos do site:

1. **Validação de campos obrigatórios:**
   - Testa se as mensagens de erro são exibidas quando os campos obrigatórios do formulário estão vazios.

2. **Confirmação de email:**
   - Verifica se o sistema detecta e exibe mensagens de erro quando os emails preenchidos nos campos "Email" e "Confirmar Email" não são idênticos.

3. **Validação de formato de email:**
   - Testa se o site exibe mensagens de erro ao inserir emails com formatos inválidos (ex.: sem @, domínios incorretos).

4. **Confirmação de senha:**
   - Verifica se há validação para senhas diferentes nos campos "Senha" e "Confirmar Senha".

5. **Cadastro com dados válidos:**
   - Simula o preenchimento correto de todos os campos obrigatórios e a aceitação dos termos de uso, validando que não aparecem mensagens de erro e que a operação é bem-sucedida.

---

## Relatório de Execução

1. **Configuração Inicial:**
   - Configuramos o ambiente com o Selenium WebDriver, especificando o ChromeDriver e acessamos o site de teste.

2. **Logs e Resultados:**
   - Durante a execução dos testes, foram registrados logs que indicam a passagem ou falha de cada cenário.
   - Todas as interações e validações seguiram um fluxo linear para facilitar a verificação de falhas.

3. **Imagens e Prints:**

   - Abaixo estão alguns dos prints de tela organizados, capturados durante o teste de submissão do formulário para validação visual:

   ### Validação de emails diferentes
    ![Captura de tela 2025-01-27 231929](https://github.com/user-attachments/assets/9f297294-e401-4b4a-986b-344d69270ecb)

   ### Validação de formato inválido de email
  ![Captura de tela 2025-01-27 231916](https://github.com/user-attachments/assets/55eda832-1d61-4cf7-80cd-270d7db22c06)

   ### Validação de senhas diferentes
  ![Captura de tela 2025-01-27 231929](https://github.com/user-attachments/assets/bcab2ef4-e99f-43ca-bad6-48ce207e89b6)

   ### Resposta do Terminal
   ![Captura de tela 2025-01-27 231821](https://github.com/user-attachments/assets/f3c4f12c-10e6-484b-a3a7-474d5898a786)

4. **Resultados Obtidos:**
   - Todos os cinco testes passaram com sucesso, validando corretamente os comportamentos descritos acima. Isso inclui mensagens de erro esperadas para entradas inválidas e operações bem-sucedidas para dados válidos.

---

## Como Executar os Testes

1. **Pré-requisitos:**
   - Python instalado (versão 3.8 ou superior)
   - Google Chrome instalado
   - ChromeDriver compatível com a versão do navegador

2. **Configuração:**
   - Instale as dependências necessárias:
     ```bash
     pip install selenium
     ```

3. **Execução:**
   - No terminal, navegue até o diretório onde o código está salvo e execute:
     ```bash
     python nome_do_arquivo.py
     ```

4. **Resultados:**
   - O terminal exibirá os logs detalhados de cada teste, indicando sucesso ou falha.

---

## Estrutura do Projeto

```
Projeto/
├── teste_cadastro.py  # Código-fonte dos testes automatizados
├── README.md          # Documento explicativo (este arquivo)
└── prints/            # Capturas de tela e logs de execução
```

---


---

## Conclusão
Os testes automatizados desenvolvidos com unittest e Selenium garantiram que as principais funcionalidades do site "Cadastro de Clientes Online" estão funcionando corretamente. A atividade proporcionou experiência prática com o desenvolvimento de cenários de teste e a validação do comportamento esperado de sistemas baseados em interface.

### Links úteis
- [Selenium Documentation](https://www.selenium.dev/pt-br/)
- [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
