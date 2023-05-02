import speedtest
from PIL import Image
import requests
from io import BytesIO

servers = []
threads = None
print("Checking....")
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
download_speed=float(results_dict["download"])
upload_speed=float(results_dict["upload"])
ping=float(results_dict["ping"])
# isp=results_dict["isp"]
picture=results_dict["share"]
picture_response=requests.get(picture)
with open("image.jpg", "wb") as f:
    f.write(picture_response.content)

print(f"Download Speed : {int(download_speed/1000000)} Mbps")
print(f"Upload Speed : {int(upload_speed/1000000)} Mbps")
print(f"Ping :{ping}")