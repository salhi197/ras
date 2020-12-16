import os
audios = os.listdir('./test_audios')
audio_file_name = audios[1]
audio_file = ";/audios/"+audio_file_name
cmd = 'mpg321 '+audio_file+' &'
# os.system(cmd)
print(cmd)