import hashlib as rinku
from pyscript import document


def md5_converter(event):      
    pwd = document.getElementById('md5_input').value
    priya = rinku.md5(pwd.encode('utf-8'))
    raja = priya.hexdigest()
    print(raja)
    output_div = document.getElementById('md5_output')
    output_div.innerText = raja
    
def sha1_converter(event):      
    pwd = document.getElementById('sha1_input').value
    priya = rinku.sha256(pwd.encode('utf-8'))
    raja = priya.hexdigest()
    print(raja)
    output_div = document.getElementById('sha1_output')
    output_div.innerText = raja
    
def sha384_converter(event):      
    pwd = document.getElementById('sha384_input').value
    priya = rinku.sha384(pwd.encode('utf-8'))
    raja = priya.hexdigest()
    print(raja)
    output_div = document.getElementById('sha384_output')
    output_div.innerText = raja
   