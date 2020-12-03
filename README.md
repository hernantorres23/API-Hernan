# Tribal
 Proyecto unificar varias API's con Flask

 En este caso he tomado inicialmente una validacion a nivel de series.
 Basandome en pruebas de ambas API's encontre que iTunes limita sus registros a 200
 como maximo, mientras que tvMaze no reflejo esa limitacion; esto ultimo me presento 
 la oportunidad de tomar como base a tvMaze para presentar los datos unificados.

 Para ello mi propuesta lo que hace es eliminar el diccionario que trae por defecto el
 resultado del API tomado como base, reconfigurarlo y luego asignar de nuevo los valores
 de una forma mas comoda para su posterior recuperacion. En el codigo del API puede verse
 el detalle para pre-procesar los registros recibidos de ambas API's.

 En cuanto a los tiempos de respuesta considero son buenos para el proceso y tomando en 
 consideracion la cantidad de datos devueltos, sin embargo la mejor opinion la tienen
 ustedes, asi que critiquen todo lo que se deba, ya que con eso aprendo mas.

 Mi intencion final es trabajar en un match mas preciso a nivel de registro, que vaya 
 comparando cada fila procesada dentro del primer bloque de datos contra todo lo que hay 
 en el segundo, lo que permitira ir agregando mas criterios (por ejemplo peliculas).

 Por ahora, y por razones de tiempo he trabajado solo un bloque (series), pero ya esta listo 
 el API para procesar peliculas y dejar unificado tal cual este, sin embargo, para recuperar 
 con una sola linea (desde el front) de busqueda y luego unificar, sin poder utilizar otros
 criterios de los tantos recibidos me hace largo el proceso pero la idea esta plasmada y la
 subire a futuro.
