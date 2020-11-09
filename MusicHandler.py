import pygame

class MusicHandler:
    def __init__(self):
        pass
    def load_play(self,file,q):
        pygame.mixer_music.load(file)
        pygame.mixer_music.play()
    def volume_change(self,v):
        """
        Change volume (up or down) by the specefied value.
        :param v: float 1.0 >= v < 0.0
        :return: None
        """
        nv = pygame.mixer_music.get_volume()
        pygame.mixer_music.set_volume(nv + v)

