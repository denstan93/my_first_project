import re
def task29_5(a):
   if re.match("^\d{4}[-/|]\d{2}\-\d{2}\s\d{2}\:\d{2}\:?\d?\d?$", a)is not None:
       return re.match("^\d{4}[-/|]\d{2}\-\d{2}\s\d{2}\:(\d{2})\:?\d?\d?$", a).groups()
   else:
       raise Exception('это не время, а фигня!!!!')
print(task29_5('2018-22-13 12:30:40'))