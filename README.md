# Contador de Carros com Python e OpenCV

## Descrição

Este projeto tem como objetivo realizar a contagem automática de veículos em movimento utilizando visão computacional com Python e OpenCV.

O sistema analisa um vídeo contendo carros trafegando em uma via pública e utiliza técnicas de processamento de imagens para identificar quando um veículo passa por uma área de contagem definida no código. A cada passagem detectada, o contador é incrementado automaticamente.

Este projeto foi desenvolvido como adaptação de um exemplo de contagem de pessoas fornecido em sala de aula, substituindo a detecção de pessoas pela detecção de veículos.

## Tecnologias Utilizadas

* Python 3
* OpenCV (cv2)
* NumPy

## Estrutura do Projeto

```text
ContagemDeCarros/
│
├── contadorCarros.py
├── carros-passando.mp4
└── README.md
```

## Instalação

Instale as bibliotecas necessárias através do comando:

```bash
pip install opencv-python numpy
```

ou

```bash
py -m pip install opencv-python numpy
```

## Execução

Para executar o projeto:

```bash
py contadorCarros.py
```

ou

```bash
python contadorCarros.py
```

## Funcionamento

O programa realiza as seguintes etapas:

1. Abre o vídeo contendo os veículos.
2. Converte cada frame para tons de cinza.
3. Aplica técnicas de processamento de imagem para destacar os objetos.
4. Monitora uma região específica da pista.
5. Detecta a passagem dos veículos pela região definida.
6. Incrementa o contador sempre que um novo veículo é identificado.

## Objetivo Acadêmico

O objetivo deste trabalho é demonstrar a aplicação de conceitos de Visão Computacional e Processamento Digital de Imagens utilizando Python e OpenCV para automatizar tarefas de monitoramento e contagem de objetos em vídeos.

## Autor

Maria Fernanda de Jesus
