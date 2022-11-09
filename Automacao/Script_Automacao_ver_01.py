import os.path

import pyautogui as py
import pandas as pd
import os



##Abrir Lupa
##Esta parte será necessária somente ao inciar o script
##Posteriormente será necessário verificar se o progrema já esta em execução
'''
py.press('win')
py.sleep(1)
py.write('LUPA RELIGADOR 6.0.19 RC4')
py.sleep(1)
py.press('enter')
py.sleep(25)
py.alert(title='O software Lupa religador foi inciado,aguarde! (pressione enter)')
'''

##Iniciar o processo de atualização do firmeware da UPS
##posição do botãp RELIG  = (194,49)

##Somenta para o desenvolvimento do código

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')

##------------------------------------------##
'''
py.moveTo(194,49)
py.leftClick()

##Clicando em tualização de firmeware
py.moveTo(226,289)
py.leftClick()
py.sleep(1)

##Clicando em atualizar firmeware da UPS
py.moveTo(677, 405)
py.leftClick()
py.sleep(1)


##Selecionar a porta de comexão

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

py.moveTo(442,307)
py.leftClick()
py.sleep(1)

##Como o programa é muito instável sera necessário tentar para outra velocidade
#--------
#
#
#
#--------

'''
##Selecionar o arquivo para atualização da UPS

py.moveTo(904,295)
py.leftClick()
py.sleep(1)

py.moveTo(457,305)
py.leftClick()
py.sleep(1)


py.moveTo(533,530)
py.leftClick()
caminho = os.path.abspath(r'G:\Operacional\Engenharia de Produto\1. Documentações dos Produtos\22. (500.001.0321) ALTERE V3 R16 (I - CMG)\7. Firmware\2. UPS\UPS-AV3-R16-v6.7.5.16032022[APP].out')
print(caminho)
py.write(caminho)
py.sleep(1)
py.press('enter')

'''
##Atualizar firmware UPS

py.moveTo(1067,298)
py.leftClick()
py.sleep(3)
resp = py.confirm(text='Ocorreu algum erro na conexão?', title='Atualização do Firmware UPS', buttons=['Sim', 'Não'])


##Trata os casos em que houverem erros de conexão
if resp == 'Sim':

   py.moveTo(813,400)
   py.leftClick()
   py.sleep(1)

   py.moveTo(1062,343)
   py.leftClick()
   py.sleep(1)

else:

   py.sleep(240)

#Finalizando o processo de atualização do firmware da UPS


py.moveTo(813,359)
py.leftClick()
py.sleep(5)

py.moveTo(808, 357)
py.leftClick()
py.sleep(5)

py.moveTo(1062, 338)
py.leftClick()
py.sleep(5)

py.moveTo(1121,160)
py.leftClick()
py.sleep(5)

py.moveTo(1045,278)
py.leftClick()
py.sleep(5)

##Abrir arquivo de base para atualização

resp_1 = py.confirm(text='O arquivo de base já foi crregado?', title='Atualização da base', buttons=['Sim', 'Não'])
py.sleep(2)

##Caso o arquivo já tenha sido carregado
if resp_1 == 'Sim':

    py.moveTo(200, 48)
    py.leftClick()
    py.sleep(5)

    py.moveTo(423, 108)
    py.leftClick()
    py.sleep(5)

##Caso o arquivo não tenha sido carregado

#else:

#print(py.position())
'''