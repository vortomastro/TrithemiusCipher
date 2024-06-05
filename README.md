Este código hace parte de un conjunto de herramientas
para descrifrar el texto del puzzle Coinmonks
link: https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254
Wallet objetivo: https://mempool.space/es/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo
Saldo: ‎0.03124630 BTC
-----------------------------------------------
Un simple codigo, basado en el cifrado Trithemius
El archivo de texto contiene por linea el texto  a descifrar
use simplemente la siguiente linea para ejecutar
python trithemius.py encrypted_text.txt REVOLUTION

Funciones:

Eliminación de signos de puntuación y caracteres especiales:
Se utiliza la expresión regular r'[^\w\s]' para eliminar todo lo que no sea una letra, número o espacio en blanco.
Se utiliza una segunda expresión regular r'[áéíóúÁÉÍÓÚ]' para eliminar los acentos.
Conteo de caracteres: Se calcula la longitud de la línea limpia (cleaned_line) y se muestra al final de cada línea junto con el texto descifrado y resaltado.
Encuentra todas las palabras (secuencias de letras) utilizando la expresión regular \b[A-Za-z]+\b.
Resalta las palabras encontradas en rojo utilizando códigos ANSI.
Imprime la línea resaltada en la terminal.
