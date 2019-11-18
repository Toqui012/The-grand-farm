La cuenta administrador es 

user : toqui12
pass : olidata123

el crud esta listo
tiene 2 filtros y si lo deja vacio retornara todos los objetos, puede listar por id del objeto y rut
Puede agregar/eliminar/actualizar pedidos de comida solamente. Basicamente tiene todo el crud
El proyecto esta hecho en base a funciones y en base a query set ya que queriamos personalizar mas detalladamente tal comportamiento del codigo,
en cambio de la otra manera nos limitaba un poco, por ello quisimos tomar la desición de hacer el proyecto en base a funciones.

La sección de comida del proyecto esta ok con el crud y con los listar. Las pruebas tambien estan efectuadas

Las pruebas basicamente tiene que ver con la eliminación y agregación de diversos objetos, al igual tiene implementado la cantidad de objetos que se encuentran en la bd. Tambien coloque un buscador para verificar si efecivamente se han borrado o modificado algunos productos, de manera que asi podemos ver si queda alguna clase de registro o cache de dichos objetos gestionados.

Las pruebas estan en farm_app/ test.py y la ejecutamos con "python manage.py test farm_app"

si usted se va a la lista de productos deja en la misma sección borrar y actualizar los productos (pedidos alimentos --> ver pedidos)
para agregar usted se va a comida y en la parte de abajo tiene el formulario para poder generar la compra

Cuando usted elimina el objeto y quiere buscar despues algun otro objeto se recomienda volver acceder a la sección de volver pedidos para restablecer la url, ya que osino tirará error con la url y arojará  un error de que no existe tal url

paso 1: Borrar
paso 2: seleccionar pedidos
paso 3: Filtrar


Vuelvo a recalcar que todo crud y pruebas y filtros estan funcionando

Ante cualquier duda estaremos disponible, la verdad me cuesta explicar algo por aca y preferia presentación pero bueno