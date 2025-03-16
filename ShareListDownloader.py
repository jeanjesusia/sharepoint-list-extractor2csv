# Imports
import os
import argparse
import pandas as pd
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.lists.list import List
from office365.runtime.auth.client_credential import ClientCredential


# Criar objeto argparser
parser = argparse.ArgumentParser(description="Processar os parâmetros via linha de comando")

# Definição dos parâmetros esperados
parser.add_argument('--base_url', type=str, help='URL base', required=True)
parser.add_argument('--list_name', type=str, help='Nome da lista', required=True)
parser.add_argument('--cols', type=str, help='lista de colunas separadas por vírgulas', required=False)
parser.add_argument('--target', type=str, help='Diretorio de destino', required=True)


# Realizar leitura dos parâmetros passados
args = parser.parse_args()

# Atribuição dos valores passados via parâmetros
base_url = args.base_url.replace("'",'')
list_name = args.list_name.replace("'",'')
target = args.target.replace("'",'')
cols = args.cols


if cols:
    cols = cols.replace("'",'')
    cols = [col.strip() for col in cols.split(',')]
        

# Conexão com sharepoint
try:
    print("Iniciando Conexão com Sharepoint...")
    app_principal = {
    'client_id': 'seu_client_id',
    'client_secret': 'seu_client_secret',
    }
    
    # URL do site SharePoint
    site_url = base_url #"https://seusite.sharepoint.com/sites/SEUSITE"
    list_name = list_name #"Nome da Lista"
    
    context = ClientContext(site_url).with_credentials(
        ClientCredential(app_principal['client_id'], 
                         app_principal['client_secret']
        ))

    print("Iniciando extração da lista")
    
    # Obtendo a lista do SharePoint
    list_obj = context.web.lists.get_by_title(list_name)
    
    # Carregar os itens da lista (Paginação)
    items = list_obj.items.paged(500).get().execute_query()
    
    # Percorrendo lista
    data = []
    for item in items:
        data.append(item.properties)
        
    # Convertendo para Dataframe (se houver colunas passada via parâmetro, realiza o filtro)
    if cols:
        print("Filtrando Colunas")
        col_tratada = [col.split(':')[-1] for col in cols]
        cols = [col.split(':')[0] for col in cols]
        df = pd.DataFrame(data)[cols]
        df.rename(columns=dict(zip(cols, col_tratada)), inplace=True)
    else:
        print("Nao foram aplicados filtros.")
        df = pd.DataFrame(data)

    # Iniciando conversão para .csv
    print("Iniciando conversão para .csv")
    
    # Se o nome do arquivo.csv destino foi passado na target, utilizará como arquivo final
    print("Convertendo para .CSV")
    if '.csv' in target.lower():
        df.to_csv(target, sep=',', encoding='utf8')
    else:
        df.to_csv(os.path.join(target+list_name.replace(' ', '_').replace('-','_')+'.csv'), sep=',', encoding='utf8')

    print("Operação finalizada com sucesso!")
    
    
except Exception as e:
    print(f"Não foi possível conectar. Erro: {e}")
    raise("Não foi possível completar a operação! Sistema finalizado.")

