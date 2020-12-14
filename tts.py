import os
cmd_beg = 'sudo espeak '
speed = 120
ticket  = input('Entrer le numero de ticket : ') 
#f  = input('frequence : ') 
# text    = "ticket numero"+ticket+" va au gichet "+gichet
command = '-vfr+f'+str(f)+' -z -a50 -s120 "ff on apelle le ticket numero  '+str(ticket)+'"'
os.system(cmd_beg+command) 
# from num2word import num2words
# from subspaces import call
# cmd_beg = 'espeak '
# ticket  = input('Entrer le numero de ticket : ') 
# gichet  = input('Entrer le numero de gichet : ') 
# text  = "ticket numero"+ticket+" va au gichet "+gichet
# call([cmd_beg+text]) 

