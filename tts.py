import os
cmd_beg = 'sudo espeak '
speed = 120
ticket  = input('Entrer le numero de ticket : ') 
#f  = input('frequence : ') 
# text    = "ticket numero"+ticket+" va au gichet "+gichet
audio_file = "/audios/"+str(p)+".mp3"
cmd = 'mpg321 '+audio_file+' &'
os.system(cmd)
#command = '-vfr+f'+str(f)+' -z -a50 -s'+str(speed)+' "ff on apelle le ticket numero  '+str(ticket)+'"'
# audio_number = "aplay ./audios/"+ticket+".wav"
#command = '-vfr+f3 -z -a50 -s120 "'+str(ticket)+'"'
#os.system(cmd_beg+command)
# os.system(audio_number)

# from num2word import num2words
# from subspaces import call
# cmd_beg = 'espeak '
# ticket  = input('Entrer le numero de ticket : ') 
# gichet  = input('Entrer le numero de gichet : ') 
# text  = "ticket numero"+ticket+" va au gichet "+gichet
# call([cmd_beg+text]) 

