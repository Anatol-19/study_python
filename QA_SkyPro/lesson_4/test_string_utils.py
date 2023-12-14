from string_utils import StringUtils
util = StringUtils()

xs = "skypro"
x_cap = "Skypro"
x_trim = "skypro"
x3 = ("1:2:3")
x_list = ["1", "2", "3"]
xS = "SkyPro"
x_t  = True
x_delete = "Sky"
x_f = False
x9 = [1,2,3,4]
x_str = "1, 2, 3, 4"

def test_capitilize():
    rest = util.capitilize(xs)
    assert rest == x_cap

def test_trim():
    rest = util.trim(xs)
    assert rest == x_trim

def test_list():
    rest = util.to_list(x3, ":")
    assert rest == x_list   

def test_contains():
    rest = util.contains(xS, "S")
    assert rest == x_t  

def test_delete():
    rest = util.delete_symbol(xS, "Pro")
    assert rest == x_delete
   
def test_start():
    rest = util.starts_with(xS, "P")
    assert rest == x_f

def test_end():
    rest = util.end_with(xS, "o")
    assert rest == x_t

def test_empty():
    rest = util.is_empty(xS)
    assert rest == x_f

def test_string():
    rest = util.list_to_string(x9)
    assert rest == x_str
  