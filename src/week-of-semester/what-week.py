from datetime import date

today = date.today()

delta = today - date(2021, 2, 1) # start of semester
weeks = delta.days // 7

print(f"{weeks}. hét: {today}")
