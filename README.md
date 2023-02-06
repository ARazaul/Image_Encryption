# Binary File Encryption/Decryption Tool

This tool provides the ability to encrypt and decrypt binary files. 
The tool takes a binary file located at a specific path, encrypts it and saves the encrypted file to a different path. 
The encrypted file can then be decrypted and saved to yet another path. 

The encryption and decryption processes use a random number generator that is seeded by a `passlock` value provided by the user. 
The `passlock` value is used to ensure the same encryption/decryption result every time the tool is run with the same value. 

The tool contains two functions, `encrypt` and `decrypt`, that handle the encryption and decryption processes, respectively. 
When the tool is run, both functions are executed, encrypting and then decrypting the binary file. 

Note: The paths to the binary files and the range of the random number generator seed are hard-coded in the tool and should be changed as needed.
