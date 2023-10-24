import ctypes

# gcc -fPIC -shared -o calibrary.so calibrary.c       run this command to generate the .so file

clibrary: ctypes.CDLL = ctypes.CDLL(
    "F:/Waheed/WOrk/studyproject/C-Revision/exercises/ctype_tutorials/calibrary.so"
)


# clibrary.display(b"Waheed", 29)

# Redefining our function  as if it is {def display(str , int):}
display = clibrary.display

display.argtypes: list = [ctypes.c_char_p, ctypes.c_int]
display.restype = ctypes.c_char_p

string: str = display(b"Waheed", 29).decode("ascii")

print(str(string))
