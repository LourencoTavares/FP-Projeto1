# Jogo MNK (Fundamentos da Programação)

Projeto desenvolvido no âmbito da UC de **Fundamentos da Programação (2024/2025)**

## Descrição

Este projeto consiste na implementação de um jogo do tipo **m, n, k**, onde dois jogadores (humano vs computador) jogam alternadamente num tabuleiro de dimensão m×n, com o objetivo de alinhar **k peças consecutivas** na horizontal, vertical ou diagonal

O jogo é uma generalização de jogos clássicos como:
- Jogo do Galo (3x3, k=3)
- Gomoku (15x15, k=5)

---

## Objetivo

Desenvolver um programa em Python que:
- Representa e manipula o tabuleiro
- Permite jogar manualmente e automáticamente
- Implementa diferentes estratégias de jogo
- Determina o fim do jogo e o vencedor

---

## Funcionalidades Implementadas

- Validação de tabuleiro e posições
- Manipulação do tabuleiro (linhas, colunas, diagonais)
- Identificação de posições livres e ocupadas
- Verificação de sequências de k peças consecutivas
- Sistema de jogo completo (humano vs computador)
- Estratégia automática de jogo (nível fácil implementado)

---

## Estratégias de Jogo

O computador pode jogar com diferentes níveis de dificuldade:

- **Fácil**  
  - Joga em posições adjacentes às suas peças, se possível
  - Caso contrário, escolhe uma posição livre

*(Outras estratégias previstas no enunciado: normal e difícil)* 

---

## Estrutura do Projeto

- `FP2425P1.py` -> Código principal do projeto  
- `FP-2024-P1.pdf` -> Enunciado do projeto  

---

## Modos de Jogo

Na ultima linha do projeto alterar os valores, se pretendido:

- `(3,3,3)` -> configuração do jogo:
  - `1º valor (m)`: número de linhas
  - `2º valor (n)`: número de colunas
  - `3º valor (k)`: número de peças consecutivas necessárias para ganhar
- `1` -> jogador humano:
  - `1` = joga com 'X' (começa primeiro)
  - `(-1)` = joga com 'O'
- Modos de Jogo:
  - `'facil'` -> jogadas simples
  - `'normal'` -> estratégia intermédia (não implementada)
  - `'dificil'` -> estratégia avançada (não implementada)

---

## Como executar

1. Abrir o ficheiro Python no terminal:

``python3 FP2425P1.py`` para Mac/Linux ou ``python FP2425P1.py`` para Windows
