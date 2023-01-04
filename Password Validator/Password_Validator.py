checkset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
checksetnum = '0123456789'
checksetspec = '!@#$%&*'
while True:
    print('')
    pw = input()

    if len(pw)<=7:
        print('Weak')
        break
    elif len(pw.strip(checkset))-len(pw.strip(checkset).strip(checksetnum))<2:
        print('Weak')
        break
    elif len(pw.strip(checkset))-len(pw.strip(checkset).strip(checksetspec).strip(checksetspec))<2:
        print('Weak')
        break
    else:
        print("Strong")
        break