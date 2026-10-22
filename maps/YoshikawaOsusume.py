from maps.AbstractGakushoku import AbstractGakushoku

class YoshikawaOsusume(AbstractGakushoku):

    def get_menu(self):
        return "Go Hachi 醤油ラーメン"
    
    def get_summary(self):
        return "ネギとスープの相性が良い"
    
    def get_author(self):
        return "吉川輝"