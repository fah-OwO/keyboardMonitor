import pandas as pd
def savepathtodesktop():
    import os
    return os.path.join('C:/Users',os.getlogin(),'Desktop/keyboardmonitoringlog.txt')
def main(filename=None):
    def lineread(line):
        x,y=line.strip().split(':|:')
        return x.lower(),float(y)
    if filename==None:filename=savepathtodesktop()
    f=open(filename,'r')
    x,y=lineread(f.readline())
    df=pd.DataFrame({'presstime':1,'presslong':y,'before backspace':0},index=[x])
    tmp=x
    for i in f.readlines():
        x,y=lineread(i)
        if x in df.index:df.loc[x]+=1,y,0
        else:df.loc[x]=1,y,0
        if x=='backspace':df.loc[tmp][2]+=1
        tmp=x
    df=df.sort_values(by=['presstime','presslong'],ascending=False)
    return df

if __name__=='__main__':
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):print(main())
