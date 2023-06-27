App infantil
============
CONSIDERACIONES IMPORTANTES
	-Instalar briefcase para uso de beeware 

	-Instalar MinGW y añardirlo en las variables de entorno de usuario
  	
		--PATH editar

		--Nuevo y agregar el directorio de instalacion de MinGW

---------Si estas usando Windows deberas instalar Zbarlight---------

-Abrir PowerShell (Si en algun punto sale algun error relacionado con scripts usar el siguiente comando "set-executionpolicy unrestricted –force")

-Con el comando CD dirigete a la carpeta que prefieras para copiar los repositorios de Zbarlight

-Copiar el repositorio con "git clone https://github.com/dani4/ZBarWin64"

  	--Haz una copia de ZBarWin64\lib\libzbar64–0.dll y renombrala a libzbar.dll

  	--Copia ZBarWin64\lib\libzbar64–0.dll y ZBarWin64\zbar\libiconv\dll_x64\libiconv.dll al directorio C:\Windows\System32

-ve hacia el directorio donde instalaste python y entra a la carpeta \Lib\distutils

  --crea el archivo "distutils.cfg" y añade estas lineas 

      	[build]

      	compiler = mingw32

  --Escribe las lineas de codigo de este link " https://bugs.python.org/file40608/patch.diff" en el archivo "cygwinccompiler.py"

-Vuelve a la carpeta principal donde estas clonando tus repositorios en powershell

-Vuelve a clonar un repositorio pero ahora con este link "https://github.com/Polyconseil/zbarlight"

------------powershell------------------
  --Escribe "cd zbarlight"

  --Escribe "python.exe -m venv env"

  --Escribe ".\env\Scripts\Activate.ps1"

  ------------Carpetas--------------

  --En el directorio de zbarlight abre con un editor "setup.py"

  --En la zona de codigo de "Extension" deberas agregar 

    	---include_dirs = [r"C:\MinGW\ZBarWin64\include"],

    	---library_dirs = [r"C:\MinGW\ZBarWin64\lib"],

  --Por ultimo usa tu compilador para correr el archivo "setup.py" seguido del comando "bdist_wheel" (Necesitaras Visual C++ 14 =>)

App infantil (nombre provisional)

.. _`Briefcase`: https://briefcase.readthedocs.io/
.. _`The BeeWare Project`: https://beeware.org/
.. _`becoming a financial member of BeeWare`: https://beeware.org/contributing/membership
