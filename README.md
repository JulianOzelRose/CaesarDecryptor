# Caesar Cipher Decryptor
This program decodes a single line of Caesar cipher-encrypted
text using a two-pronged approach; brute force and simple heuristics. The program
produces 12 decryption results, then prints two lists. The first list contains
all 12 decryption keys with their results. The second list contains the decryption results
which contain keywords.

# Caesar Cipher
![Caesar-cipher](https://user-images.githubusercontent.com/95890436/209759606-fd1893a9-0eea-4d11-b8f1-ee694274132f.png)

A Caesar cipher is a simple encryption technique named after Julius Caesar, who used the technique when communicating sensitive information.
It uses a shift cipher to move a plaintext character a fixed amount of spaces apart in the alphabet. For example, a shift value of +3 would shift ```abcd``` to ```defg```. The downside to using a Caesar cipher is that it is relatively easy to decrypt.



# Program Screenshot
![Untitled-1](https://user-images.githubusercontent.com/95890436/199611621-21a04a04-6a69-4c33-984c-70202a674fff.png)

In this screenshot, the original plaintext is displayed as key #0. Since key #9 contained the keywords ```attack``` and ```easternfront```, it is printed as a likely result. To
decrypt a line of text, simply store it in a text file and enter the filename when prompted. The program then prompts for a filename to save the result
to.
