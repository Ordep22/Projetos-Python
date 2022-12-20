
class decodifica_serial:

    def __init__(self):
        self.dadoEnviado = None
        self.dadoLido = None
        self.leitura = None

    def decodifica(self, dadoLido, dadoEnviado):

        ###Basicamente será pegar o pacote completo e processar as informções
        # LUPATTFRqtbytesqtpctCC
        # 4c 55 50 41 32 32 30 3a3032303030303034303830304632 be 78
        # 76 85 80 65 50 50 48 58 48 50 48 48 48 48 48

        # LUPA2200:020000040800F2

        ##Dados vindoas da serial
        self.dadoLido = str(dadoLido).strip("'b").strip('\n\r')
        tamanhoDadolido = len(self.dadoLido)

        ##Dados enviados
        self.dadoEnviado = dadoEnviado.strip('\n')
        tamanhoDadoenviado = len(self.dadoEnviado)

        estado = 0

        # Verificando resposta
        if estado == 0:
            print(self.dadoLido[12:14])
            if self.dadoLido[12:14] == '48':
                estado = 1
            elif self.dadoLido[13:14] == '49':
                estado = 'fim'
            else:
                estado = 'fim'

        # Verificando até o comando
        if estado == 1:

            if self.dadoLido[0:14] == self.dadoEnviado[0:14]:
                estado = 2
            else:
                estado = 'fim'

        # Comparando o CRC
        if estado == 2:
            if self.dadoLido[tamanhoDadolido - 4:tamanhoDadolido] == self.dadoEnviado[tamanhoDadoenviado - 4:
            tamanhoDadoenviado]:
                return True

        if estado == 'fim':
            return False
