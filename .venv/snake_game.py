import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir o relogio para controle de tempo
relogio = pygame.time.Clock()

# Configurações iniciais
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))

# Cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
azul = (0, 0, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Lista de cores para a cobra
cores_cobra = [
    (255, 255, 255),  # Branco
    (0, 255, 0),      # Verde
    (0, 0, 255),      # Azul
    (255, 0, 0),      # Vermelho
    (255, 255, 0),    # Amarelo
    (255, 0, 255),    # Magenta
    (0, 255, 255),    # Ciano
]

# Parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15

# Funções auxiliares
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels, cor_cobra):
    for pixel in pixels:
        pygame.draw.rect(tela, cor_cobra, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [largura - texto.get_width() - 10, 10]) 

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

# Tela inicial
def tela_inicial():
    fonte_titulo = pygame.font.SysFont("Helvetica", 70)
    fonte_botao = pygame.font.SysFont("Helvetica", 50)
    fonte_nome = pygame.font.SysFont("Helvetica", 40)

    titulo = fonte_titulo.render("Bem-vindo ao Snake Game!", True, branca)
    botao_texto = fonte_botao.render("Pressione Enter para jogar", True, azul)
    nome_input_texto = fonte_nome.render("Digite seu nome:", True, branca)

    nome_usuario = ""
    caixa_nome = pygame.Rect(largura / 2 - 150, altura / 2 + 50, 300, 50)
    font = pygame.font.SysFont("Helvetica", 40)

    while True:
        tela.fill(preta)

        # Desenhar título
        tela.blit(titulo, [largura / 2 - titulo.get_width() / 2, altura / 4])

        # Caixa de entrada do nome do usuário
        pygame.draw.rect(tela, branca, caixa_nome, 2)
        nome_usuario_texto = font.render(nome_usuario, True, branca)
        tela.blit(nome_usuario_texto, (caixa_nome.x + 10, caixa_nome.y + 10))

        tela.blit(nome_input_texto, [largura / 2 - nome_input_texto.get_width() / 2, altura / 2])

        # Desenhar botão de jogar
        tela.blit(botao_texto, [largura / 2 - botao_texto.get_width() / 2, altura / 2 + 120])

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Adicionar letras ao nome do usuário
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Pressionar Enter para iniciar o jogo
                    return nome_usuario
                elif evento.key == pygame.K_BACKSPACE:
                    nome_usuario = nome_usuario[:-1]
                else:
                    nome_usuario += evento.unicode

# Função para rodar o jogo
def rodar_jogo(nome_usuario):
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()
    indice_cor = 0  # Índice da cor atual da cobra

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar a cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # se a cobrinha bateu no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # Verificar se deve mudar a cor da cobra
        if (tamanho_cobra - 1) % 10 == 0 and tamanho_cobra > 1:
            indice_cor = (tamanho_cobra // 10) % len(cores_cobra)

        desenhar_cobra(tamanho_quadrado, pixels, cores_cobra[indice_cor])

        # desenhar pontos
        desenhar_pontuacao(tamanho_cobra - 1)

        # mostrar nome do usuário
        fonte_nome = pygame.font.SysFont("Helvetica", 25)
        texto_nome = fonte_nome.render(f"Jogador: {nome_usuario}", True, branca)
        tela.blit(texto_nome, [10, 10])

        # atualização da tela
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

# Executar o jogo
nome_usuario = tela_inicial()
rodar_jogo(nome_usuario)
