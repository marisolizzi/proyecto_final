<strong>Sobre el proyecto</strong>

Este proyecto es realizado como proyecto final del curso de Python de CoderHouse.

Fue terminado el 08 de febrero de 2024.

Básicamente es un catálogo, en este caso de celulares, pero que puede ser cualquier otro producto o contenido.
Posée una estructrua básica de Marca y Producto. Los celulares (producto final) se encuentran asociados a una Marca.
También posee un login de usuarios y un módulo o sección de administración, que permite editar el catálogo y los usuarios del sisitema.

De acuerdo a lo descripto anteriormente, posee una vista Publica y otra Privada.
Los usuarios que acceden verán las Marcas y Productos. Mientras que al logearse, además de la vista pública podrán acceder al sisitema de gestión del catálogo.

Fue desarrollado en Python utilizando el framework Django.

Internamente posee 3 Apps:
 <li>Catalogo, donde se encuentran los modelos, vistas y demás que engloban al catálogo propiamente dicho.</li>
 <li>Usuario, donde se manejan las vistas, urls y demás para la gestión de usuarios. En este caso el modelo utilizado es User, nativo de django.</li>
 <li>Sitio, donde se menejan los archivos genéricos que dan forma al sitio, por ejemplo el directorio estátcio (static), el template base, etc.</li>

 Vale aclarar que cada App también posee sus templates. Los templates son html. 

 A continuación agunas pantallas:

 
