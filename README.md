# Exercícios de Programação em Python 🐍

Os projetos foram criados para praticar lógica de programação, estruturas de dados, orientação a objetos, manipulação de arquivos e automação com Excel.

---

## Exercícios 📋

### Exercício 1: Menu de Cálculos Salariais
**Descrição:** Programa com um menu interativo para cálculos salariais.

**Menu de Opções:**
1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair

**Requisitos:**
- Usuário seleciona uma opção e insere os dados solicitados.
- **Opção 1:** Calcula o novo salário com base nas faixas:
  - Até R$ 350,00: aumento de 15%
  - Entre R$ 350,00 e R$ 600,00: aumento de 10%
  - Acima de R$ 600,00: aumento de 5%
- **Opção 2:** Calcula férias (salário + 50%).
- **Opção 3:** Calcula décimo terceiro: `(salário × meses trabalhados) ÷ 12`.
- **Opção 4:** Encerra o programa.
- Valida opções inválidas, mas não os valores inseridos.

---

### Exercício 2: Lista de Tarefas (To-Do List)
**Descrição:** Sistema de gerenciamento de tarefas no console.

**Menu de Opções (como tupla):**
1. Adicionar uma tarefa
2. Visualizar todas as tarefas
3. Marcar uma tarefa como concluída
4. Remover uma tarefa
5. Sair

**Requisitos:**
- Tarefas são representadas como dicionários.
- Navegação contínua pelo menu até a opção de saída.

---

### Exercício 3: Sistema Bancário com POO
**Descrição:** Implementação de um sistema bancário com classes `Cliente` e `ContaBancaria`.

**Classe `Cliente`:**
- Atributos: `nome`, `cpf`

**Classe `ContaBancaria`:**
- Atributos: `numero_conta`, `saldo`, `titular` (instância de `Cliente`)
- Métodos:
  - `depositar(valor)`: Adiciona valor ao saldo.
  - `sacar(valor)`: Subtrai valor, se saldo suficiente.
  - `consultar_saldo()`: Retorna o saldo atual.
  - `informacoes_titular()`: Exibe nome e CPF do titular.

---

### Exercício 4: Cadastro de Pessoas com Excel
**Descrição:** Sistema de cadastro utilizando um arquivo `.xlsx` como banco de dados.

**Classe `Pessoa`:**
- Atributos: `código`, `nome`, `idade`, `telefone`

**Menu do Sistema:**
1. Cadastrar nova pessoa (telefones duplicados não permitidos)
2. Consultar todas as pessoas
3. Editar uma pessoa existente
4. Excluir uma pessoa
5. Sair e gerar arquivo `novo.xlsx`

**Requisitos:**
- Dados lidos de um `.xlsx` inicial e manipulados via DataFrame.
- Alterações salvas em novo arquivo Excel ao encerrar.
- Interação 100% via console.

---

### Exercício 5: Sistema de Controle de Estoque
**Descrição:** Sistema com autenticação e gerenciamento de produtos em Excel.

**Autenticação:**
- Usuário: e-mail (definido pela dupla)
- Senha: `python`

**Estrutura do Excel:**
- Colunas: `ID do Produto`, `Nome do Produto`, `Quantidade em Estoque`, `Preço de Compra`, `Preço de Venda`, `Data da Compra`

**Menu de Funcionalidades:**
1. Adicionar produto
2. Editar produto
3. Excluir produto
4. Exportar dados (`.xlsx`, `.csv`, `.json`)
5. Sair

**Regras de Validação:**
- Preços de compra/venda > 0.
- Quantidade > 0.
- Campos obrigatórios.

**Extras:**
- Retorno ao menu após cada ação.
- Pergunta sobre exportação ao sair, se não realizada.
- Interface amigável no terminal.

---

## Tecnologias Utilizadas 🛠️
- **Python 3.x**
- **Bibliotecas:** `pandas`, `openpyxl` para manipulação de arquivos Excel.

---

## Objetivo 🧠 
Praticar fundamentos de programação e automação em Python, aplicando-os em sistemas simples e funcionais.

---

## Contato 📩
**Desenvolvido por:** Leonardo da Silveira  
**Formação:** Estudante de Sistemas de Informação - Unifafibe