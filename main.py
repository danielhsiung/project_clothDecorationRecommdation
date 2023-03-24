from cloth import Cloth
from os import listdir
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, messagebox, Tk


#存放照片的位置
path=r'rpg'
#從照片位致中，存取資料夾的名子，並做成list
list_hay=listdir(path)
picDict = {}
#將所有的圖片變成一個物件
for name_list in range(len(list_hay)):
    picDict[name_list]=Cloth(list_hay[name_list])
    picDict[name_list].add_place()
    picDict[name_list].add_style()

#此時，物件會需要用list的方式來呼叫，而非直接呼叫該物件的本名，以下為示範：
#for a in range(len(list_hay)):
#    picDict[a].place_show()
#    print('________________')
#    picDict[a].style_show()
#不能使用 艷麗風.place_show()

list_1checkedImg = {}
checkedPlace = {}
checkedStyle = {}
count = 0
#儲存符合勾選標籤的圖片

##########################################
#############TKinter模板區################
#########################################

#建立tkinter視窗，為了能夠按下一頁，我們幫每一頁建立一個模板，並在按下下一頁的時候把原本得模板清除
#初始設定可以寫在這
class SampleApp(tk.Tk): #主要切換模板的class，並繼承tkinter的tk.Tk方法
    def __init__(self):
        tk.Tk.__init__(self)  #宣告一個網頁
        self._frame = None  #宣告一個變數存放原本是使用哪一個模板，預設為None
        self.switch_frame(StartPage) #一個class內建的switch_frame方法，來切換模板

    def switch_frame(self, frame_class): #寫一個class內建的switch_frame方法， 參數是下一個要執行的模板
        new_frame = frame_class(self) #frame_class(self)會
        if self._frame is not None: #如果偵測到上一個模板不是None就會把上一個模板摧毀
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack() #執行現在的這個模板

#下面開始寫個個頁面的功能
#這是開始頁
class StartPage(tk.Frame): #繼承tk.Frame
    def resizeImage(self, image):
        w, h = image.size  # 獲取image的長和寬
        mlength = max(w, h)  # 取最大的一邊作爲縮放的基準
        mul = 400 / mlength  # 縮放倍數
        w1 = int(w * mul)
        h1 = int(h * mul)
        return image.resize((w1, h1))

    def showImage(self, path):
        global img
        image = Image.open(path)  # 打開圖片放到image中
        re_image = self.resizeImage(image)
        img = ImageTk.PhotoImage(re_image)  # 在canvas中展示圖片
        self.canvas.create_image(200, 200, anchor='center', image=img)  # 以中小點爲錨點

    def destroy_canvas(self):
        self.canvas.destroy()

    def __init__(self, master): #想像等於 master=tk.Tk()
        self.canvas = tk.Canvas(master, height=400, width=400)  # 畫布長款定爲400x400
        self.canvas.pack()
        tk.Frame.__init__(self, master)
        self.showImage('wear.png')

        tk.Button(self, text="下一頁", font=('Microsoft JhengHei', 19, "bold"),
                  command=lambda: [master.switch_frame(PageOne),self.destroy_canvas()]).pack()
        # button按鈕的command lambda表示想要傳回一些引數，第一個就是回去執行上面switch_frame的指令，切換頁面，後面可以放多個指令
        # 第二個指令就可以放一些條件判斷，這裡以something函數為例，它會印回Hi!的值，記得格式為lamba:[(指令一),(指令二)... ...]





#第一頁
class PageOne(tk.Frame):
    country = {0: '大學校園', 1: '健身房', 2: '海邊', 3: '山林', 4: '正式場合', 5: '都會區', 6: '夜店'}
    check_v = {}
    def getCheckedPlace(self):  #將勾選的值儲存到checkedPlace字典中
        global checkedPlace
        for i in self.check_v:
            if self.check_v[i].get() == True:
                checkedPlace[i] = self.country[i]
        print(checkedPlace)

    def findCheckedImg(self):  #在所有圖片中找圖片標籤有包含checkedPlace的圖片 並加入list_1checkedImg
        global list_1checkedImg
        list_1checkedImg.clear()
        order = 0
        if len(checkedPlace)==0 : #checkedPlace是空的(使用者沒勾選) 
            list_1checkedImg = picDict
        else :                                         #勾選一個以上
            for i in range(len(picDict)) :
                if set(checkedPlace.values()) <= set(picDict[i].place) : #set1 是否為 set2子集合
                    list_1checkedImg[order] = picDict[i]
                    order+=1
        for i in range(len(list_1checkedImg)) : #印出來檢查看有沒有錯而已
            print(list_1checkedImg[i].place)
            print(list_1checkedImg[i].style)
        print('-----')

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        master.title('場合')
        tk.Label(self, text='請勾選你的場合', font=('Microsoft JhengHei', 20, "bold"),pady=1).pack()
        
        for i in range(len(self.country)):
            self.check_v[i] = tk.BooleanVar()
            tk.Checkbutton(self, text=self.country[i], variable=self.check_v[i], font=('Microsoft JhengHei', 14)).pack(side='top')
        tk.Label(self, text='若沒有要選就跳過', font=('Microsoft JhengHei', 14, "bold"), padx=5, pady=10).pack()
        tk.Button(self, text="下一頁",font=('Micorosoft JhenHei',14,"bold"),
                  command=lambda: [master.switch_frame(PageTwo),self.getCheckedPlace(), self.findCheckedImg()]).pack(side="top")


#第二頁
class PageTwo(tk.Frame):
    country = {0: '可愛', 1: '性感', 2: '文青', 3: '街頭', 4: '簡約', 5: '帥氣', 6: '運動', 7: '優雅', 8: '浮誇', 9: '休閒'}
    check_v = {}
    def getCheckedStyle(self):
        global checkedStyle
        for i in self.check_v:
            if self.check_v[i].get() == True:
                checkedStyle[i] = self.country[i]
        print(checkedStyle)

    def findCheckedImg(self):
        global list_1checkedImg
        list_2checkedImg ={}
        order = 0
        if len(checkedStyle)==0 :
            list_2checkedImg = list_1checkedImg
        else :
            for i in range(len(list_1checkedImg)):
                if set(checkedStyle.values()) <= set(list_1checkedImg[i].style) : #set1 是否為 set2子集合
                    list_2checkedImg[order] = list_1checkedImg[i]
                    order+=1
        list_1checkedImg= list_2checkedImg
        for i in range(len(list_1checkedImg)) :
            print(list_1checkedImg[i].place)
            print(list_1checkedImg[i].style)
        print('-----')
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        master.title('風格')
        tk.Label(self, text='請勾選你的風格',font=('Microsoft JhengHei', 26, "bold")).pack()
        for i in range(len(self.country)):
            self.check_v[i] = tk.BooleanVar()
            tk.Checkbutton(self, text=self.country[i], variable=self.check_v[i],font=('Microsoft JhengHei', 14),padx=60,justify='right').pack(side='top',anchor='w')
        tk.Button(self, text="下一頁分析結果",font=('Micorosoft JhenHei',14,"bold"),
                    command=lambda: [self.getCheckedStyle(),self.findCheckedImg(),master.switch_frame(PageThree)]).pack(side='top')

#第三頁
class PageThree(tk.Frame):
    def clearChecked(self):  #將字典清空
        global list_1checkedImg
        global checkedPlace
        global checkedStyle

        if len(checkedStyle)>0 :
            checkedStyle.clear()
        else :
            checkedStyle={}
        if len(checkedPlace)>0 :
            checkedPlace.clear()
        else :
            checkedPlace={}
        if len(list_1checkedImg)>0 :
            list_1checkedImg.clear()
        else :
            list_1checkedImg = {}

    def __init__(self,master):
        tk.Frame.__init__(self,master)
        master.title('穿搭推薦結果')
        master.geometry('700x700')
        
        self.canvas=tk.Canvas(master,height=400,width=400)   #畫布長款定爲400x400
        self.canvas.pack()

        if len(list_1checkedImg)>0 :     #結果有交集的話
            
            self.showImage(list_1checkedImg[count].imagesPath)

            label1 = tk.Label(self, text=list_1checkedImg[count].place,font=('Microsoft JhengHei', 18, "bold"),pady=5)
            label1.pack()   #顯示圖片標籤(地點
            label2 = tk.Label(self, text=list_1checkedImg[count].style,font=('Microsoft JhengHei', 18, "bold"),pady=5)
            label2.pack()   #顯示圖片標籤(風格
            
            nextB=tk.Button(self,text='next pic', command=lambda : self.nextPic(label1,label2)).pack(side = 'right')
            prevB=tk.Button(self,text='prev pic', command=lambda : self.prevPic(label1,label2)).pack(side = 'left')
            
        else :      #沒交集的話
            tk.messagebox.showinfo(title = '提醒', message = '抱歉，沒有包含您要找的種類，請重新選擇')
        
        tk.Button(self, text="回第一頁",font=('Micorosoft JhenHei',14,"bold"),
                    command=lambda: [master.switch_frame(StartPage),self.clearChecked(),self.clearPic()]).pack(side = 'top')

    def resizeImage(self,image) :
        w,h=image.size     #獲取image的長和寬
        mlength=max(w,h)    #取最大的一邊作爲縮放的基準
        mul=400/mlength    #縮放倍數
        w1=int(w*mul)
        h1=int(h*mul)
        return image.resize((w1,h1))
        
    def showImage(self,path) :
        global img
        image=Image.open(path)        #打開圖片放到image中
        re_image = self.resizeImage(image)
        img=ImageTk.PhotoImage(re_image)    #在canvas中展示圖片            
        self.canvas.create_image(200,200,anchor='center',image=img)   #以中小點爲錨點
        
    def nextPic(self,placeLabel,styleLabel) :  #切到下一張照片並根據圖片更改圖片標籤
        global count
        try :
            self.showImage(list_1checkedImg[count+1].imagesPath)
            placeLabel['text'] = list_1checkedImg[count+1].place
            styleLabel['text'] = list_1checkedImg[count+1].style
            count+=1
        except KeyError :
            tk.messagebox.showinfo(title = '提醒', # 視窗標題
                                message = '這是最後一張')   # 訊息內容
    def prevPic(self,placeLabel,styleLabel) :  #切到上一張照片並根據圖片更改圖片標籤
        global count
        try :
            self.showImage(list_1checkedImg[count-1].imagesPath)
            placeLabel['text'] = list_1checkedImg[count-1].place
            styleLabel['text'] = list_1checkedImg[count-1].style
            count-=1
        except KeyError :
            tk.messagebox.showinfo(title = '提醒', # 視窗標題
                                message = '這是第一張')   # 訊息內容
    def clearPic(self) : #canvas種類物件切到下一頁竟然不會自動刪除只好自己把他砍了並把count值規0
        global count
        self.canvas.destroy()
        count = 0

#執行程式
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()





