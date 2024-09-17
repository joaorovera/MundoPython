var = input('Digite algo: ')

print(f'O tipo é {type(var)}')
print('Isso é alfabético?', var.isalpha())
print('Isso é numérico?',var.isnumeric())
print('Isso é somente espaços?',var.isspace())
print('Isso é alfanumérico?',var.isalnum())
print('Isso é tudo minúsculo?',var.islower())
