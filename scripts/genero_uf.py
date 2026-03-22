import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from utils_basico import carregar_dados, calcular_percentual

anos = ["2020", "2021", "2022", "2023", "2024"]

base_dir = os.path.dirname(os.path.dirname(__file__))

for ano in anos:
    print(f"Processando gênero por UF - {ano}")

    caminho_dados = f"{base_dir}/dados/{ano}/microdados_ed_basica_{ano}.CSV"
    pasta_saida = f"{base_dir}/resultados/{ano}"
    os.makedirs(pasta_saida, exist_ok=True)

    df = carregar_dados(caminho_dados)

    df_final = df.groupby(
        ["SG_UF", "NO_UF", "NO_REGIAO"],
        as_index=False
    ).agg(
        QT_MAT_BAS_FEM=("QT_MAT_BAS_FEM", "sum"),
        QT_MAT_BAS_MASC=("QT_MAT_BAS_MASC", "sum"),
        QT_MAT_FUND=("QT_MAT_FUND", "sum"),
        QT_MAT_FUND_AI=("QT_MAT_FUND_AI", "sum"),
        QT_MAT_FUND_AF=("QT_MAT_FUND_AF", "sum"),
        QT_MAT_MED=("QT_MAT_MED", "sum"),
    )

    df_final["QT_MAT_BAS_TOTAL"] = df_final["QT_MAT_BAS_FEM"] + df_final["QT_MAT_BAS_MASC"]
    df_final["PERC_FEM"] = calcular_percentual(df_final, "QT_MAT_BAS_FEM", "QT_MAT_BAS_TOTAL")
    df_final["ANO"] = int(ano)

    df_final = df_final[[
        "ANO", "NO_REGIAO", "SG_UF", "NO_UF",
        "QT_MAT_BAS_FEM", "QT_MAT_BAS_MASC", "QT_MAT_BAS_TOTAL",
        "PERC_FEM",
        "QT_MAT_FUND", "QT_MAT_FUND_AI", "QT_MAT_FUND_AF", "QT_MAT_MED"
    ]].sort_values(by=["NO_REGIAO", "SG_UF"])

    df_final.to_csv(
        f"{pasta_saida}/genero_uf_{ano}.csv",
        sep=";", index=False, encoding="utf-8-sig"
    )

    print(f"{ano} concluído. {len(df_final)} estados.")

print("Arquivos de gênero por UF gerados.")