# REFERENCIA

El cifrado Trithemius es un método de cifrado polialfabético inventado
por Johannes Trithemius en el Renacimiento. Utiliza una tabla llamada "tabula recta"
que contiene el alfabeto desplazado varias veces. Cada letra del mensaje original se
sustituye por otra letra de la tabla, siguiendo un patrón determinado.
Este cifrado fue un avance importante en la criptografía de la época, ya que
dificultaba el descifrado de mensajes al usar múltiples alfabetos.

# EJEMPLO PRÁCTICO

Este ejemplo básico ilustra el principio de sustitución polialfabética utilizado el cifrado Trithemius.

Imaginemos que tenemos la siguiente tabla, llamada "tabula recta":
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
...
```
Cada fila es el alfabeto desplazado una posición respecto a la anterior.

Ahora, queremos cifrar el mensaje "HOLA". Para ello, usamos la primera fila
para la primera letra, la segunda fila para la segunda, y así sucesivamente.

- H se convierte en I (primera fila).
- O se convierte en P (segunda fila).
- L se convierte en M (tercera fila).
- A se convierte en B (cuarta fila).
  
Por lo tanto, el mensaje cifrado sería "IPMB".

Este es un ejemplo simplificado, en la práctica el cifrado Trithemius puede 
ser más complejo, utilizando claves y patrones de desplazamiento más elaborados. 


# PUZZLE COINMONKS

Post: https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254
- La frase semilla de la wallet se encuentra oculta en el articulo.

Wallet objetivo: https://mempool.space/es/address/1K4ezpLybootYF23TM4a8Y4NyP7auysnRo
* Saldo: ‎0.03124630 BTC
-----------------------------------------------

# EJECUTAR

En la ventana de comando copie la siguiente linea para ejecutar
```
python trithemius.py encrypted_text.txt REVOLUTION
```
- Agrege al final la "Palabra Clave" para que se cree la Tabula Trithemius.
- Modifique el "encrypted_text.txt" y agrege el texto a desencriptar.
- El archivo de texto contiene por linea el texto a descifrar.
  
# FUNCIONES

- Eliminación de signos de puntuación y caracteres especiales:
- Se utiliza la expresión regular r'[^\w\s]' para eliminar todo lo que no sea una letra, número o espacio en blanco.
- Se utiliza una segunda expresión regular r'[áéíóúÁÉÍÓÚ]' para eliminar los acentos.
- Conteo de caracteres: Se calcula la longitud de la línea limpia (cleaned_line) y se muestra al final de cada línea junto con el texto descifrado y resaltado.
- Encuentra todas las palabras (secuencias de letras) utilizando la expresión regular \b[A-Za-z]+\b.
- Resalta las palabras encontradas en ROJO utilizando códigos ANSI.
- Imprime la línea resaltada en la terminal.
- En la terminal puede ver el resultado en letra capital.

# SUGERENCIAS Y CONTACTO
- t.me/vortomastro

# APOYO Y DONACIONES
- BTC: bc1q3228g2cv73agw2xnfxvplaavepvwa2dl0ne9sm

