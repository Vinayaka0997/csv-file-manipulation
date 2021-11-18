import csv

players_data_older_than_30_reffered_by_google=[]

#read csv
with open('players_data.csv', 'r')as players:
    csv_dict_reader = csv.DictReader(players)


    for row in csv_dict_reader:
        #players must be older than 30
        #players must have been reffered by google

        age = int(row['age'])
        reffered_by = row['reffered_by']
        if age >= 30 and reffered_by == 'google':
            players_data_older_than_30_reffered_by_google.append({
                'name':row['name'],
                'email':row['email']
            })


#write new csv

with open('players_data_older_than_30_reffered_by_google.csv','w',newline='') as players_data_older_than_30_reffered_by_google_csv:
    fieldnames = ['name','email']
    csv_dict_writer = csv.DictWriter(players_data_older_than_30_reffered_by_google_csv,fieldnames=fieldnames)
    csv_dict_writer.writeheader()


    for players in players_data_older_than_30_reffered_by_google:
        csv_dict_writer.writerow(players)

