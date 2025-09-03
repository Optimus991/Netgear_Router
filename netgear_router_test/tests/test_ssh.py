import paramiko

def test_ssh_login(router_ip, credentials):
    username, password = credentials
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(router_ip, username=username, password=password, timeout=5)
        stdin, stdout, stderr = client.exec_command("uname -a")  # Example command
        output = stdout.read().decode()
        assert output.strip(), "SSH command returned no output"
    finally:
        client.close()
