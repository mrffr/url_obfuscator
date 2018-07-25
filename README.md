# url obfuscator

Randomly obfuscates a url using a few methods.

* Replacing hostname with IP.
  * Obscuring the IP by using octal, hexadecimal or decimal representations or a mixture of the three.
* Adding dummy auth information before hostname, ie. anything preceeded by @.
* Replacing characters with their ascii values.

Use \-\-no_host option if you get errors related to content delivery networks.

For example this file here is at:  
<https://ge:(tOz,R5mJTblahblah.com.org.123@github.com/%6drf%66%72/u%72%6c_%6fb%66%75%73c%61tor/b%6cob/master/%52%45%41%44%4dE.m%64>  
And cannot be accessed without the hostname github.com.  
