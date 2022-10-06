import string
abjad = string.printable

def enkrip(pesan) :
    global abjad

    key = int(input(' Masukan Key / pergeseran   :   '))
    cipher = '' #Menampilkan chiper enkripsi
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) # Menentukan Variable sebelumnya yang sudah di panggil
            k = (k+key)%100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekrip(cipher) :
    global abjad
    key = int(input(' Masukan key / pergeseran   : '))
    pesan = '' # Menampilkan pesan dekripsi
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k-key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan +i
    return pesan

if __name__ == '__main__' :
    print('-----------------------------------')
    print('|--------Anshar Rahmawan----------|')
    print('|---------- 312010308 ------------|')
    print('-----------------------------------')

    option = int(input('1. Enkripsi\n2. Dekripsi\npilih option      :   '))
    if option == 1:
        pesan = input(' masukan pesan ( palintext)  :   ') 
        print(enkrip(pesan))
    elif option == 2:
        cipher = input('masukan pesan  (chipertext)    :    ')
        print(dekrip(cipher))
    else:
        print(' masukan pilihan 1 atau 2')

