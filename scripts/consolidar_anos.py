import pandas as pd
import os

anos = ["2020", "2021", "2022", "2023", "2024"]

base_dir = os.path.dirname(os.path.dirname(__file__))
pasta_saida = f"{base_dir}/resultados/consolidado"
os.makedirs(pasta_saida, exist_ok=True)

arquivos = [
    ("genero_uf",          "genero_uf_2020_2024.csv"),
    ("genero_dependencia", "genero_dependencia_2020_2024.csv"),
    ("genero_localizacao", "genero_localizacao_2020_2024.csv"),
]

for prefixo, nome_saida in arquivos:
    lista = []

    print(f"\nConsolidando {prefixo}...")

    for ano in anos:
        caminho = f"{base_dir}/resultados/{ano}/{prefixo}_{ano}.csv"
        print(f"  Procurando arquivo de {ano}.")

        if os.path.exists(caminho):
            df = pd.read_csv(caminho, sep=";")
            lista.append(df)
            print(f"  {ano} adicionado.")
        else:
            print(f"Arquivo NÃO encontrado para {ano}.")

    if len(lista) == 0:
        print(f"Nenhum arquivo encontrado para consolidar ({prefixo}).")
    else:
        df_final = pd.concat(lista, ignore_index=True)
        df_final = df_final.sort_values(by=["ANO", "NO_REGIAO", "SG_UF"])

        df_final.to_csv(
            f"{pasta_saida}/{nome_saida}",
            sep=";", index=False, encoding="utf-8-sig"
        )

        print(f"Consolidado gerado: {nome_saida} ({len(df_final)} registros).")

print("\nConsolidação concluída.")