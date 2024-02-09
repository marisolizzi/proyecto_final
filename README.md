<strong>Sobre el proyecto</strong>

<p>Este proyecto es realizado como proyecto final del curso de <strong>Python</strong> de <strong>CoderHouse</strong>.</p>
<p>Fue terminado el 08 de febrero de 2024.</p>
<p>Fue desarrollado por Marisol Izzi. </p>
<p>Básicamente es un catálogo, en este caso de celulares, pero que puede ser cualquier otro producto o contenido.</p>
Posée una estructrua básica de Marca y Producto. Los celulares (producto final) se encuentran asociados a una Marca.</p>
<p>También posee un login de usuarios y un módulo o sección de administración, que permite editar el catálogo y los usuarios del sisitema.</p>

<p>De acuerdo a lo descripto anteriormente, posee una vista Publica y otra Privada.
Los usuarios que acceden verán las Marcas y Productos. Mientras que al logearse, además de la vista pública podrán acceder al sisitema de gestión del catálogo.


<strong>Características del desarrollo</strong>

Fueron respetadas en su totalidad las consignas del curso para el proyecto final.
Fue desarrollado en Python utilizando el framework Django. El manejador de base de datos es Sqlite3.
Para el css se utilizó Bootstrap y algunos estilos extraidos de la web y adaptados a la aplicación.
Internamente posee 3 Apps:
 <li>Catalogo, donde se encuentran los modelos, vistas y demás que engloban al catálogo propiamente dicho.</li>
 <li>Usuario, donde se manejan las vistas, urls y demás para la gestión de usuarios. En este caso el modelo utilizado es User, nativo de django.</li>
 <li>Sitio, donde se menejan los archivos genéricos que dan forma al sitio, por ejemplo el directorio estátcio (static), el template base, etc.</li>
<br>
 Vale aclarar que cada App también posee sus templates. Los templates son html. 

 <strong>Algunas pantallas</strong>

 
