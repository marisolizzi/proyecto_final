<h1>Sobre el proyecto</h1>

<p>Este proyecto es realizado como proyecto final del curso de <strong>Python</strong> de <strong>CoderHouse</strong>.</p>
<p>Fue terminado el 08 de febrero de 2024.</p>
<p>Fue desarrollado por Marisol Izzi. </p>
<p>Básicamente es un catálogo, en este caso de celulares, pero que puede ser cualquier otro producto o contenido.</p>
<p>Posee una estructura básica de Marca y Producto. Los celulares (producto final) se encuentran asociados a una Marca. El usuario primeramente accede a la lista de Marcas, al seleccionarla va a los modelos, y desde cada modelo se podrá acceder a al ampliación de la información. También posee un buscador donde se podrá buscar un modelo en la Marca en la cual está posicionado.</p>
<p>También posee un login de usuarios y un módulo o sección de administración, que permite editar el catálogo y los usuarios del sistema.</p>

<p>De acuerdo a lo descripto anteriormente, posee una vista pública y otra privada.
Los usuarios que acceden verán las Marcas y Productos. Mientras que al logearse, además de la vista pública podrán acceder al sistema de gestión del catálogo.


<h1>Características del desarrollo</h1>

<p>Fueron respetadas en su totalidad las consignas del curso para el proyecto final.</p>
<p>Fue desarrollado en Python utilizando el framework Django. El manejador de base de datos es Sqlite3.</p>
<p>Para el css se utilizó Bootstrap y algunos estilos extraídos de la web y adaptados a la aplicación.</p>
<p>Fueron realizados los CRUDS para cada modelo, incluyendo imagen para las Marcas y Modelo.</p>
<p>Internamente posee 3 Apps:</p>
 <li>Catalogo, donde se encuentran los modelos, vistas y demás que engloban al catálogo propiamente dicho.</li>
 <li>Usuario, donde se manejan las vistas, urls y demás para la gestión de usuarios. En este caso el modelo utilizado es User, nativo de django.</li>
 <li>Sitio, donde se menejan los archivos genéricos que dan forma al sitio, por ejemplo el directorio estátcio (static), el template base, etc.</li>
</p>
 <p>Vale aclarar que cada App también posee sus Templates. Los Templates son HTML.</p> 

<h1>Pantallas</h1>h1>
<p>Inicio de la web, donde se visualizan las marcas.</p>
<br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/080944f0-988d-4e83-9599-703e77ebb994">
<br>
<p>Vista de los modelos por Marca.</p>
<br>
 <img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/037a717c-1e6a-4ee2-97f1-1fd1a5a5edc2">

 <br>
<p>Vista de la información ampliada del modelo.</p>
<br>
 <img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/1d2554c5-e1a4-4c4b-b760-3d27222bd34e">
<br>

<p>Vista del Login de Usuario.</p>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/1a3b8476-8098-4801-9f85-78552ef36767"></p>
<p>Vistas de la gestión de contenidos (Marcas, Modelos y Usuarios)<br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/bf6c5e1f-8663-4e6f-8004-f29101ded7d8"><br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/4cde8b21-71a4-4f4d-9dc5-5063ff1cb9b3"><br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/0eb43429-0297-4bf7-b1b9-bd661b6d1e61"><br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/999f0435-fe02-47c1-9385-ea9d4bc3debe"><br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/9384f42f-48e1-460e-8974-fcc4a6335aa1"><br>
<img src="https://github.com/marisolizzi/proyecto_final/assets/70345802/3f9d0e01-72cb-43f1-92c8-f6cbf5f686c7"></p>

