import yaml
from yaml.loader import SafeLoader

#with open('C:\Github\PythonApps\Yaml\db.yaml') as fh:
#    read_data = yaml.load(fh, Loader=yaml.FullLoader)

read_data = yaml.load(open('C:\Github\PythonApps\Yaml\db.yaml'),Loader=yaml.FullLoader)
    
host = read_data['pg_host']
user = read_data['pg_user']
password = read_data['pg_password']
database = read_data['pg_db']
port = read_data['pg_port']

print('host ',host)
print('user ',user)
print('password ',password)
print('database ',database)
print('port ',port)
print(str(read_data))
    
print(read_data)

sorted_data = yaml.dump(read_data)

print(sorted_data)