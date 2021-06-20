# keyboardMonitor
For selecting keyboard switch for my hotswappable
(code is very easy to read)<br/>

## There are 3 files here<br />

#### 1) keyboardmonitor.py
  always run this, and it will track your typing, watching everything you do, listening everything you say<br />
  as this format "(key):|:(timepress)"<br />
  
#### 2) monitoringcompiler.py
  it will print or return data as df (dataframe)<br />
  with key as index and "presstime","presslong","before backspace" as column<br />
  "presstime"= how many times you press those key<br />
  "presslong"= average time you press for this key<br />
  "before backspace"= howmany time you press those key before you press backspace<br />
  
#### 3) graphcompiler.py
  import df from 2 and return or show image of keyboard with color and number as permillion<br />
  (plot "presstime" and "presslong/presstime"; you can edit it as you want)
  
## Summary:

  run keyboardmonitor.py all the time ( or put it in your computer's "Startup" folder)<br />
  run graphcompiler.py to see your result
