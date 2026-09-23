from machine import Pin

led_vermelho = Pin(1, Pin.OUT)
led_amarelo = Pin(5, Pin.OUT)
led_verde = Pin(9, Pin.OUT)


def controlar_led(estado):
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)

    if estado == "RECARGA AUTORIZADA":
        led_verde.value(1)

    elif estado == "RECARGA REDUZIDA":
        led_amarelo.value(1)

    elif estado == "RECARGA BLOQUEADA":
        led_vermelho.value(1)


def verificar_recarga(geracao, consumo):

    disponivel = geracao - consumo

    if disponivel >= 1000:
        estado = "RECARGA AUTORIZADA"

    elif disponivel > 0:
        estado = "RECARGA REDUZIDA"

    else:
        estado = "RECARGA BLOQUEADA"

    controlar_led(estado)

    print("GERACAO:", geracao, "W")
    print("CONSUMO:", consumo, "W")
    print("DISPONIVEL:", disponivel, "W")
    print("STATUS:", estado)
    print("------------------------")


verificar_recarga(1000, 1800)