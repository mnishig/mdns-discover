# mdns resolve use dnspython

import dns.resolver

myRes = dns.resolver.Resolver()
myRes.nameservers = ['224.0.0.251'] #mdns multicast address
myRes.port = 5353 #mdns port

#NAME = 'mna.local'
NAME = 'exhd-817961.local'
PTR = '17.1.168.192.in-addr.arpa'
PTR = '43.1.168.192.in-addr.arpa'

a = myRes.resolve(NAME, 'A')
print(a[0].to_text())
#'10.0.0.7'

a = myRes.resolve(PTR, 'PTR')
print(a[0].to_text())
#'Microknoppix.local.'
