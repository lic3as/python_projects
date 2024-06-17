from pygame import mixer            # o método mixer da biblioteca pygame pode tocar músicas

mixer.init()                        # iniciar mixer
mixer.music.load('ex021.ogg')       # carregar música
mixer.music.play()                  # play na música carregada
# para parar é só digitar algo:
x = input('Digite algo para parar: ')
