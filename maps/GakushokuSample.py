from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "オススメの学食メニューをここに書きます"
    
    def get_summary(self):
        return "オススメのポイントやなぜオススメできるかなど、簡単に書きます"
    
    def get_author(self):
        return "書いた人の名前を書きます"