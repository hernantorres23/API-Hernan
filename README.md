 **Proyecto unificar varias API's con Flask**

Comenzando con una validación a nivel de series y basándome en pruebas realizadas en ambas API's, encontré
que iTunes limita el resultado de las consultas a un máximo 200 registros, mientras que TVmaze no reflejó
esa limitación; esto último me presento la oportunidad de utilizar los resultados de TVmaze como base para
representar los datos unificados.  

**𝑃𝑎𝑟𝑎 𝑐𝑜𝑛𝑠𝑒𝑔𝑢𝑖𝑟 𝑒𝑙 𝑟𝑒𝑠𝑢𝑙𝑡𝑎𝑑𝑜, 𝑚𝑖 𝑝𝑟𝑜𝑝𝑢𝑒𝑠𝑡𝑎 ℎ𝑎𝑐𝑒 𝑒𝑠𝑡𝑜:**
1. eliminar el diccionario que trae por defecto el resultado del API tomado como base (en este caso TVmaze),
2. reconfigurar el diccionario tomado en el punto anterior
3. asignar nuevamente los valores al diccionario, pero ahora en una forma que nos permita recuperar los datos facilmente.  
En el código del API puede verse el detalle para pre-procesar los registros recibidos de ambas API's.

En cuanto a los tiempos de respuesta, los considere adecuados para el proceso teniendo en cuenta la cantidad de registros devueltos desde una consulta hacia dos origenes simultaneamente, sin embargo, la mejor opinión la tienen ustedes, así que critiquen todo lo que se deba, ya que con eso aprendo más, porque con toda seguridad cuando yo vea esto con mayor tranqulidad, empiezo darme cuenta de todo lo que deje de hacer.

En cuanto al codigo es bien explicito, para no decirle largo, pero cuando hay apuros prefiero dar el paso hacia la solucion y luego empiezar a reducir las lineas con mejores practicas, al final el cliente quiere todo instantaneamente, sin importar como lo logres.

Realmente muchas ideas vinieron a mi mente, pero al final mi intención es trabajar en un match bien preciso, es decir, a nivel de registro, algo que vaya comparando cada fila procesada dentro del primer bloque de datos contra todo lo que hay en el segundo (o en los que hayan), lo que permitirá ir agregando más criterios y mas información por cada ítem (por ejemplo películas, protagonistas, etc.).

En esta oportunidad y por razones de tiempo he limitado el enfoque a un solo bloque (**las series**), pero ya está listo el API para procesar películas y dejar unificado tal cual este "Endpoint"; sin embargo, para recuperar con una sola línea (desde el front) de búsqueda y luego unificar, sin poder utilizar (**el reto así lo requería**) otros criterios de los tantos recibidos y que con seguridad pudieran ser utiles para agregar criterios, se me hace largo el proceso, pero la idea está plasmada y la subiré a futuro.

**Hernan Torres**
