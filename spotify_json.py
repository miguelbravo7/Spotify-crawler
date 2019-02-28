import requests
import json
import csv

dos_primeras = 0

with open('regional-us-daily-2019-02-25.csv','r') as userFile:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, dialect='excel')        
        userFileReader = csv.reader(userFile)
        
        for row in userFileReader:
            
            if(dos_primeras<2):
                dos_primeras=dos_primeras+1
                writer.writerow(row)
                continue
            
            song_id=row[-1].split('/')
            #print(song_id[-1])
            url = 'https://api.spotify.com/v1/audio-features/' + song_id[-1]
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Bearer BQA86i8n84H4-_rEsk6kYea4oFXd7uIJO-JG5nDXz1UPh0TaDOlx4QiVYybVOKkTUXvpf1iWexsvyV1chrBmE-5A07RAFIWh5H3bfek2kXoA8VPeD7A0m3I8t9ca8EcjiNO7MaAo5-uD7A'}
            r = requests.get(url,  headers=headers)

            data=json.loads(r.text)
            array = []
            
            for key in data.keys():
                if key in("type", "id", "uri", "track_href", "analysis_url"):
                    continue
                array.append(data[key])
                
            #print(array)
            row.extend(array)
            writer.writerow(row)

        

