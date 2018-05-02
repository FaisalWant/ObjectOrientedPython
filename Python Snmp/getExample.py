#getExample.py

from pysnmp.entity.rfc3413.oneliner import cmdgen
cg = cmdgen.CommandGenerator()
comm_data = cmdgen.CommunityData('my-manager', 'public')
transport = cmdgen.UdpTransportTarget(('192.168.43.1', 161))
variables = (1, 3, 6, 1, 2, 1, 1, 1, 0)
errIndication, errStatus, errIndex, result = cg.getCmd(comm_data, transport, variables)
print (errIndication)
print (errStatus)
print (errIndex)
print (result)
