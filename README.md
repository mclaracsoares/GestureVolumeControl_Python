# GestureVolumeControl_Python

### 🚀 Desenvolvido por:
- **Lucas Eduardo Gurgel**
- **Maria Clara Soares**
- **Pedro Filipe Macedo**

## 📌 Descrição do Projeto
Este projeto implementa uma interface intuitiva de controle de volume utilizando gestos captados em tempo real por uma webcam. Com o uso de visão computacional (MediaPipe) e automação de áudio (PyCaw), o sistema ajusta o volume do computador com base no número de dedos levantados.

## 🚀 Funcionalidades
- **Detecção de dedos**: Reconhece a quantidade de dedos levantados em uma mão.
- **Ajuste de volume**: Controla o volume do sistema proporcionalmente ao número de dedos levantados (0 a 5).
- **Interface em tempo real**: Exibe a imagem capturada com os pontos da mão desenhados na tela.

## 🛠️ Ferramentas e Tecnologias Utilizadas
- **Python**: Linguagem de programação.
- **MediaPipe**: Para detecção de mãos e pontos de referência.
- **PyCaw**: Para manipulação do áudio do sistema.
- **OpenCV**: Para captura e processamento de vídeo.
- **Comtypes**: Para integração com a API de áudio do Windows.

## 📷 Como Funciona
1. A webcam captura a imagem em tempo real.
2. O MediaPipe identifica a mão e seus pontos de referência.
3. O número de dedos levantados é calculado.
4. O volume do sistema é ajustado proporcionalmente ao número de dedos levantados.

## 🖥️ Como Executar o Projeto
**Pré-requisitos**:
- Python 3.x instalado.
- Instale as dependências do projeto: pip install opencv-python mediapipe pycaw comtypes.

**Clone o Repositorio**
- git clone https://github.com/seu-usuario/GestureVolumeControl.git
- Execute o script principal.

## 📄 Licença
- Este projeto é de código aberto e pode ser utilizado para fins educacionais e experimentais. Contribuições são bem-vindas!

## 🎉 Obrigado por conferir nosso projeto!
