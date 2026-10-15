from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "コンビニのサンドイッチ(ミックス)"
    
    def get_summary(self):
        return "安い、おいしい、栄養ある"
    
    def get_author(self):
