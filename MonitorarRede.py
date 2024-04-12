import pcapy
from impacket.ImpactDecoder import EthDecoder

# Função para decodificar e imprimir pacotes
def packet_handler(header, data):
    decoder = EthDecoder()
    eth_pkt = decoder.decode(data)
    print(eth_pkt)

def main(interface, num_packets):
    # Abre o dispositivo de captura
    cap = pcapy.open_live(interface, 65536, True, 100)

    # Define um filtro para capturar todos os tipos de pacotes
    cap.setfilter('')

    # Define o número de pacotes a serem capturados (-1 para capturar indefinidamente)
    cap.loop(num_packets, packet_handler)

if __name__ == "__main__":
    try:
        # Interface de rede a ser monitorada
        interface = input("Insira o nome da interface de rede (por exemplo, 'eth0'): ")

        # Número de pacotes a serem capturados (-1 para capturar indefinidamente)
        num_packets = int(input("Insira o número de pacotes a serem capturados (ou -1 para capturar indefinidamente): "))

        # Inicia a captura de pacotes
        main(interface, num_packets)
    except KeyboardInterrupt:
        print("\nCaptura de pacotes encerrada.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
