# Snake Game Python

Este é um clássico jogo da cobra desenvolvido em Python com a biblioteca Pygame. O jogador controla uma cobra que se move pela tela, comendo comida para aumentar de tamanho e evitando colisões com as paredes e com o próprio corpo. O jogo apresenta uma tela inicial para inserir o nome do jogador e cores dinâmicas para a cobra.

## Funcionalidades

*   **Tela Inicial:** Permite ao jogador inserir seu nome antes de iniciar o jogo.
*   **Movimentação:** Controle da cobra usando as setas do teclado (cima, baixo, esquerda, direita).
*   **Crescimento:** A cobra aumenta de tamanho ao comer a comida.
*   **Colisões:** Detecção de colisões com as paredes e com o próprio corpo, resultando no fim do jogo.
*   **Pontuação:** Exibição da pontuação na tela, aumentando a cada comida consumida.
*   **Cores Dinâmicas:** A cor da cobra muda a cada 10 pontos.
*   **Nome do Jogador:** Exibe o nome do jogador na tela durante o jogo.

## Tecnologias Utilizadas

*   Python
*   Pygame

## Como Executar

1.  Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).
2.  Instale a biblioteca Pygame:

    ```bash
    pip install pygame
    ```

3.  Clone o repositório ou baixe o arquivo `snake_game.py`.
4.  Navegue até o diretório onde o arquivo está salvo no terminal.
5.  Execute o jogo:

    ```bash
    python snake_game.py
    ```

## Estrutura do Projeto

O projeto consiste em um único arquivo:

*   `snake_game.py`: Contém todo o código do jogo.

## Código-Fonte (Trechos Importantes)

Abaixo, alguns trechos importantes do código com comentários explicativos:

```python
import pygame
import random

# Inicializar o Pygame
pygame.init()



# Função para gerar a comida em posições aleatórias
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

# Função para desenhar a cobra
def desenhar_cobra(tamanho, pixels, cor_cobra):
    for pixel in pixels:
        pygame.draw.rect(tela, cor_cobra, [pixel[0], pixel[1], tamanho, tamanho])

# ... (Outras funções: desenhar_comida, desenhar_pontuacao, selecionar_velocidade, tela_inicial, rodar_jogo)

# Execução principal do jogo
nome_usuario = tela_inicial()
rodar_jogo(nome_usuario)