import requests as r
import json

class wa:
     def __init__(self, json):
         self.phonenum = json['payload']['sender']
         self.pesan = json['payload']
         self.apikey = 'Twu833WIptV}gh{8nTX3S6I|6xm~4FDklNna2a~30EivOqja-rezza'
         print(self.pesan)

     def kirim_requests(self, data):
         url = "https://api.kirimwa.id/v1/messages"
         headers = {
             "Authorization": f"Bearer {self.apikey}",
             "Content-Type": "application/json"
         }
         kirim = r.post(url, data=json.dumps(data), headers=headers)
         return kirim.json()

     def heloworld(self):
         data = {
         "phone_number": self.phonenum,
         "message": "Halo Apa Kabar",
         "device_id": "iphone-x-pro",
         "message_type": "text"
         }
         kirim = self.kirim_requests(data)
         return kirim

     def gambar(self):
         data = {
         "phone_number": self.phonenum,
         "message": "https://neva125671182.files.wordpress.com/2017/12/12.png",
         "device_id": "iphone-x-pro",
         "message_type": "image"
         }
         kirim = self.kirim_requests(data)
         return kirim

     def NoCommand(self):
         data = {
         "phone_number": self.phonenum,
         "message": "Maaf Command Tidak Ditemukan, Command Yang Tersidia Untuk Saat Ini Adalah \n text untuk Merespon Pesan \n gambar untuk merespon pesan dengan gambar \n\n Note : Bot Masih Dalam Tahap Percobaan, Tunggu Next Update nya yaa :)",
         "device_id": "iphone-x-pro",
         "message_type": "text"
         }
         kirim = self.kirim_requests(data)
         return kirim

     def processing(self):
         msg = self.pesan['text']
         if msg == 'text':
             return self.heloworld()
         if msg == 'gambar':
             return self.gambar()
         else:
             return self.NoCommand()
