# Exportar Usuários JSON para Excel

Ferramenta simples para transformar dados de usuários em formato JSON em uma planilha Excel estruturada.


## 📥 Download

Baixe o executável na aba Releases:
https://github.com/lailanga/exportar-usuarios-json-para-excel/releases

## 🎯 Objetivo

Este projeto foi criado para resolver um problema comum:
a necessidade de extrair dados de sistemas que não possuem opção nativa de exportação.

A solução consiste em utilizar dados JSON (obtidos via API ou inspeção do navegador) e convertê-los em um formato utilizável para análise.

---

## 🚀 Funcionalidades

* Leitura de arquivos JSON (estrutura flexível)
* Suporte a:

  * listas diretas
  * objetos com `content`
* Geração automática de planilha Excel
* Identificação de níveis de acesso:

  * Administrador
  * Técnico
* Interface simples para seleção de arquivo

---

## 📥 Download rápido

Você pode baixar a versão executável (não precisa de Python):

👉 Acesse a aba **Releases** e faça o download do arquivo `.exe`

---

## 🧩 Como usar (Python)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar

```bash
python gerar_excel.py
```

### 3. Selecionar o arquivo JSON

A planilha será gerada automaticamente na mesma pasta do arquivo selecionado.

---

## 📁 Estrutura esperada do JSON

Formato 1:

```json
[
  {
    "username": "Nome",
    "user": "login",
    "admin": true,
    "technical": false
  }
]
```

Formato 2:

```json
{
  "content": [
    {
      "username": "Nome",
      "user": "login",
      "admin": true,
      "technical": false
    }
  ]
}
```

---

## ⚙️ Personalização

Caso o JSON utilize outros nomes de campos, ajuste no código:

```python
MAP = {
    "nome": "username",
    "usuario": "user",
    "admin": "admin",
    "tecnico": "technical"
}
```

---

## 🧠 Contexto

A solução surgiu a partir de uma demanda real:
obter a relação de usuários de um sistema sem funcionalidade de exportação disponível.

Ao analisar o comportamento da aplicação no navegador, foi possível identificar que os dados eram carregados via JSON.
A partir disso, foi feita a extração e transformação dos dados em Excel.

---

## 📌 Possíveis usos

* Auditoria de acessos
* Controle de usuários
* Integração com Power BI
* Extração de dados de sistemas legados

---

## ⚠️ Observações

* O JSON deve estar válido
* Campos ausentes serão preenchidos como vazio
* O script pode ser adaptado para outros cenários de dados

---

## 📄 Licença

Uso livre para fins de estudo e adaptação.
