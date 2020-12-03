# Tribal
 Proyecto unificar varias API's con Flask

En este mi ejemplo he tomado inicialmente una validación a nivel de series. Basándome en pruebas de ambas API's 
encontré que iTunes limita el resultado de las consultas a un máximo 200 registros, mientras que TVmaze no 
reflejo esa limitación; esto último me presento la oportunidad de utilizar a TVmaze como base para presentar 
los datos unificados.

Para ello mi propuesta lo que hace es eliminar el diccionario que trae por defecto el resultado del API tomado 
como base (TVmaze), reconfigurarlo y luego asignar de nuevo los valores de una forma más cómoda para su posterior
recuperación. En el código del API puede verse el detalle para pre-procesar los registros recibidos de ambas API's.

En cuanto a los tiempos de respuesta considero que son adecuados para el proceso considerando la cantidad de 
registros devueltos por la consulta a dos origenes simultaneamente, sin embargo, la mejor opinión la tienen ustedes,
así que critiquen todo lo que se deba, ya que con eso aprendo más.

Mi intención final es trabajar en un match más preciso a nivel de registro, que vaya comparando cada fila procesada
dentro del primer bloque de datos contra todo lo que hay en el segundo (o en los que hayan), lo que permitirá ir 
agregando más criterios y mas información por cada ítem (por ejemplo películas, protagonistas, etc.).

Por ahora, y por razones de tiempo he trabajado solo un bloque (series), pero ya está listo el API para procesar 
películas y dejar unificado tal cual este "Endpoint". Sin embargo, para recuperar con una sola línea (desde el front) 
de búsqueda y luego unificar, sin poder utilizar otros criterios de los tantos recibidos me hace largo el proceso, 
pero la idea está plasmada y la subiré a futuro. 
