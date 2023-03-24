from PIL import Image,ImageTk

class Cloth:

    def __init__(self, name):
        #抓取目的地資料夾當中該檔案的位置
        #self.images=ImageTk.PhotoImage(Image.open(r"rpg\%s\%s.jpg"%(name,name)))#使用PhotoImage方法打開圖檔
        self.imagesPath = r"rpg\%s\%s.jpg"%(name,name)
        self.place=[]
        self.style=[]
        self.name=name

    #把物件的類別印出來的方法
    def images_show(self):
        a=self.images
        return a.show()
    def place_show(self):
        print(self.place)
    def style_show(self):
        print(self.style)
    def name_show(self):
        print(self.name)

    #幫物件加入place屬性的參數
    def add_place(self):
        #將place.txt抓下
        file = open(r'rpg\%s\place.txt'%self.name, 'r+', encoding='utf-8') #讀取資料
        file_list=file.read().split() #將資料文字分解並變成一個list
        self.place=file_list #幫物件加入place屬性參數

    #幫物件加入style屬性的參數
    def add_style(self):
        # 將place.txt抓下
        file=open(r'rpg\%s\style.txt'%self.name,'r+',encoding='utf-8') #同上
        file_list=file.read().split() #同上
        self.style=file_list #同上















