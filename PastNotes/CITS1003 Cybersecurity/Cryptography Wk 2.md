[[CITS1003 Cybersecurity]]

|   |   |
|---|---|
|Created|@March 2, 2023 10:31 AM|
|Class|CITS1003|
|Reviewed||

Cryptanalysis:

- Brute Force

- Letter Frequency

Transposition cypher: letters are rearranged, padded out with x’s to make a full grid

Block cypher: chunks of plaintext are manipulated

Stream cypher: encrypt data as a stream of bytes

Data Encryption Standard (DES):

- block length of 64 bits

- key length of 56 bits

- takes the key, then subkeys are generated

Cryptographic Hash Functions: operates one way, maps data of arbitrary size to a bit string of a fixed size, deterministic, fast to compute, difficult to generate message, small changes in messages result in large change in hash

- Can be used for password storage, never store the plaintext,

- Can also be used to confirm the message has not been changed

- Also for digital signature using the private key