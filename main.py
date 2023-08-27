import pygame
from sys import exit
from random import randint

def mostra_tempo():
    tempo_atual = int(pygame.time.get_ticks() / 1000) - tempo_inicio
    cont_regr = cont_base - tempo_atual
    tempo = fonte_inicio.render(f'Tempo: {cont_regr}', False, ("black"))
    tempo_rect = tempo.get_rect(center = (400, 50))
    tela.blit(tempo, tempo_rect)
    return (cont_regr)

def mostra_conta(val1, val2):
    resultado = val1 * val2

    return resultado

def pula_planta1(num_id):
    global cont_base
    global jogo_ativo
    global num_ale1
    global num_ale2
    global num_tela1
    global num_tela2
    global num_certo
    global num_err
    global id
    global erro_sinal
    global pontos
    
    global pontos_tela
    global ult_pont
    if planta_rect1.collidepoint(event.pos):
        sapo_rect.center = planta_rect1.center    
        if num_id == 0:
            cont_base += (5 - mostra_tempo())
            sapo_rect.center = planta_rect.center
            id = randint(0, 1)
            erro_sinal = randint(0, 1)
            num_ale1 = randint(1, 10)
            num_ale2 = randint(1, 10)
            pontos += 1
            num_tela1 = fonte_inicio.render(f'{num_ale1}', False, (0, 40, 0))
            num_tela2 = fonte_inicio.render(f'{num_ale2}', False, (0, 40, 0))
            num_certo = fonte_inicio.render(f'{mostra_conta(num_ale1, num_ale2)}', False, (0, 40, 0))
            num_err = fonte_inicio.render(f'{valor_errado()}', False, (0, 40, 0))
            pontos_tela = fonte_inicio .render(f'Pontos: {pontos}', False, (0, 40, 0))
            ult_pont = fonte_inicio.render(f'Ultima  pontuacao: {pontos}', False, (77, 78, 0))
            pulo.play()
        else:
            jogo_ativo = False

def pula_planta2(num_id):
    global cont_base
    global jogo_ativo
    global num_ale1
    global num_ale2
    global num_tela1
    global num_tela2
    global num_certo
    global num_err
    global id
    global erro_sinal
    global pontos
    global pontos_tela
    global ult_pont
    if planta_rect2.collidepoint(event.pos):
        sapo_rect.center = planta_rect2.center
        if num_id == 1:
            cont_base += (5 - mostra_tempo())
            sapo_rect.center = planta_rect.center
            id = randint(0, 1)
            erro_sinal = randint(0, 1)
            num_ale1 = randint(1, 10)
            num_ale2 = randint(1, 10)
            pontos += 1
            num_tela1 = fonte_inicio.render(f'{num_ale1}', False, (0, 40, 0))
            num_tela2 = fonte_inicio.render(f'{num_ale2}', False, (0, 40, 0))
            num_certo = fonte_inicio.render(f'{mostra_conta(num_ale1, num_ale2)}', False, (0, 40, 0))
            num_err = fonte_inicio.render(f'{valor_errado()}', False, (0, 40, 0))
            pontos_tela = fonte_inicio .render(f'Pontos: {pontos}', False, (0, 40, 0))
            ult_pont = fonte_inicio.render(f'Ultima  pontuacao: {pontos}', False, (77, 78, 0))
            pulo.play()
        else:
            jogo_ativo = False

def valor_correto():
    global id
    if id == 0:
        num_certo_rect.center = (200, 260)
        num_err_rect.center = (600, 260)
        tela.blit(num_certo, num_certo_rect)
        tela.blit(num_err, num_err_rect)
    else:
        num_certo_rect.center = (600, 260)
        num_err_rect.center = (200, 260)
        tela.blit(num_certo, num_certo_rect)
        tela.blit(num_err, num_err_rect)

def valor_errado():
    global erro_sinal
    global valor_erro
    erro_sinal = randint(0, 1)
    if erro_sinal == 0:
        valor_erro = mostra_conta(num_ale1, num_ale2) - randint(1, 10)
        return valor_erro
    else:
        valor_erro = mostra_conta(num_ale1, num_ale2) + randint(1, 10)
        return valor_erro


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Math Jump")

clock = pygame.time.Clock()
fonte_inicio = pygame.font.Font("./assets/Pixeltype.ttf", 50)
jogo_ativo = False
tempo_inicio = 0

cont_base = 5

id = randint(0, 1)

pontos = 0

fundo_tela = pygame.image.load("./assets/lago.png").convert_alpha()

fundo_mus = pygame.mixer.Sound("./assets/music_track_Gameplay.mp3")

sapo = pygame.image.load("./assets/sapo_sprite.png").convert_alpha()
sapo_rect = sapo.get_rect(center = (400, 460))

pulo = pygame.mixer.Sound("./assets/sfx_classic_jump.wav")

sapo_inicio = pygame.image.load("./assets/sapo_inicio.png").convert_alpha()
sapo_inicio_maior = pygame.transform.scale2x(sapo_inicio)
sapo_inicio_rect = sapo_inicio_maior.get_rect(midbottom = (400, 500))

nome_jogo = fonte_inicio.render("Math Jump", False, (77, 78, 0))
nome_jogo_maior = pygame.transform.scale2x(nome_jogo)
nome_jogo_rect = nome_jogo_maior.get_rect(center = (400, 100))

instr_jogo = fonte_inicio.render("Clique na tela para jogar!", False, (77, 78, 0))
instr_jogo_rect = instr_jogo.get_rect(center = (400, 200))

planta = pygame.image.load("./assets/planta.png").convert_alpha()
planta_maior = pygame.transform.rotozoom(planta, 0, 1.5)
planta_rect = planta_maior.get_rect(center = (400, 480))
planta_rect1 = planta_maior.get_rect(center = (200,170))
planta_rect2 = planta_maior.get_rect(center = (600, 170))

base_num = pygame.image.load("./assets/base_num.png").convert_alpha()
base_rect = base_num.get_rect(center = (340, 565))
base_rect2 = base_num.get_rect(center = (460, 565))
base_res1 = base_num.get_rect(center = (200, 255))
base_res2 = base_num.get_rect(center = (600, 255))

num_ale1 = randint(1, 10)
num_ale2 = randint(1, 10)

num_tela1 = fonte_inicio.render(f'{num_ale1}', False, (0, 40, 0))
num_tela2 = fonte_inicio.render(f'{num_ale2}', False, (0, 40, 0))
num_tela1_rect = num_tela1.get_rect(center = (340, 570))
num_tela2_rect = num_tela2.get_rect(center = (460, 570))

num_certo = fonte_inicio.render(f'{mostra_conta(num_ale1, num_ale2)}', False, (0, 40, 0))
num_certo_rect = num_certo.get_rect(center = (200, 260))
num_err = fonte_inicio.render(f'{valor_errado()}', False, (0, 40, 0))
num_err_rect = num_err.get_rect(center = (600, 260))

sinal_x = fonte_inicio.render("X", False, (0, 40, 0))
sinal_x_rect = sinal_x.get_rect(center = (400, 570))

pontos_tela = fonte_inicio.render(f'Pontos: {pontos}', False, (0, 40, 0))
pontos_tela_rect = pontos_tela.get_rect(center = (400, 85))

ult_pont = fonte_inicio.render(f'Ultima  pontuacao: {pontos}', False, (77, 78, 0))
ult_pont_rect = ult_pont.get_rect(center = (400, 150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if jogo_ativo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pula_planta1(id)
                pula_planta2(id)

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogo_ativo = True
                sapo_rect.center = (400, 460)
                cont_base = 5
                tempo_inicio = int(pygame.time.get_ticks() / 1000)
                pontos = 0
                pontos_tela = fonte_inicio .render(f'Pontos: {pontos}', False, (0, 40, 0))
                fundo_mus.play(loops = -1)

    if jogo_ativo:

        tela.blit(fundo_tela, (0, 0))
        tela.blit(fundo_tela, (0, 200))
        tela.blit(fundo_tela, (0, 400))

        tela.blit(planta_maior, planta_rect)
        tela.blit(planta_maior, planta_rect1)
        tela.blit(planta_maior, planta_rect2)

        tela.blit(sapo, sapo_rect)

        tela.blit(base_num, base_rect)
        tela.blit(base_num, base_rect2)
        
        tela.blit(base_num, base_res1)
        tela.blit(base_num, base_res2)

        tela.blit(num_tela1, num_tela1_rect)
        tela.blit(num_tela2, num_tela2_rect)

        tela.blit(sinal_x, sinal_x_rect)

        tela.blit(pontos_tela, pontos_tela_rect)
        
        valor_correto()
        
        if mostra_tempo() < 0:
            jogo_ativo = False
        
    else:
        tela.fill((47, 182, 102))
        tela.blit(nome_jogo_maior, nome_jogo_rect)
        tela.blit(instr_jogo, instr_jogo_rect)
        tela.blit(sapo_inicio_maior, sapo_inicio_rect)
        fundo_mus.stop()
        if pontos > 0:
            tela.blit(ult_pont, ult_pont_rect)

    pygame.display.update()
    clock.tick(60)
