# 📊 Análise de Dados do Censo Escolar (INEP)
##  Objetivo
Este projeto realiza o processamento dos microdados do Censo Escolar com foco na análise de matrículas no ensino básico, considerando:
- Gênero (masculino e feminino)
- Estado (UF)
- Ano

O objetivo principal é investigar a distribuição de matrículas por gênero ao longo do tempo, permitindo análises sobre participação e possíveis desigualdades no ensino básico brasileiro.

📁 Estrutura do Projeto
microdados-censo-escolar/
│  
├── dados/                # Microdados do Censo Escolar (não versionados)  
│   ├── 2020/  
│   ├── 2021/  
│   ├── 2022/  
│   ├── 2023/  
│   └── 2024/  
│  
├── resultados/           # Arquivos gerados pelos scripts (não versionados)  
│   ├── 2020/  
│   ├── 2021/  
│   ├── 2022/  
│   ├── 2023/  
│   ├── 2024/  
│   └── consolidado/  
│  
└── scripts/              # Scripts para processamento dos dados  
    ├── consolidar_anos.py  
    ├── genero_dependencias.py  
    ├── genero_localizacao.py  
    ├── genero_uf.py  
    └── utils_basico.py
    
⚠️ As pastas dados/ e resultados/ não estão no repositório devido ao tamanho dos arquivos.

##  Fonte dos Dados
Os microdados são disponibilizados pelo
Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

Download oficial:
[Microdados do Censo Escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)  
Pasta no Drive com os Microdados: [Microdados INEP](https://drive.google.com/drive/folders/1FLd-5qgK4JRAfQCTEELMrkkD__2R2QWI?usp=sharing)

##  Como executar os scripts
###  1. Baixar os microdados
Organize os arquivos na estrutura:
dados/  
├── 2020/  
├── 2021/  
├── 2022/  
├── 2023/  
└── 2024/  

###  2. Executar os scripts de processamento
Os scripts devem ser executados na seguinte ordem:  

#### 📌 Etapa 1 — Processamento por gênero
````
python scripts/genero_uf.py
python scripts/genero_dependencias.py
python scripts/genero_localizacao.py
````

Esses scripts geram os dados de matrículas por gênero considerando diferentes recortes:  
- Por estado (UF)
- Por dependência administrativa
- Por localização (urbano/rural, se aplicável)

#### 📌 Etapa 2 — Consolidação dos anos

Após executar todos os scripts de gênero:  
````
python scripts/consolidar_anos.py
````  
Este script:  
- Junta os dados de diferentes anos
- Gera séries históricas consolidadas


###  3. Saída dos dados
Os arquivos serão gerados na pasta:
resultados/  
├── 2020/  
├── 2021/  
├── 2022/  
├── 2023/  
├── 2024/  
└── consolidado/  
  
⚠️ Os scripts de consolidação dependem da execução prévia dos scripts de processamento por gênero.  


##  Tecnologias utilizadas
- Python 3.x
- Pandas
- Git / GitHub
