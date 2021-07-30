data = { 1:{'nama': 'Ardha', 'umur':'17', 'hobby':'ngaji'},
         2:{'nama': 'Afif', 'umur': '18', 'hobby': 'tilawah'}}
for key, value in data.items():
    print("\nData ke-:", key)
    for key2 in value:
            print(key2 + "=" + value[key2])