# Twitter-bot
Este bot selecciona de un archivo txt un link de Amazon Affiliate, tomado de manera aleatoria, 
que contiene un producto de Amazon y lo concatena con una frase motivadora, que puedes solicitar
a cualquier inteligencia artificial, para publicar un tweet cada 35 minutos.
Este bot está hecho para no gastar un centavo, y promocionar productos gratis y que te paguen por ello.
AMAZON TE PAGA UNA COMISION SI EL PRODUCTO ES COMPRADO USANDO TU LINK. BUSCA VIDEOS DE AMAZON AFFILIATE
Puedes adaptarlo y publicar cualquier frase. Lo conecté con las API de Chatgpt pero funcionaba con fallas por la cantidad de request que acepta chatgpt gratis.
Recuerda abrir una carpeta y colocar todo dentro de la misma carpeta. 
Puedes usar el idle que quieras, pero yo usé Visual Studio Code (VSC) en windows.

*************************************************************************************************************

Este bot es gratis, pero si quieres ayudarme como creador puedes donar:

btc 

	1LVocwYpWnd59Juyfhyum7JiVRXAmqAaWb

eth (bsc)

	0x44d27c323a0b0a7ec9d2cf2ccfa173f15ce27ef5

bnb (bsc)

	0x44d27c323a0b0a7ec9d2cf2ccfa173f15ce27ef5

xrp

	rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV


	Memo: 401375175

usdt (trx)

	TFjbSrQVmAqaeuGzUsPHVTM2nDD1LweY5k

rvn

	RFLbQboprMwgeuXGTPy3h6gW72Lvfgkgrs

*************************************************************************************************************

Instrucciones de Instalación

1- Instala Python y pip: Asegúrate de tener Python y pip instalados en tu sistema. 
   Puedes descargar Python desde [python.org](https://www.python.org/).

2- Instala las dependencias: Abre una terminal o línea de comandos y ejecuta los siguientes comandos
   para crear un entorno virtual (opcional) e instalar tweepy.

   EJECUTAR ESTE COMANDO EN EL TERMINAL

   sh

		  pip install tweepy

   Si te pide que actualices las funciones (install pip-24.1.2):

   sh

	   python.exe -m pip install --upgrade pip



3- Preparar Archivos

    Crear archivo tweets.txt: Este archivo debe contener los enlaces de productos que deseas twittear,
    uno por línea.

   
    Crear archivo frases.txt: Este archivo debe contener las frases motivacionales, una por línea.


    Crear archivo ejecutable: x-bot.py (pegar el código que está en el punto 6)



4- Configura tus claves API: Asegúrate de tener tus claves API V2 de Twitter. Para ellos debes 
   abrir tu cuenta de tweeter en https://developer.x.com/en

   Configurar Credenciales de Twitter:

   Reemplazar los valores de las variables en el archivo x-bot.py: 

   			API_KEY, API_SECRET_KEY, ACCESS_TOKEN 

   			ACCESS_TOKEN_SECRET

   			BEARER_TOKEN con tus propias credenciales de la API de Twitter.



5- Explicación del Código
   Lectura de Archivos: Se leen las frases motivacionales y los tweets desde los archivos frases.txt y
   tweets.txt.
   
   Selección Aleatoria Sin Repetición: Se selecciona un tweet y una frase motivacional de manera aleatoria
   y se aseguran de no repetirse hasta que todas las opciones hayan sido usadas. 
   Se usan conjuntos (set) para rastrear las frases y tweets ya usados.
   
   Reinicio del Proceso: Cuando todas las frases y tweets se han usado, se vacían los conjuntos
   para reiniciar el proceso y permitir que se usen nuevamente.
   
   Publicación del Tweet: Se publica el tweet en Twitter concatenando la frase motivacional y
   el enlace del producto.
   
   Espera: El bot espera 35 minutos antes de publicar el siguiente tweet. Este tiempo es para 
   evitar sobrepasar el límite de 1500 tweets mensuales para cuentas gratis.
   Las cuentas de pago pueden disminuir el tiempo de publicación entre tweets.

Estructura de los Archivos, copia y pega cuantos quieras.
tweets.txt:

 	https://www.amazon.com/producto1
 	https://www.amazon.com/producto2
 	https://www.amazon.com/producto3

frases.txt:

	¡No te pierdas este increíble producto!
	Este producto puede cambiar tu vida. ¡Pruébalo ahora!
	¡Aprovecha esta oportunidad única con este producto!
	¡Descubre las maravillas de este producto hoy mismo!


Con este enfoque, el bot garantizará que todas las frases y todos los enlaces se publiquen
de manera aleatoria y sin repetición hasta que se hayan utilizado todas las opciones, 
momento en el cual el proceso se reiniciará.


6- Abre un archivo llamado "x-bot.py" y pega el siguiente código:

    Incluido en el archivo x-bot.py

7- En el terminal ejecuta el siguiente comando:

sh
python x-bot.py  


DISFRUTA TU CÓDIGO!!!!
