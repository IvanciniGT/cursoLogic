<html>
    <body>
        <h2>Programa de suma</h2>
        <%
        int numero1=Integer.parseInt(request.getParameter("a"));
        int numero2=Integer.parseInt(request.getParameter("b"));
        int suma=numero1+numero2;
        %>
        <p>El primer numero es: <%=numero1%></p>
        <p>El segundo numero es: <%=numero2%></p>        
        <p>La suma de ambos vale: <%=suma%></p>

    </body>
</html> 