def notas(*n, situacao=False):
    resultado = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n) / len(n)
    }
    
    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado['situacao'] = 'RUIM'
    
    return resultado


resp = notas(5.5, 9.5, 7.0, 6.5, situacao=True)
print(resp)