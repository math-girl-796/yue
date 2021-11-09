import pygame

NUM_MIXER_CHANNEL = 10

mixer = pygame.mixer
mixer.init()
mixer.set_num_channels(NUM_MIXER_CHANNEL)
mixer.Channel(0).play(mixer.Sound("voice_bank\\zqq\\a.mp3"))
# import time
# time.sleep(5)