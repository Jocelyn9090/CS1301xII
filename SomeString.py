1| def has_a_numeral(some_string):
2|     found_a_numeral = False
3|     for letter in some_string:
4|         if letter in "0123456789":
5|             found_a_numeral = True
6|     return found_a_numeral


ORRR



1| def has_a_numeral(some_string):
2|     for letter in some_string:
3|         if letter in "0123456789":
4|             return True
5|     return False
