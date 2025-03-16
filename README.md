# Extrator de Listas do SharePoint para CSV
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![SharePoint](https://img.shields.io/badge/SharePoint-Integration-green)
![CSV](https://img.shields.io/badge/CSV-Export-orange)

## 🚀 Sobre o Projeto

Este script em Python permite conectar-se a um site SharePoint, extrair dados de uma lista específica e convertê-los para um arquivo CSV. A solução facilita a interoperabilidade entre sistemas ao fornecer dados estruturados de maneira acessível e portátil.

## 📌 Funcionalidades

✅ Conexão segura com SharePoint usando autenticação via Client ID e Client Secret.  
✅ Extração automatizada de dados de listas do SharePoint.  
✅ Filtro opcional de colunas para otimizar os dados exportados.  
✅ Exportação dos dados em formato CSV para integração com outros sistemas.  

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Office365-REST-Python-Client** para conexão com SharePoint
- **Pandas** para manipulação e exportação de dados
- **Argparse** para manipulação de parâmetros via linha de comando

## 📦 Instalação

### 1️⃣ Clone este repositório
```sh
 git clone https://github.com/jeanjesusia/sharepoint-list-extractor2csv.git
 cd sharepoint-list-extractor2csv
```

### 2️⃣ Instale as dependências
```sh
pip install -r requirements.txt
```

## 🔧 Como Usar

O script pode ser executado diretamente via linha de comando, passando os parâmetros necessários.

### 📌 Exemplo de Uso
```sh
python extractor.py --base_url "https://seusite.sharepoint.com/sites/SEUSITE" \
                    --list_name "Nome da Lista" \
                    --cols "col1, col2, col2:novo_nome" \
                    --target "./dados/lista.csv"
```

### 📌 Parâmetros
| Parâmetro    | Obrigatório | Descrição |
|-------------|------------|-----------|
| `--base_url` | ✅ | URL base do SharePoint |
| `--list_name` | ✅ | Nome da lista a ser extraída |
| `--cols` | ❌ | Lista de colunas separadas por vírgula (opcional). Para mudar o nome de uma coluna, use `:` e adicione o novo nome ao lado. Exemplo: `coluna_antiga:coluna_nova`. |
| `--target` | ✅ | Diretório ou caminho do arquivo CSV de saída. Caso não seja passado o nome do arquivo de saída, será utilizado o nome da lista como nome final do arquivo. |

## 🔐 Autenticação

Para autenticação, é necessário fornecer as credenciais do aplicativo SharePoint, substitua os parâmetros `seu_client_id` e `seu_client_secret` por suas informações:

```python
app_principal = {
    'client_id': 'seu_client_id',
    'client_secret': 'seu_client_secret',
}
```
💡 **Dica:** Não é uma boa prática manter suas credenciais diretamente no código! Utilize variáveis de ambiente ou um arquivo `.env`. Para fins de aprendizado, iremos utilizar as credenciais no codigo.

## ⚠️ Tratamento de Erros

O script possui um mecanismo de tratamento de erros para garantir que falhas na conexão com o SharePoint ou na extração de dados sejam devidamente reportadas. No entanto, para automações que exigem uma resposta (como PowerCenter e outros), utilizamos raise para gerar um erro que possa ser capturado pelo programa.

---

Feito com ❤️ por [Jean Jesus](https://github.com/jeanjesusia) 🚀

