def encode_url(url):
    
    mapping = {
        'a': '01',
        'b': '02',
        'c': '03',
        'd': '04',
        'e': '05',
        'f': '06',
        'g': '07',
        'h': '08',
        'i': '09',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26',
        '.': '27',
        ':': '28',
        '/': '29'
    }
    

    encoded_url = ""
    for char in url.lower():
        if char.isalpha():
            encoded_url += mapping[char]
    
    return encoded_url

def decode_url(encoded_url):
    
    reverse_mapping = {
        '01': 'a',
        '02': 'b',
        '03': 'c',
        '04': 'd',
        '05': 'e',
        '06': 'f',
        '07': 'g',
        '08': 'h',
        '09': 'i',
        '10': 'j',
        '11': 'k',
        '12': 'l',
        '13': 'm',
        '14': 'n',
        '15': 'o',
        '16': 'p',
        '17': 'q',
        '18': 'r',
        '19': 's',
        '20': 't',
        '21': 'u',
        '22': 'v',
        '23': 'w',
        '24': 'x',
        '25': 'y',
        '26': 'z',
        '.': '27',
        ':': '28',
        '/': '29'
    }
    
   
    chunks = [encoded_url[i:i+2] for i in range(0, len(encoded_url), 2)]
    
  
    decoded_url = ""
    for chunk in chunks:
        if chunk in reverse_mapping:
            decoded_url += reverse_mapping[chunk]

    return decoded_url

choice = input("Enter '1' to encode a URL or '2' to decode an encoded URL: ")

if choice == '1':
    url = input("Enter a URL to encode: ")
    encoded_url = encode_url(url)
    print("Encoded URL:", encoded_url)
elif choice == '2':
    encoded_url = input("Enter an encoded URL: ")
    decoded_url = decode_url(encoded_url)
    print("Decoded URL:", decoded_url)