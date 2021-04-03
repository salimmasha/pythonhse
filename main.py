f = open('the_matrix.txt','r')
f = f.readlines()
neo_speech = open("neo_speech.txt", "w") 

speech_number = 1

for n, line in enumerate(f):
    if line.strip().startswith('NEO'):
        neo_speech.write(str(speech_number) + '\n')
        speech_number += 1
        i = 1

        while f[n+i] != '\n' and f[n+i].strip().startswith('THE MATRIX') == False:
            neo_speech.write(f[n+i].strip() + '\n') 
            i += 1


