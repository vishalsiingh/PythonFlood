# ek function h dusra funnction leta h usko kuch change kr ke reurn kr deta h 

def greet(fx):
    def mfx(*args,**kwargs):    # *args ---arguments leta h as a tuple
                             # **kwargs --- arguments leta h as a dictonary
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using thus function ")
    return mfx

@greet

def hello():
    print("heloo ji")

hello()
# greet (hello)()
@greet
def add(a,b):
    print(a+b)
# add()

greet (add)(1,2)