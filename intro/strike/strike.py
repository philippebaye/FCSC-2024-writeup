charset = 'abcdefghijklmnopqrstuvwxyz!# $:-().'

to_check = '# congratulations! this is a strike :-) you should now see the flag printed ... #'

c_delta = ''
for i in range(len(to_check)):
    c = to_check[i]
    c_in_charset = charset.index(c)
    v4 = (c_in_charset - 2*i) % 0x23
    print(f'{v4:02}, {v4:02x}')
    c_delta += f'{v4:02x}'

print(f'{c_delta=}')
