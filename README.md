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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

la cuenta de administrador es la misma que antes, al igual se incorporó una más la cual es 
koala1 / olidata000

atributos:
rut = username
contraseña = password

el proyecto conserva lo que es su crud y sus funcionalidades, sin embargo pensamos en no solo agregar el login y el sistema de permisos (ademas de subirlo al servidor).
si no que tambien añadimos 2 nuevas funcionalidades las cuales 1 de ellas esta presente en el proyecto final, la funcionalidad del proyecto final es basicamente mostrar los pedidos asociados a una cuenta, es decir a su username. Por ejemplo si yo hago un pedido de comida con el rut x entonces inmediatamente me voy a la sección de mis pedidos y encontraré dicha petición realizada.

 sin embargo este sistema digamos que esta en algo de beta ya que como el crud fue realizado antes que el login se nos fue el paso de que al realizar un pedido nos requiere un rut , cosa que el rut la pagina ya lo tiene, por ello ese paso sentimos que es algo innecesario y queriamos sintetizarlo pero quisimos evitar riesgos de dañar el proyecto, por ello preferimos explicarlo. Por otro lado tambien pensamos en requerir ese rut ya que teniamos pensado añadir una especie de modo familiar, el cual podrá asociar diferentes cuentas a una sola, es decir que una cuenta puede hacer pedidos por otro rut. En fin lo importante es que se entiende el uso que se le quiere otorgar a dicha sección

(al momento de realizar un pedido el numero del rut tiene que ser el mismo valor ingresado que en el username(rut) para que aparezca en mis pedidos, disculpe esta acotación pero arriba explique la razón de porque es así el funcionamiento)

Otra funcionalidad que añadimos, sin embargo no se encuentra en el proyecto final es la capacidad de mandar correos electronicos, la cual servia para evidenciar la transacción de dicho pedido (no lo incluimos debido a que este con pythonanywhere se cae, ya que requiere de un servidor de google o alguno dedicado)

Una vez ya mencionadas las 2 funcionalidades procedemos a lo que es la evaluación.

La pagina basicamente fue realizada con un login ejercido mediante funciones, en el cual para filtrar permisos usamos el atributo staff del paquete user y la función is_authenticated. El crud esta solamente accesible para las cuentas superuser, en cambio las normales solo pueden navegar por la pagina principal, realizar pedidos y observar sus pedidos. La pagina cuenta seguridad tanto como en su front-end como en sus url, vale decir que si yo intento colocar en la url payment_food_list, me arrojara un error en el cual dice que no tengo permisos suficientes

Sin nada más que mencionar muchas gracias por todo, espero que se encuentre bien