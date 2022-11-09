import pyautogui as py
import psutil as ps





path_Arquivo_base = r'/Projeto/Imagens/Arqui_base.PNG'
path_Arquivo_script = r'/ProjetoAutomacao/Firmware\SCRIPT_CALIBRICAO_OFSSET.txt'
path_Button_atualizar = r'/Projeto/Imagens/Button_atualizar.png'
path_Button_relig = r'/Projeto/Imagens/Button_relig.png'
path_Button_atufirmware = r'/Projeto/Imagens/Button_atufirmware.png'
path_Caminho = r'/ProjetoAutomacao/Firmware\UPS-AV3-R16-v6.7.5.16032022[APP].out'
path_Button_atumodUPS = r'/Projeto/Imagens/Button_atumodUPS.png'
path_Button_arq_firmware = r'/Projeto/Imagens/Button_arq_firmware.PNG'
path_Button_confgcaboserial_01 = r'/Projeto/Imagens/Button_confgcaboserial_01.png'
path_Button_confgcaboserial_02 = r'/Projeto/Imagens/Button_confgcaboserial_02.PNG'
path_Vel_conecxao_19200 = r'/Projeto/Imagens/Vel_conecxao_19200.PNG'
path_Vel_conecxao_57600 = r'/Projeto/Imagens/Vel_conexao_57600.PNG'
path_Button_conectar_agora = r'/Projeto/Imagens/Button_conectar_agora.PNG'
path_Button_fechar = r'/Projeto/Imagens/Button_fechar.PNG'
path_Button_fechar_03 = r'/Projeto/Imagens/Button_fechar_03.PNG'
path_Button_Envio_Recebimento = r'/Projeto/Imagens/Button_Envio_Recebimento.PNG'
path_Button_enviar = r'/Projeto/Imagens/Button_enviar.png'
path_Icon_Arquivos_Enviado_Com_Sucesso = r'/Projeto/Imagens/Icon_Arquivos_Enviado_Com_Sucesso.PNG'
path_Butto_oK = r'/Projeto/Imagens/Button_ok.PNG'
path_Button_Modo_console = r'/Projeto/Imagens/Button_Modo_console.png'
path_Butto_Entrar = r'/Projeto/Imagens/Button_Entrar.PNG'
path_Button_Carregar_Script = r'/Projeto/Imagens/Button_Carregar_Script.PNG'
path_Script = r'/ProjetoAutomacao/Firmware\SCRIPT_CALIBRICAO_OFSSET.txt'
path_Button_Rodar_script = r'/Projeto/Imagens/Button_Rodar_script.PNG'
path_Button_avancado = r'/Projeto/Imagens/Button_avancado.png'
path_Button_arq_logica = r'/Projeto/Imagens/Button_arq_logica.PNG'
path_Button_Enviar_arq_logica = r'/Projeto/Imagens/Button_enviar_avancado.png'
path_Button_voltar = r'/Projeto/Imagens/Button_voltar.PNG'
path_Button_conexao = r'/Projeto/Imagens/Button_conexao.PNG'
path_Button_desconectar = r'/Projeto/Imagens/Button_desconectar.PNG'
path_information_firmwareatualizadocomsucesso = r'/Projeto/Imagens/Information_firmwareatualizadocomsucesso.PNG'
path_information_fimdaatualizacao = r'/Projeto/Imagens/Information_fimdaatualizacao.PNG'
path_information_concluido = r'/Projeto/Imagens/Information_concluido.PNG'
path_Button_fechar_01 = r'/Projeto/Imagens/Button_fechar_01.PNG'
path_Button_ok_UPS = r'/Projeto/Imagens/Button_ok_UPS.PNG'
path_Button_enviar_todas = r'/Projeto/Imagens/Button_Env_Todas_as_conexoes.PNG'
path_Button_conectar_TCPIP = r'/Projeto/Imagens/Button_conectar_TCPIP.PNG'
path_Button_conectar_cabo_serial = r'/Projeto/Imagens/Button_conectar_cabo_serial.PNG'

def localiza_and_click(a):

 x = py.locateCenterOnScreen(a,grayscale=True, confidence = 0.9)
 py.leftClick(x)
 py.sleep(1)


##Abrir Lupa

#Ao rodar o scrip o código deve verificar quais os programas etão e execução e identicar o lupareligador.exe
#Assim que for idC:\ Users\ rubens.araujo\PycharmProjects\pythonProject1\Projeto\Firmware\UPS-AV3-R16-v6.7.0.02022020[APP].out
#entificado e o seu status estiver como running ele deve iniciar o processo de atualização.
#Senão será necessário que ele abra o software e execute  todo o restante do scrip

##Verificando se o software Lupa Religador está ou não em execução

stat = { 'name': '','status':''}


for proc in ps.process_iter():

    info = proc.as_dict(attrs=['name','status'])

    if info['name'] == 'lupareligador.exe' and info['status'] == 'running':

        stat = info

#----------------------------------------------------------------------------------------------------------------------#
##Caso o software já esteja aberto seguirá esse caminho

if stat['name'] == 'lupareligador.exe' and stat['status'] == 'running':

#mudando de aba para iniciar o processo
#Talvez essa etapa seja subistituida por outra forma de buscar mais eficas.

    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')

#----------------------------------------------------------------------------------------------------------------------#

##Senão ele será iniciado pelo script

else:
#Abrindo o programa pelo windols

    py.press('win')
    py.sleep(1)
    py.write('LUPA RELIGADOR 6.0.19 RC4')
    py.sleep(1)
    py.press('enter')
    py.sleep(35)


    ##Selecionar arquivo de base
    ##Nesta solução o arquivo slecionado é o ultimo adionando, isto é um ponto de atenção

    localiza_and_click(path_Button_relig)
    py.sleep(2)

    localiza_and_click(path_Arquivo_base)
    py.sleep(5)

#----------------------------------------------------------------------------------------------------------------------#

##Atualizar firmware da UPS

##Encontrando o botão relig

localiza_and_click(path_Button_relig)

#Selecionando o comando o botão de atualização firmware

localiza_and_click(path_Button_atufirmware)

#Selecionando o botão atualizar módulo UPS

localiza_and_click(path_Button_atumodUPS)

##Selecionar a porta de comexão

    ##Trbalhando nesta etapa

py.moveTo(369,234)
py.leftClick()
py.sleep(1)

py.moveTo(346,255)
py.leftClick()
py.sleep(1)

##Selecionar a velocidade de conexão

py.moveTo(466,234)
py.leftClick()
py.sleep(1)

py.moveTo(451,329)
py.leftClick()
py.sleep(1)


#Selecionar o arquivo de atualização da UPS

localiza_and_click(path_Button_arq_firmware)

py.write(path_Caminho)
py.sleep(1)
py.press('enter')
py.sleep(1)

#Selecionando o botão atualizar UPS

localiza_and_click(path_Button_atualizar)
py.sleep(235)

#Finalizar processo de atualização da UPS


Status_atualizacao_UPS_00  = py.locateCenterOnScreen(path_information_firmwareatualizadocomsucesso)

if Status_atualizacao_UPS_00 != 'none':

    localiza_and_click(path_Button_ok_UPS)
    py.sleep(2)

Status_atualizacao_UPS_01  = py.locateCenterOnScreen(path_information_fimdaatualizacao)

if Status_atualizacao_UPS_01 != 'none':

    localiza_and_click(path_Button_ok_UPS)
    py.sleep(2)

Status_atualizacao_UPS_02  = py.locateCenterOnScreen(path_information_concluido)
py.sleep(1)

if Status_atualizacao_UPS_02 != 'none':

    #localiza_and_click(path_Button_fechar_01)
    py.leftClick(1060,346)
    py.sleep(2)

localiza_and_click(path_Button_fechar_01)
py.sleep(2)

localiza_and_click(path_Button_fechar_01)
py.sleep(2)

#----------------------------------------------------------------------------------------------------------------------#

##Iniciar o processo de conexão via cabo serial

#Selecionando o botão de configuração serial

info = py.locateCenterOnScreen(path_Button_confgcaboserial_01)
py.sleep(1)

if info != 'none':
    localiza_and_click(path_Button_confgcaboserial_01)
    print('um')

else:
    localiza_and_click(path_Button_confgcaboserial_02)
    print('dois')

#Definindo a porta de conexão

py.moveTo(329,270)
py.sleep(1)
py.leftClick()
py.moveTo(329,287)
py.leftClick()

#Definindo a velocidade de conexão

py.moveTo(322,300)
py.sleep(1)
py.leftClick()
py.sleep(1)

##Ao inves de mostrar qual é a posição indiquei o que deve ser procurado na tela

localiza_and_click(path_Vel_conecxao_57600)

#Conectar agora

localiza_and_click(path_Button_conectar_agora)
py.sleep(6)

#Fechar informação de conexão

info = py.locateCenterOnScreen(path_Button_fechar_03)

if info != 'none':

    localiza_and_click(path_Button_fechar_03)
    print('1')
    
else:

    py.press('Enter')
    print('2')

#----------------------------------------------------------------------------------------------------------------------#

##Iniciar o processo de rodar o script

#Localizar o botaão Modo Console

localiza_and_click(path_Button_Modo_console)

#Carregar script

localiza_and_click(path_Button_Carregar_Script)

#Abrir o arquivo de scrip

py.write(path_Script)
py.sleep(1)
py.press('enter')
py.sleep(1)
    #Essa etapa foi necessária pois o software não esta identificandi o próximo passo

py.moveTo(655,414)

#Entrar no modo console

py.sleep(1)
localiza_and_click(path_Butto_Entrar)
    #Essa etapa foi necessária pois o software não esta identificando o próximo passo
py.moveTo(655,414)

#Rodar o script carregado

localiza_and_click(path_Button_Rodar_script)
py.sleep(65)

#Finalizar o precesso de execução do script

localiza_and_click(path_Button_fechar)
py.sleep(1)

#----------------------------------------------------------------------------------------------------------------------#

#localiza_and_click(path_Button_desconectar)

Status_envio_base = py.locateCenterOnScreen(path_Button_desconectar)
py.sleep(2)

if Status_envio_base != 'none':

    localiza_and_click(path_Button_desconectar)
    print('1')

else:

    py.moveTo(343, 97)
    py.leftClick()
    print('2')

localiza_and_click(path_Button_conectar_TCPIP)

#py.moveTo(506,92)
#py.leftClick()
#py.sleep(1)

#----------------------------------------------------------------------------------------------------------------------#

##Iniciar o processo de conexão via cabo serial

#Selecionando o botão de configuração serial

localiza_and_click(path_Button_conectar_cabo_serial)

#py.moveTo(206,101)
#py.leftClick()
#py.sleep(1)

Status_envio_base = py.locateCenterOnScreen(path_Button_enviar_todas)
py.sleep(2)

if Status_envio_base != 'none':

    localiza_and_click(path_Button_enviar_todas)
    print('1')

else:

    py.moveTo(343,97)
    py.leftClick()
    print('2')

py.sleep(110)

#Finalizar processo de enviar todas

Status_envio_base = py.locateCenterOnScreen(path_Icon_Arquivos_Enviado_Com_Sucesso)
py.sleep(1)

if Status_envio_base != 'none':

    localiza_and_click(path_Butto_oK)
    print('1')

else:
    py.press('enter')
    py.sleep(1)
    print('2')


#----------------------------------------------------------------------------------------------------------------------#

##Iniciar o processo de envio da lógica

#Localizar o botão avançado

localiza_and_click(path_Button_avancado)

#Localizar o botão arquivos de logica

localiza_and_click(path_Button_arq_logica)

#Enviar arquivos de lógica

localiza_and_click(path_Button_Enviar_arq_logica)
py.sleep(45)

#Finalizar processo de envio de arquivos de lógica

Status_envio_base = py.locateCenterOnScreen(path_Icon_Arquivos_Enviado_Com_Sucesso)
py.sleep(1)

if Status_envio_base != 'none':

    localiza_and_click(path_Butto_oK)
    print('1')
else:
    py.press('enter')
    print('2')

localiza_and_click(path_Button_voltar)

#----------------------------------------------------------------------------------------------------------------------#

##Finalizar processo

#Localizar a aba conexão

localiza_and_click(path_Button_conexao)

#localiza_and_click(path_Button_desconectar)

Status_envio_base = py.locateCenterOnScreen(path_Button_desconectar)
py.sleep(2)

if Status_envio_base != 'none':

    localiza_and_click(path_Button_desconectar)
    print('1')

else:

    py.moveTo(343,97)
    py.leftClick()
    print('2')


