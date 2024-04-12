from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Bill_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")

        #product categories lists
        self.Category=["Select Option","Clothing","Mobile"]
        
        #product categories lists clothing

        self.SubcatClothing=["Pant","T-shirt","Shirt"]
        self.pant=["Levis","Mufti"]
        self.price_Levis=2000
        self.price_Mufti=4000

        self.T_shirt=["Levis","Mufti"]
        self.price_Levis=2500
        self.price_Mufti=4400

        self.Shirt=["Levis","Mufti"]
        self.price_Levis=1000
        self.price_Mufti=2000

        #product categories lists mobile


        self.SubcatMobile=["Iphone","Samsung","Realme","OnePlus",]
        self.SubcatMobile=["Iphone14","Iphone13","Iphone11"]
        self.pant=["Iphone14pro","Iphone14"]
        self.price_Iphone14pro=200000
        self.price_Iphone14=70000

        self.pant=["Iphone13pro","Iphone13"]
        self.price_Iphone13pro=180000
        self.price_Iphone13=65000

        

        self.SubcatMobile=["Samsung S Series","Samsung M Series"]
        self.pant=["Samsung S22","Samsung S24"]
        self.price_SamsungS22=140000
        self.price_SamsungS24=170000

        self.pant=["Samsung M 22","Samsung M 23"]
        self.price_SamsungM22=1800
        self.price_SamsungM23=25000


        self.SubcatMobile=["Realme3","Realme5"]
        self.pant=["Realme 3 pro","Realme3"]
        self.price_Realme3Pro=15000
        self.price_Realme3=9000

        self.pant=["Realme 5 pro","Realme5"]
        self.price_Realme5pro=15000
        self.price_Realme5=9000


        self.SubcatMobile=["OnePlus 9","OnePlus 10"]
        self.pant=["OnePlus 9 pro","OnePlus 9"]
        self.price_OnePlus9Pro=49000
        self.price_OnePlus9=39000

        self.pant=["OnePlus 10 pr0","OnePlus 10"]
        self.price_OnePlus10pro=55000
        self.price_OnePlus10=45000
        



        lbl_title=Label(self.root,text="Billing System",font=("times new roman",35,'bold'),fg="black")
        lbl_title.place(x=0,y=10,width=1500,height=60)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=100,width=1400,height=620)

        #customer frame
        customer_frame=LabelFrame(Main_Frame,text="Customer Details",font=("times new roman",14,'bold'),fg="black")
        customer_frame.place(x=15,y=15,width=400,height=150)




        self.lbl_name=Label(customer_frame,text="Customer Name.",font=("times new roman",14,'bold'),fg="black")
        self.lbl_name.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_name=ttk.Entry(customer_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_name.grid(row=0,column=2)

        self.lbl_mob=Label(customer_frame,text="Mobile No.",font=("times new roman",14,'bold'),fg="black")
        self.lbl_mob.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(customer_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_mob.grid(row=1,column=2)

        self.lbl_email=Label(customer_frame,text="Email",font=("times new roman",14,'bold'),fg="black")
        self.lbl_email.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.entry_email=ttk.Entry(customer_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_email.grid(row=3,column=2)


 #product label frame
        product_frame=LabelFrame(Main_Frame,text="Product Details",font=("times new roman",14,'bold'),fg="black")
        product_frame.place(x=15,y=180,width=400,height=250)


#product details

        self.lbl_Category=Label(product_frame,text="Item",font=("times new roman",14,'bold'),fg="black")
        self.lbl_Category.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        # self.Combo_Category=ttk.Combobox(product_frame,font=('arial',12,'bold'),background='white',text=selct catrgory)
    

        self.entry_Category=ttk.Combobox(product_frame,value=self.Category,font=("times new roman",13,'bold'),width=24)
        self.entry_Category.current(0)
        self.entry_Category.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.entry_Category.bind("<<lbl_entrySelcted>>",self.Categories)

        self.lbl_Category=Label(product_frame,text="Item Code",font=("times new roman",14,'bold'),fg="black")
        self.lbl_Category.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_Category=ttk.Combobox(product_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_Category.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        self.lbl_Category=Label(product_frame,text="Quantity",font=("times new roman",14,'bold'),fg="black")
        self.lbl_Category.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.entry_Category=ttk.Combobox(product_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_Category.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        self.lbl_Category=Label(product_frame,text="Price",font=("times new roman",14,'bold'),fg="black")
        self.lbl_Category.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        self.entry_Category=ttk.Combobox(product_frame,font=("times new roman",13,'bold'),width=24)
        self.entry_Category.grid(row=4,column=1,sticky=W,padx=5,pady=2)

        # self.lbl_Category=Label(product_frame,text="Tax",font=("times new roman",14,'bold'),fg="black")
        # self.lbl_Category.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        # self.entry_Category=ttk.Combobox(product_frame,font=("times new roman",13,'bold'),width=24)
        # self.entry_Category.grid(row=4,column=1,sticky=W,padx=5,pady=2)

        #search box
        
        Search_frame=LabelFrame(Main_Frame,text="Search bill ",font=("times new roman",14,'bold'),fg="black")
        Search_frame.place(x=870,y=15,width=480,height=60)

        self.lbl_BILL=Label(Search_frame,text="Bill Number",font=("times new roman",14,'bold'),fg="white",bg="red")
        self.lbl_BILL.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_frame,font=("times new roman",13,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2,pady=2)

        self.btnAddTocart=Button(Search_frame,text="Search",font=("times new roman",11,'bold'),bg="red",fg="white",width=7,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=0)
        self.btnAddTocart.place(x=340,y=0)
    

        #right frame bill area
        RightLableFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",14,'bold'),bg="white",fg="black")
        RightLableFrame.place(x=870,y=80,width=480,height=440)

        scroll_y=Scrollbar(RightLableFrame,orient=VERTICAL)
        self.textarea=Text(RightLableFrame,yscrollcommand=scroll_y.set,font=("times new roman",14,'bold'),bg="white",fg="black")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill counter
        RightLableFrame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",14,'bold'),bg="white",fg="black")
        RightLableFrame.place(x=425,y=15,width=420,height=200)
        
        
        self.subtotal=Label(RightLableFrame,text="Sub Total",font=("times new roman",14,'bold'),fg="black")
        self.subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Entrysubtotal=ttk.Entry(RightLableFrame,font=("times new roman",13,'bold'),width=24)
        self.Entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(RightLableFrame,text="Taxes",font=("times new roman",14,'bold'),fg="black")
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(RightLableFrame,font=("times new roman",13,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lbl_tax1=Label(RightLableFrame,text="Total without Taxes",font=("times new roman",14,'bold'),fg="black")
        self.lbl_tax1.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax1=ttk.Entry(RightLableFrame,font=("times new roman",13,'bold'),width=24)
        self.txt_tax1.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax2=Label(RightLableFrame,text="Total with Taxes",font=("times new roman",14,'bold'),fg="black")
        self.lbl_tax2.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax2=ttk.Entry(RightLableFrame,font=("times new roman",13,'bold'),width=24)
        self.txt_tax2.grid(row=3,column=1,sticky=W,padx=5,pady=2)

        #img frame
        Img_Frame=Frame(Main_Frame,bd=10)
        Img_Frame.place(x=425,y=230,width=430,height=280)
        img=Image.open("imges/img.jpg.webp")
        # img=img.resize(430,130)
        # self.photoImg=ImageTk.PhotoImage(Img_Frame)
        # Img_Frame.place(x=425,y=230,width=430,height=280)


        #bottom frame
        Bill_frame=LabelFrame(Main_Frame,text="",font=("times new roman",14,'bold'),fg="black")
        Bill_frame.place(x=15,y=535,width=1320,height=50)



        Btn_frame=Frame(Bill_frame,bd=2,bg="black")
        Btn_frame.place(x=0,y=145)

        self.btnAddTocart=Button(Bill_frame,text="Add to Card",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=0)
        self.btnAddTocart.place(x=300,y=0)
        
        self.btnAddTocart=Button(Bill_frame,text="Bill Genrate",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=1)
        self.btnAddTocart.place(x=425,y=0)

        
        
        self.btnAddTocart=Button(Bill_frame,text="Save Bill",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=2)
        self.btnAddTocart.place(x=550,y=0)

        self.btnAddTocart=Button(Bill_frame,text="Print",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=3)
        self.btnAddTocart.place(x=670,y=0)


        self.btnAddTocart=Button(Bill_frame,text="Clear",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=4)
        self.btnAddTocart.place(x=790,y=0)


        self.btnAddTocart=Button(Bill_frame,text="Exit",font=("times new roman",15,'bold'),bg="red",fg="white",width=10,cursor="hand2")
        self.btnAddTocart.grid(row=0,column=50)
        self.btnAddTocart.place(x=900,y=0)

        #subcategories validation

    def Categories(self,event=""):
        if self.entry_Category.get()=="Clothing":
            self.lbl_Category.current(0)
            self.lbl_Category.config(value=self.SubcatClothing)











if __name__ == '__main__':
    root=Tk()
    obj=Bill_System(root)
    root.mainloop()
     