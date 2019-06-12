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

# This part is used to display the 
# working of the set command
####################################################
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902
cg= cmdgen.CommandGenerator()
comm_data= cmdgen.CommunityData('my-manager', 'public')
transport= cmdgen.UdpTransportTarget(('192.168.43.1',161))
variables = ((1,3,6,1,2,1,1,1,0), rfc1902.OctetString('new System Description'))
errIndication, errStatus, errIndex , result= cg.setCmd(comm_data, transport, variables)
print( errIndication)
print(errStatus)
print(errIndex)
print(result)

# woking with the GETNEXT COMMAND

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902
cg= cmdgen.CommandGenerator()
comm_data= cmdgen.CommunityData('my-manager', 'public')
transport= cmdgen.UdpTransportTarget(('192.168.43.1',161))
variables=(1,3,6,1,2,1,1)
errIndication, errStatus, errIndex , result= cg.nextCmd(comm_data, transport, variables)
print( errIndication)
print(errStatus)
print(errIndex)
print(result)
for object in result:
	print object
	# ## The result is indentical to that produced by the
	# command-line tool snmpwalk, which uses the same technique to
	# retrieve the SNMP OID subtree 




