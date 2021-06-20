
import pandas as pd
import monitoringcompiler as mc
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def main():
	d={}
	for x,y,z in zip(r"""~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?""",r"""`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./""",list(range(1,48))):d[x],d[y]=z,z
	wx,hx=24,32
	dw={"tab":4,"caps lock":5,"shift":7,"":1,"enter":6,"right shift":8,"space":22,"backspace":5,"ctrl":3,"left windows":3,"alt":3,"right alt":3,"right ctrl":3,26:3}
	for i in range(1,5):dw[' '*i]=i	
	r1=list(range(1,14))+["backspace","","insert","home","page up"]
	r2=["tab"]+list(range(14,27))+["","delete","end","page down"]
	r3=["caps lock"]+list(range(27,38))+["enter"]
	r4=["shift"]+list(range(38,48))+["right shift","","  ","up","  "]
	r5=["ctrl","left windows","alt","space","right alt","   ","   ","right ctrl","","left","down","right"]
	ra=[r1,r2,r3,r4,r5];dc=r1+r2+r3+r4+r5
	df=mc.main()
	ndf=pd.DataFrame(columns=df.columns,index=set(dc)).fillna(0)
	for i in df.index:
		if i in d:ndf.loc[d[i]]+=df.loc[i]
		elif i in dc:ndf.loc[i]=df.loc[i]
	ndf['before backspace']['backspace']=0
	ndf['l/t']=(ndf['presslong']/ndf['presstime']).replace([np.inf, -np.inf, np.nan],0)

	def fic(m,s):
		m=255*m.replace([np.inf, -np.inf, np.nan],0)
		s=1e6*s.replace([np.inf, -np.inf, np.nan],0)
		img  = Image.new( mode = "RGB", size = (72*wx, 10*hx) )
		draw = ImageDraw.Draw(img,'RGB')
		x,y=0,0
		for i in ra:
			for j in i:
				if j=='':w=1
				elif j in dw:w=dw[j]+2
				else:w=4
				if not j==' '*len(str(j)):
					color=int(m[j])
					textcolor=max([0,255],key=lambda x:abs(x-color))
					draw.rectangle([(x,y),(x+w*wx,y+2*hx)],outline='black',fill=(color,)*3)
					draw.text((x+wx,y+hx),str(int(s[j])),fill=(textcolor,)*3)
				x+=w*wx
			x,y=0,y+2*hx
		return img
			
	def seriepersum(sr):return sr/sr.sum()
	def seriepernlargest(sr,n):return sr/sr.nlargest(n).min()
	a=fic(seriepernlargest(ndf['presstime'],10),seriepersum(ndf['presstime']))
	b=fic(seriepernlargest(ndf['l/t'],10),seriepersum(ndf['l/t']))
	return a,b
if __name__=="__main__":
	for i in main():i.show()
