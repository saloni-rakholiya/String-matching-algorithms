from flask import Flask, render_template,request, redirect
import requests
from time import time
from zarray import Zarr
from zarray_application import Zarr_a
import os
from robin import Robin
from ukonnens import SuffixTree

app=Flask(__name__)

#functions
def ukkonen_time(string, pattern):
    begin = time()
    t = SuffixTree(string)
    ind = t.find_substring(pattern)
    print(time()-begin)
    return (f"Pattern not found" if ind == -1 else f"Pattern found at {ind}", f"Time taken is {time()-begin}")

def zarr_time(string, pattern):
    begin = time()
    z = Zarr(string, pattern)
    ind = z.search()
    print(time()-begin)
    return (f"Pattern not found" if ind == -1 else f"Pattern found at {ind}", f"Time taken is {time()-begin}")

# def robin_time(string, pattern):
#     begin = time()
#     r = Robin(string, pattern)
#     ind = r.search()
#     print(time()-begin)
#     return (f"Pattern not found" if ind == -1 else f"Pattern found at {ind}", f"Time taken is {time()-begin}")

def robin_time(string, pattern):
    begin = time()
    r = Robin(string, pattern)
    ind = r.search()
    print(time()-begin)
    return (str(ind), f"Time taken is {time()-begin}")

# def ukkonen_time(string, pattern):
#     begin = time()
#     t = SuffixTree(string)
#     ind = t.find_substring(pattern)
#     end = time() - begin
#     return "{:10f}".format(end)

# def zarr_time(string, pattern):
#     begin = time()
#     z = Zarr(string, pattern)
#     ind = z.search()
#     end = time() - begin
#     return "{:10f}".format(end)
#     # return (f"Pattern not found" if ind == -1 else f"Pattern found at {ind}", f"Time taken is {time()-begin}")

# def robin_time(string, pattern):
#     begin = time()
#     r = Robin(string, pattern)
#     ind = r.search()
#     # return (f"Pattern not found" if ind == -1 else f"Pattern found at {ind}", f"Time taken is {time()-begin}")
#     return "{:10f}".format(time() - begin)
#functions

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="POST":
        strin=request.form.get("strin")
        pattern=request.form.get("strin2")
        return render_template("ans_page.html", ans_ukkonens=ukkonen_time(strin,pattern) , ans_robinkarp=robin_time(strin,pattern), ans_zalgo=zarr_time(strin,pattern)) 
    return render_template("index.html")

@app.route('/application',methods=["GET","POST"])
def application():
    if request.method =="POST":
        if request.files:
            image = request.files["image"]
            pattern=request.form.get("strin2")
            file_name=image.filename
            image.save(file_name)
            finalstr=""
            with open(file_name, "r") as f:
                c = 0
                for i in f:
                    z = Zarr_a(i, pattern)
                    if False:
                        if(z.search() == -1):
                            finalstr+="Pattern found on line "+str(c)+" and Line: "+str(i)+"<br/>"
                            # print(f"{c} {i}", end="")
                    else:
                        if(z.search() != -1):
                            finalstr+="Pattern found on line "+str(c)+" and Line: "+str(i)+"<br/>"
                            # print(f"{c} {i}", end="")
                                
                    c += 1
            print(finalstr)
            return render_template("application_ans.html",finalans=finalstr)        
    return render_template("application_pg.html")

if __name__=="__main__":
    app.run(debug=True)