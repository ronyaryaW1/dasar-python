data = {    'nama' : 'rony',
            'age'  : '10',
            'Sekolah': 'SMK TELKOM'
}

for key, value in data.items():
    print(key + "=" + value)

# menambahkan data 
data['Hobby'] = 'SIng'
# mengedit data
data['nama'] = 'Rina'
# menghapus data
del data['age']
print(data)