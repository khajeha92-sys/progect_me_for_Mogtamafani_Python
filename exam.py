import pyttsx3

engine = pyttsx3.init()
text = input('Write the text: ')
name = f'voise_output.mp3'
    
engine.save_to_file(text, name)    
engine.runAndWait()

print('The audio file was created ©')
