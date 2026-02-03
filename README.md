# Simulação de Fluxo de Trânsito com Autômatos Celulares

## Descrição

Este projeto implementa uma simulação computacional do fluxo de veículos utilizando **Autômatos Celulares**, com base no modelo clássico de **Nagel-Schreckenberg**. O objetivo é analisar o comportamento do trânsito em uma via unidimensional por meio de regras locais simples que geram padrões emergentes complexos, como congestionamentos espontâneos.

O sistema permite visualizar o movimento dos veículos, além de coletar dados estatísticos e gerar gráficos científicos para análise do comportamento do tráfego.

---

## Objetivos

- Simular o fluxo de trânsito utilizando autômatos celulares
- Analisar o impacto da densidade veicular no desempenho do sistema
- Observar padrões emergentes de congestionamento
- Gerar métricas científicas como:
  - Velocidade média
  - Fluxo de veículos
  - Relação fluxo × densidade

---

## Fundamentação Teórica

O modelo utilizado é baseado no modelo **Nagel-Schreckenberg**, amplamente empregado na modelagem de tráfego rodoviário. Ele representa a estrada como uma estrutura discreta composta por células que podem estar vazias ou ocupadas por veículos.

A dinâmica do sistema é definida por quatro regras principais:

1. Aceleração dos veículos  
2. Prevenção de colisões  
3. Comportamento estocástico do motorista  
4. Atualização simultânea do sistema  

---

## Funcionalidades

- ✔ Simulação visual do trânsito  
- ✔ Coleta automática de dados estatísticos  
- ✔ Geração de gráficos científicos  
- ✔ Modelo baseado em autômato celular  
- ✔ Estrutura modular e orientada a objetos  

---

## Estrutura do Projeto

traffic_automata/
│
├── simulation.py # Modelo do autômato celular
├── visualization.py # Animação da simulação
├── analysis.py # Geração de gráficos científicos
├── main.py # Arquivo principal
├── requirements.txt
└── README.md

## Instalação

Clone o repositório:

git clone https://github.com/SEU-USUARIO/traffic-automata.git

---

Entre na pasta do projeto:

cd traffic-automata

---

Instale as dependências:

pip install -r requirements.txt

---
Como Executar:

python main.py

