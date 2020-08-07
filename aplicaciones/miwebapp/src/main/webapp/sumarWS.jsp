 <%
        int numero1=Integer.parseInt(request.getParameter("a"));
        int numero2=Integer.parseInt(request.getParameter("b"));
        int suma=numero1+numero2;
        %>
{
    'numero1': <%=numero1%>,
    'numero2': <%=numero2%>,
    'suma': <%=suma%>
}