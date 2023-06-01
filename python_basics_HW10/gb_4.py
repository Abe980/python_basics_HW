

text = '''She sells sea!    shells on the sea shore The: shells    that she sells are sea shells 
Im sure So if she sells sea shells^ on     the sea shore Im sure/    that the shells are sea shore shells'''


text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('!', '')

text = text.lower().split()

print(text)
print(len(set(text)))

