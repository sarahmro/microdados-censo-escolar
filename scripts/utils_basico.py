import pandas as pd


# Mapeamentos para deixar os valores legíveis nos CSVs de saída
DEPENDENCIA = {
    1: "Federal",
    2: "Estadual",
    3: "Municipal",
    4: "Privada"
}

LOCALIZACAO = {
    1: "Urbana",
    2: "Rural"
}


def carregar_dados(caminho: str) -> pd.DataFrame:
    """
    Lê o CSV de microdados do Censo Escolar com as configurações padrão.
    Seleciona apenas as colunas necessárias para reduzir uso de memória.
    """
    colunas = [
        "NU_ANO_CENSO",
        "SG_UF",
        "NO_UF",
        "NO_REGIAO",
        "TP_DEPENDENCIA",
        "TP_LOCALIZACAO",
        "QT_MAT_BAS_FEM",
        "QT_MAT_BAS_MASC",
        "QT_MAT_FUND",
        "QT_MAT_FUND_AI",
        "QT_MAT_FUND_AF",
        "QT_MAT_MED",
    ]

    df = pd.read_csv(
        caminho,
        sep=";",
        encoding="latin1",
        low_memory=False,
        usecols=colunas
    )

    # Filtra apenas escolas em funcionamento normal (remove registros inválidos)
    df = df[df["QT_MAT_BAS_FEM"].notna() | df["QT_MAT_BAS_MASC"].notna()].copy()

    # Preenche nulos de matrícula com 0
    for col in ["QT_MAT_BAS_FEM", "QT_MAT_BAS_MASC", "QT_MAT_FUND",
                "QT_MAT_FUND_AI", "QT_MAT_FUND_AF", "QT_MAT_MED"]:
        df[col] = df[col].fillna(0).astype(int)

    # Substitui códigos por descrições legíveis
    df["TP_DEPENDENCIA"] = df["TP_DEPENDENCIA"].map(DEPENDENCIA)
    df["TP_LOCALIZACAO"] = df["TP_LOCALIZACAO"].map(LOCALIZACAO)

    return df


def calcular_percentual(df: pd.DataFrame, col_fem: str, col_total: str) -> pd.Series:
    """Calcula o percentual feminino, tratando divisão por zero."""
    return (
        df[col_fem] / df[col_total] * 100
    ).where(df[col_total] > 0).round(2)