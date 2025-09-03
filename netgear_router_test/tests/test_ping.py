import os
import platform

def test_ping_router(router_ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    result = os.system(f"ping {param} 2 {router_ip}")
    assert result == 0, f"Ping to {router_ip} failed!"
