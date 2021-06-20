# keyboardMonitor
For selecting keyboard switch for my hotswappable

There are 3 files here
1:keyboardmonitor.py
  always run this, and it will track your typing, watching everything you do, listening everything you say
  as this format "(key):|:(timepress)"
2:monitoringcompiler.py
  it will print or return data as df
  with key as index and "presstime","presslong","before backspace" as column
  "presstime"= how many times you press those key
  "presslong"= average time you press for this key
  "before backspace"= howmany time you press those key before you press backspace
3:graphcompiler.py
  import df from 2 and return or show image ofkeyboard with color and number as permillion
  
Summary:
  run keyboardmonitor.py all the time ( or put it in your computer's "Startup" folder)
  run graphcompiler.py to see your result
