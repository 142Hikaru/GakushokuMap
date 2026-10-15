from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "ガパオライス"
    
    def get_summary(self):
        return "スパイシーで美味しい！オープンキャンパスで食べて感動した。"
    
    def get_author(self):
        return "村山丈一郎"