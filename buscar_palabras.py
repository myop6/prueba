
def buscar_palabras(texto):

    palabras_clave = ['anular','substituir limitador','substituir manobra','casquilho','encasquilhar','não atua','atuaria',
                        'atauva','não  atuaria','adaptar','modernizar','substituir rolamento','limitador de velocidade',
                        'deslocar puerta','mover porta','modificar porta','mudar o limitador','trocar limitador', 'substituir lv',
                        'shuntar','instalar vf', 'trocar regulador','suprimir','adaptar fechadura','adaptar variador',
                        'trocar limitador', 'trocar vf','anular', 'sustituir limitador', 'sustituir maniobra', 'casquillo', 'encasquillar', 'anulado',
                      'no actúa', 'actuaría', 'actuaba','no actuaría', 'adaptar', 'modernizar','sustituir rodamiento',
                       'mover puerta','cambiar puerta','cambiar lv', 'cambiar limitador'
                      'sustituir lv','puentear','puntear','punteado','puenteado','instalar VF','instalar var','cambiar regulador','suprimir',
                      'adaptar cerr', 'adaptar variador','macizo','sustituir regulador','modificar','actua','actúa','no funciona','falta rodiillo','rodillo']


    if any(palabra in texto.lower() for palabra in palabras_clave):
        return "Sí"
    return "No"

'''anular', 'sustituir limitador', 'sustituir maniobra', 'casquillo', 'encasquillar', 'anulado',
                      'no actúa', 'actuaría', 'actuaba','no actuaría', 'adaptar', 'modernizar','sustituir rodamiento',
                       'mover puerta','cambiar puerta','cambiar lv', 'cambiar limitador'
                      'sustituir lv','puentear','puntear','punteado','puenteado','instalar VF','instalar var','cambiar regulador','suprimir',
                      'adaptar cerr', 'adaptar variador','macizo','sustituir regulador','modificar','actua','actúa','no funciona','falta rodiillo','rodillo'''
