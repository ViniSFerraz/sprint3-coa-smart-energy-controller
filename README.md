# Smart Energy Controller

Protótipo educacional de um sistema de controle de sessão de recarga, desenvolvido para a **Sprint 3 de Arquitetura de Computadores**.

O projeto utiliza um **Raspberry Pi Pico** programado em **MicroPython** para simular o gerenciamento de uma sessão de recarga a partir da relação entre geração e consumo de energia.

## Links

**Vídeo da apresentação:**  
https://youtu.be/tdpkI9IZyA4

**Wokwi:**  
https://wokwi.com/projects/474810270904458241

## Objetivo

Desenvolver um protótipo capaz de calcular a energia disponível para uma sessão de recarga a partir dos valores de geração e consumo, determinando automaticamente o estado da recarga.

O sistema utiliza três LEDs para representar os estados:

- **LED verde:** Recarga autorizada
- **LED amarelo:** Recarga reduzida
- **LED vermelho:** Recarga bloqueada

O projeto é um protótipo educacional inspirado no conceito de gerenciamento inteligente de energia.

## Tecnologias utilizadas

- Raspberry Pi Pico
- MicroPython
- LEDs
- Monitor Serial

## Funcionamento

O programa recebe os valores de **geração** e **consumo** através da função `verificar_recarga()`.

A energia disponível é calculada pela seguinte operação:

```text
Energia disponível = Geração - Consumo
```

Depois do cálculo, o programa verifica o resultado e determina o estado da recarga:

```text
Se disponível >= 1000 W:
    RECARGA AUTORIZADA

Se disponível > 0 W e < 1000 W:
    RECARGA REDUZIDA

Se disponível <= 0 W:
    RECARGA BLOQUEADA
```

## Controle dos LEDs

Os LEDs estão conectados aos seguintes pinos do Raspberry Pi Pico:

| LED | GPIO | Estado |
|---|---:|---|
| Vermelho | GP1 | Recarga bloqueada |
| Amarelo | GP5 | Recarga reduzida |
| Verde | GP9 | Recarga autorizada |

Antes de indicar um novo estado, o programa desliga os três LEDs. Em seguida, acende somente o LED correspondente ao estado identificado.

## Exemplos das situações

### Recarga autorizada

```text
Geração: 4000 W
Consumo: 1500 W
Disponível: 2500 W
Status: RECARGA AUTORIZADA
```

Nesse caso, a energia disponível é igual a **2500 W**, valor superior ou igual ao limite de 1000 W. O LED verde é acionado.

### Recarga reduzida

```text
Geração: 1800 W
Consumo: 1500 W
Disponível: 300 W
Status: RECARGA REDUZIDA
```

Nesse caso, existe energia disponível, mas o valor é inferior a 1000 W. O LED amarelo é acionado.

### Recarga bloqueada

```text
Geração: 1000 W
Consumo: 1800 W
Disponível: -800 W
Status: RECARGA BLOQUEADA
```

Nesse caso, o consumo é maior que a geração, resultando em energia disponível negativa. O LED vermelho é acionado.

## Saída no Monitor Serial

Durante a execução, o programa apresenta no monitor serial:

```text
GERACAO: 1000 W
CONSUMO: 1800 W
DISPONIVEL: -800 W
STATUS: RECARGA BLOQUEADA
------------------------
```

Essas informações permitem acompanhar os dados utilizados pelo programa e o resultado do processamento.

## Relação com Arquitetura de Computadores

O projeto demonstra a relação entre **entrada, processamento, memória e saída**.

### Entrada

Os valores de geração e consumo são fornecidos ao programa:

```python
verificar_recarga(geracao, consumo)
```

### Processamento

O Raspberry Pi Pico executa o programa e calcula:

```text
geração - consumo = energia disponível
```

Depois, o resultado é comparado com os limites definidos no algoritmo para determinar o estado da recarga.

### Memória

Durante a execução, os valores utilizados pelo programa, como geração, consumo, energia disponível e estado da recarga, são mantidos na memória para serem processados e utilizados pelas demais instruções.

### Saída

O resultado do processamento é apresentado através de:

- **LEDs**, indicando visualmente o estado da recarga;
- **Monitor Serial**, apresentando os valores de geração, consumo, energia disponível e status.

Dessa forma, o protótipo demonstra a interação entre **hardware, software e dados**.

## Integrantes

- Ângelo Malta Reina — RM 570769
- Gustavo Mendonça Duarte — RM 570561
- Matheus Carpinheiro Moreno — RM 571770
- Renan de Castro Albuquerque — RM 570532
- Vinícius Souza Ferraz — RM 570622
