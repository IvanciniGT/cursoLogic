<%
    try{
        Thread.sleep(1000);
        String busqueda=request.getParameter("busqueda");
    }catch(Exception e){}
%>

<html>
<body>
<h2>Resultados: <%=busqueda%></h2>
</body>
</html>
