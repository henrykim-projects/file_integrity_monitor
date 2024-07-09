<h1>File Integrity Monitor</h1>


<h2>Description</h2>
This project aims to explore the concepts of the CIA triad by creating a file integrity monitor with Python. There will be an initial 'mold' solely using knowledge from the CS50 course, then will be gradually built upon with libraries and hash files. Ultimately, the program will read through a designated text file and check if a change has been made. Then it will provide the appropriate alert repsonse depending on whether or not the file has maintained integrity. This project delves into software development and cyber security. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>[CS50](https://github.com/thethirdbirthday/harvard_python)</b>
- <b>Oracle Virtual Box</b>

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Program walk-through:</h2>

<p align="center">
Create a Domain Controller VM installed with Server 2019: <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/main/ad_1.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Distinguish home internet and internal network:  <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/main/ad_2.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br/>
<br />
Add Active Directory Domain Services: <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/8cf3a9f5c735d42d45c55cfb79462702e2eed85e/ad_3.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br/>
Create admin account: <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/d16bfe521e26cce607b68e6115dadc69c66e12a3/images/ad_5.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br/>
Add Remote Access: <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/2e89cf54db7acecf70c92f16cfd937e15d21f40c/images/ad_NAT.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /> 
<br/>
Configure NAT in Routing and Remote Access: <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/2e89cf54db7acecf70c92f16cfd937e15d21f40c/images/ad_remoteaccess.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />  
<br />
Set DHCP server scope of IP addresses:  <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/3d1348440261b9f3aeda47158482a7c1f5d75ad0/ad_35.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Create User Accounts with PowerShell script:  <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/3d1348440261b9f3aeda47158482a7c1f5d75ad0/ad_39.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Create client VM connected only to internal network :  <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/3d1348440261b9f3aeda47158482a7c1f5d75ad0/ad_46.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Client IP address and default gateway will correspond with Domain Controller and DHCP:  <br/>
<img src="https://github.com/thethirdbirthday/Active-Directory/blob/2e89cf54db7acecf70c92f16cfd937e15d21f40c/images/ad_usercomplete.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<h2>Final Thoughts</h2>
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
