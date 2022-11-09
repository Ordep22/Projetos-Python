import pyautogui as py


##Abrir Lupa
##Esta parte será necessária somente ao inciar o script
'''
py.press('win')
py.sleep(1)
py.write('LUPA RELIGADOR 6.0.19 RC4')
py.sleep(1)
py.press('enter')
py.sleep(25)
py.alert(title='O software Lupa religador foi inciado,aguarde e pressione enter')
'''
##Selecionar arquivo de base
##Somenta para o desenvolvimento do código


py.keyDown('alt')
py.press('tab')
py.keyUp('alt')


#a = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_relig.png')
#py.leftClick(a)
#py.sleep(1)

#Selecionar o arquivo
##Nesta solução o arquivo slecionado é o ultimo adionando, isto é um ponto de atenção
#py.sleep(1)
#b = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Arqui_base.PNG')
#py.leftClick(b)


##Iniciar o processo de atualização do firmeware da UPS

##------------------------------------------##

##Atualizar firmware
##Encontrando o botaão relig

#x = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_relig.png')
#py.leftClick(x)
#py.sleep(1)

#Selecionando o comando o botão de atualização firmware

#y = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_atufirmware.png')
#py.leftClick(y)
#py.sleep(1)

#Selecionando o botão atualizar módulo UPS

#z = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_atumodUPS.png')
#py.leftClick(z)
#py.sleep(1)

##Selecionar a porta de comexão

#py.moveTo(369,234)
#py.leftClick()
#py.sleep(1)

#py.moveTo(346,255)
#py.leftClick()
#py.sleep(1)

##Selecionar a velocidade de conexão

#py.moveTo(466,234)
#py.leftClick()
#py.sleep(1)

#py.moveTo(442,307)
#py.leftClick()
#py.sleep(1)



#Selecionar o arquivo de atualização da UPS

'''
py.moveTo(905,299)
py.leftClick()
py.sleep(1)


py.moveTo(397,342)
py.leftClick()
py.sleep(1)


py.moveTo(683, 590)
py.sleep(1)
py.leftClick()
'''

#caminho = (r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Firmware\UPS-AV3-R16-v6.7.0.02022020[APP].out')

'''
py.write(caminho)
py.sleep(1)
py.press('enter')
py.sleep(1)
'''


#Selecionando o botão atualizar UPS

#py.sleep(1)
#a = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_atualizar.png')
#py.leftClick(a)

#Finalizar processo de atualização da UPS

#py.sleep(1)
#c,d= py.locateCenterOnScreen(r'C:\ Users\ rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_ok.png')
#py.leftClick(c,d)


##Iniciar o processo de conexão via cabo serial

#Selecionando o botão de configuração serial

x = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_confgcaboserial.png')
py.leftClick(x)

#Definindo a porta de conexão
'''
py.moveTo(329,270)
py.sleep(1)
py.leftClick()
py.moveTo(329,287)
py.leftClick()
'''

#Definindo o velocidade de conexão

py.moveTo(322,300)
py.sleep(1)
py.leftClick()
py.sleep(1)
##Ao inves de mostrar qual é a posição indiquei o que deve ser procurado na tela
x = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Vel_conecxao_19200.PNG')
py.sleep(1)
py.leftClick(x)

#clicar em conectar agora

x = py.locateCenterOnScreen(r'C:\Users\rubens.araujo\PycharmProjects\pythonProject1\Projeto\Imagens\Button_conectar_agora.PNG')
py.leftClick(x)








