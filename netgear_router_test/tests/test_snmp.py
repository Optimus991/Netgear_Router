from pysnmp.hlapi import *

def test_snmp_sysname(router_ip, snmp_community):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(snmp_community),
        UdpTransportTarget((router_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))  # sysName
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    assert not errorIndication, f"SNMP error: {errorIndication}"
    assert not errorStatus, f"SNMP error status: {errorStatus.prettyPrint()}"
    assert varBinds, "No SNMP response received"
