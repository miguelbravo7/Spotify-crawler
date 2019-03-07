import requests
import json
import csv
import sys

dos_primeras = 0
peticiones = 0
acc_keys = []
acc_rows = []
acc_array = []



with open('regional-us-daily-2019-02-25.csv','r') as userFile:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, dialect='excel')        
        userFileReader = csv.reader(userFile)
        
        for row in userFileReader:
            peticiones += 1
            if(dos_primeras<2):
                dos_primeras=dos_primeras+1
                writer.writerow(row)
                continue
            
            song_id=row[-1].split('/')
            #print(song_id[-1])
            acc_keys.append(song_id[-1])
            acc_rows.append(row)
            if(peticiones < 90):
                continue
            
##            print(acc_rows)
            
            url = 'https://api.spotify.com/v1/audio-features/?ids=' + "%2C".join(acc_keys)
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Bearer BQC6lfA8c7lTu0bUideIi2gavCIYRk_OZqmMbyb8lVEU8mxqHEhCJsslamzCp4w3wPp8CYxj58-z3SCUc-jrhrEt01GQW_OsMRtwASrJMpWadUF17dxNrNV5mBDQMkgT9HqRPOm-JzZO3Q'}
            r = requests.get(url,  headers=headers)

            data=json.loads(r.text)
##            print(data['audio_features'])
            
            try:
                for song in data['audio_features']:
                    array = []
                    for key in song.keys():
                        if key in("type", "id", "uri", "track_href", "analysis_url"):
                            continue
                        array.append(song[key])
                    acc_array.append(array)
    ##            print(acc_array)
                for lineas in acc_rows:
                    features = acc_array.pop(0)
                    print(features)
                    lineas.extend(features)
    ##                print(lineas)
                    writer.writerow(lineas)
            except:
                print(data)
                print('https://api.spotify.com/v1/audio-features/?ids=' + "%2C".join(acc_keys))
            

        

