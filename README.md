<h2>Introducción</h2>

Admetricks captura campañas publicitarias de los principales medios de cada país, procesa esta información identificando quién y cuánto realiza la campaña, realiza filtros relevantes y entrega reportes de inteligencia para sus clientes que acceden a ellos a través de una plataforma web. El trabajo se enfocará en esta última parte, la plataforma que entrega los reportes. 

Esta plataforma utiliza las siguientes tecnologías. Primero la información se encuentra en tablas resúmenes en una base de datos mysql. Luego información es obtenida por una aplicación “backend” escrita en python usando el framework flask que expone una API REST JSON. Finalmente el cliente interactúa con una capa “frontend” de widgets Javascript creados a partir de angularJS.

<h2>Primera parte: portafolio</h2>

Describe el objetivo y el funcionamiento de una aplicación con arquitectura similar que hayas creado. Particularmente que exponga una API REST JSON consumida por una aplicación de una página Javascript. Adjunta screenshots y pedazos de código (o pseudocódigo) relevantes y que muestren soluciones elegantes a sub-problemas.

<h2>Segunda parte: prototipo</h2>

Dada la base de datos mysql adjunta, construye un prototipo funcional que implemente una aplicación con una serie de widgets

Cada widget es un elemento independiente que mediante javascript obtiene su información de una API REST JSON implementada en el framework Django. Para implementar los widgets puedes utilizar javascript y el framework Angular o otro equivalente que te acomode. Para HTML y CSS puede ser bootstrap o otro equivalente de tu gusto.

Implementa los siguientes APIs + widgets:

<h3>1) Campaña</h3>

Este widget contiene un cuadro con el banner, el nombre de la campaña, la lista de medios en que aparece, la suma de su impacto y la fecha de inicio y término.

<h3>2) Lista de campañas</h3>

Este widget contiene todas las campañas de la base de datos.

<h3>3) Gráfico de impacto</h3>

Este widget gráfica el impacto diario de cada campaña. Puedes usar hightcharts o equivalente.

<h3>4) Fecha</h3>

Este widget permite filtrar la lista de campañas por rango de fecha. Puedes usar cualquier javascript pre hecho

<h3>5) Anunciante</h3>

Este widget carga una lista con los anunciantes con actividad en esa fecha y en los medios seleccionados. Permite elegir uno de estos anunciantes y así filtrar la lista de campañas.

<h3>6) Medio</h3>

Este widget carga una lista con los medios con actividad en la fecha seleccionada y anunciantes seleccionados.

<h3>7) Extra</h3>

Ya entiendes la idea, ahora opcionalmente implementa cualquier cosa que se te ocurra.

<h2>Entrega</h2>

Tienes 3 días para desarrollar, comitea lo más seguido posible para ver tu avance.

<h2> Evaluación</h2>

Los criterios de evaluación (de 1 a 10) serán los siguientes:

- Acabado general, como se ve y funciona desde el cliente
- Backend: funcionalidad, calidad y buenas prácticas
- Frontend: funcionalidad, calidad y buenas prácticas
- Orden y lectura del código en general
