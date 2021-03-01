import speedtest

def initialize(voice_command,sentences):

    response = ("Mise en route d'un speedtest..")
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    d = (float(res["download"]) / 1024)/1000
    u = (float(res["upload"]) / 1024)/1000
    p = float(res["ping"])
    d = round(d,3)
    u = round(u,3)
    p = round(p,3)
    d = str(d)
    u = str(u)
    p = str(p)
    d = d.replace(".",",")
    u = u.replace(".",",")
    p = p.replace(".",",")
    response = (f"Vous êtes actuellement à {d} Mb/s download et {u} Mb/s upload, avec un ping de {p} millisecondes")
    return True, response
