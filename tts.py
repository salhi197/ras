import os
cmd_beg = 'espeak '
speed = 120
ticket  = input('Entrer le numero de ticket : ') 
# text    = "ticket numero"+ticket+" va au gichet "+gichet
command = '-vfr+f2 -a50 -s'+str(speed)+' "ff le ticket numero  '+str(ticket)+'"'
os.system(cmd_beg+command) 
# from num2word import num2words
# from subspaces import call
# cmd_beg = 'espeak '
# ticket  = input('Entrer le numero de ticket : ') 
# gichet  = input('Entrer le numero de gichet : ') 
# text  = "ticket numero"+ticket+" va au gichet "+gichet
# call([cmd_beg+text]) 

