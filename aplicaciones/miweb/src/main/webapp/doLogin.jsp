<%
    try{
        Thread.sleep(600);
        String usuario=request.getParameter("usuario");
        String password=request.getParameter("password");
    }catch(Exception e){}
%>

<html>
<body>
<h2>Bienvenido: <%=usuario%></h2>
</body>
</html>
