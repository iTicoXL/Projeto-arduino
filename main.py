import serial
import time
from datetime import datetime

#configurando a porta serial
#***checar se a porta de entrada esta correta(COM3)

arduino_port = 'COM3' 
serial_begin = 9600
ser = serial.Serial(arduino_port, serial_begin)

#verificar se a conexao foi feita com sucesso
print("arduino conectado na porta: ", arduino_port)
contador_ativacoes = 0 #variavel criada pra armazenar o valor de quantas vezes banheiro foi usado
#função p/ registrar em um arquivo de log
def log_registro():
    global contador_ativacoes
    contador_ativacoes += 1 #atualiza contador
    with open("registro_uso_banheiro.txt", "a") as file:
        file.write(f"Banheiro usado pela: {contador_ativacoes} vez em: {datetime.now()}\n")
        print("Registro feito!")
        print("Contador de ativacoes: {contador_ativacoes}")

#loop checar os dados enviados pelo arduino
try:
    while True:
        if ser.in_waiting > 0: # Verifica se há dados na porta serial
            linha = ser.readline().decode("utf-8").strip()
            print("Recebido do Arduino:", linha)

            if linha == "Banheiro usado": #se der errado acrescente "em" no final (consulte linha 20)
                log_ativacao()
                
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa interrompido.")

finally:
    ser.close()
    print("Conexão com o Arduino encerrada.")