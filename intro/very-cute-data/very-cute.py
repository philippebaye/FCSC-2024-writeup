with open('very-cute-data.vcd', 'r') as data_file:
    datas = data_file.readlines()[6:]

debut_capture = 300_000
fin_capture = 2000_000

capture = []

for timestamp, signal in zip(datas[::2], datas[1::2]):
    timestamp, signal = timestamp.strip(), signal.strip()
    timestamp = int(timestamp[1:])
    valeur_signal = signal[:-1]
    type_signal = signal[-1:]
    if type_signal == '!':
        signal_D0 = valeur_signal
    elif type_signal == '"':
        signal_D1 = valeur_signal
        if (signal_D1 == '0') and (debut_capture <= timestamp <= fin_capture):
            # Transition signal D1 de 1 à 0 => capture de D0 à prendre
            capture.append(signal_D0)
    else:
        print("bug dans l'algo !!!")
        print(timestamp, signal)
        quit()
    pass

capture = ''.join(capture)
print(f'flag=FCSC{{{capture}}}')
