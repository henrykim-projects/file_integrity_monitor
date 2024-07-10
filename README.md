<h1>File Integrity Monitor</h1>


<h2>Description</h2>
A file integrity monitor (FIM) demonstrates an essential concept of Cyber Security, namely 'integrity' found in the CIA (Confidentiality, Integrity, Accessibility) triad. Integrity is essential principle, noting whether data stored by the user has been untouched and unaltered by an unintended party. The FIM checks if a file has been altered, and provides an alert whether the file has been breached or integrity has been maintained. Here, I have constructed a rudimentary FIM solely using Python commands. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>[CS50](https://github.com/thethirdbirthday/harvard_python)</b>

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Program walk-through:</h2>

<p align="center">
First, the FIM must locate the target file. A specific file can be selected using the open() function - here the text file <i>confidential.txt</i> is designated to be opened and read: <br/>
<img src="https://github.com/thethirdbirthday/file_integrity_monitor/blob/8223776a5e71b85010cb726a90b2801d96973f98/images/fim_1.PNG" height="80%" width="80%" alt="FIM"/>
<br />
<br />
Let's confirm the information we are protecting. Opening the file reveals the sensitive information within:  <br/>
<img src="https://github.com/thethirdbirthday/file_integrity_monitor/blob/ddcf27e9dda495fa936f78b225d3142c77a2ef81/images/fim_3.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br/>
<br />
Returning to the code, we will add a conditional where if the message is the same "There is no change" will be returned. Otherwise, we will know "There is a change!": <br/>
<img src="https://github.com/thethirdbirthday/file_integrity_monitor/blob/d4e16befabb004ce9a4340fa7970d816e8bd78e1/images/fim_2.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br/>
To test the FIM, running it correctly indicates that "There is no change" meaning the file has maintained integrity: <br/>
<img src="https://github.com/thethirdbirthday/file_integrity_monitor/blob/501032971b54803e729237764b33256bcd84d113/images/fim_4.PNG" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br/>
However, in the case of a breach by a hacker, or perhaps unauthorized access by an employee who has unintentionally been given access, let's test the result when the file has been altered: <br/>
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
