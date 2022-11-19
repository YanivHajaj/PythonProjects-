
# %% Functions
# decode a word(plaintext) using vigenere-cipher method
def decode(word,key): 
    word = str(word)
    index=0
    DDD_word=''
    for x in range (len(word)) : #all letter in decword
        ascii_sum= (ord(word[x])) + (ord(key[index])-97) #a(97) sub 0 b(98) sub 1...
        index+=1 #inc index
        if(index==(len(key))): #number of charcter in key 
            index=0 #return index to 1 
        if(ascii_sum>122): #97-122 a-z ascii 
            ascii_sum=ascii_sum-26
        DDD_word+=chr(ascii_sum)
    print(DDD_word)

# encode a word(cypertext) using vigenere-cipher method
def encode(dec_word,key):
    dec_word = str(dec_word)
    index=0
    enc_word=''
    for x in range (len(dec_word)) : #all letter in decword
        ascii_sum= (ord(dec_word[x])) - (ord(key[index])-97) #a(97) sub 0 b(98) sub 1...
        index+=1 #inc index
        if(index==(len(key))): #number of charcter in key 
            index=0 #return index to 1 
        if(ascii_sum<97): #97-122 a-z ascii 
            ascii_sum=ascii_sum+26
        enc_word+=chr(ascii_sum)
    return enc_word
    
    
# %% import  file
key='crypto'
input_file = open('C:/Users/yaniv/source/repos/cryptogrphy/ex1_vigenere_ciphertext.txt','r')
first_line=input_file.readline()
enc_word=encode(first_line,key)
input_file.close()
print(enc_word)

output_file = open("ex1_vigenere_plaintext.txt", "w")
output_file.write(enc_word)
output_file.close()