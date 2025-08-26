# 🛒 Sistema de Gerenciamento de Estoque em Python

Este é um **sistema simples de gerenciamento de estoque** desenvolvido em Python.  
Ele roda no terminal e permite **cadastrar, editar, remover, consultar e gerar relatórios** de produtos.

---

## 📌 Funcionalidades
- 📥 **Cadastrar Produto**: Nome, categoria, quantidade e preço
- ✏️ **Editar Produto**: Atualize informações já cadastradas
- ❌ **Remover Produto**: Exclua produtos do estoque
- ➕ **Registrar Entrada**: Adicione quantidade a um produto
- ➖ **Registrar Saída**: Retire quantidade de um produto
- 🔍 **Consultar Produto**: Busque por ID, nome ou categoria
- 📋 **Relatório Geral**: Veja todos os produtos cadastrados
- ⚠️ **Relatório de Baixo Estoque**: Produtos com quantidade abaixo de um valor mínimo

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**

---

## 📂 Estrutura do Código
O código é dividido em funções para cada ação:
- `cadastrar_produto()`
- `editar_produto()`
- `remover_produto()`
- `registrar_entrada()`
- `registrar_saida()`
- `consultar_produto()`
- `relatorio_geral()`
- `relatorio_baixo_estoque()`

O programa funciona em **loop** até que o usuário escolha a opção de sair.
