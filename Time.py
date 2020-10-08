 1| if period == "AM" and hour <= 4:
 2|     print("It's early!")
 3| elif period == "AM":
 4|     print("Good morning!")
 5| elif hour <= 5:
 6|     print("Good afternoon!")
 7| elif hour <= 8:
 8|     print("Good evening!")
 9| else:
10|     print("Good night!")


ORRR

 1| if period == "AM":
 2|     if hour <= 4:
 3|         print("It's early!")
 4|     else:
 5|         print("Good morning!")
 6| else:
 7|     if hour <= 5:
 8|         print("Good afternoon!")
 9|     elif hour <= 8:
10|         print("Good evening!")
11|     else:
12|         print("Good night!")
