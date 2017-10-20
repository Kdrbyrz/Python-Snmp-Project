from urllib.request import Request,urlopen
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
    '1.3.6.1.2.1.1.1.0', #system description
    '1.3.6.1.2.1.1.6.0'  #location
)

# Check for errors, print out and post results
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            request = Request('Target_UrlorIp',data=val.prettyPrint())            
        print("Data Sent Successful")
