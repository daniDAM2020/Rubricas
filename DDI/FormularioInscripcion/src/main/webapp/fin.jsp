<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c"  uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
		<head>
			<meta charset="ISO-8859-1">
			<title>Usuario introducido</title>
		</head>
		<body>
			<table>
				<tr>
					<th>Nombre</th>
					<th>Edad</th>
					<th>Curso</th>
					<th>Borrar usuario</th>
				</tr>
				<c:forEach items="${userList}" var="userList">
					<tr>
						<td>${userList.name}</td>
						<td>${userList.age}</td>
						<td>${userList.year}</td>
						<td>
							<form method="post" action="/DeleteUser">	
								<input type="hidden" name="userName" value="${userList.name}">
								<input type="submit" value="Borrar">
							</form>
						</td>
					</tr>
				</c:forEach>
			</table>
			<a href="index.jsp">Index</a>
		</body>
</html>