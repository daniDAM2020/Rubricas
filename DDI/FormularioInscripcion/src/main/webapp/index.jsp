<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c"  uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Formulario</title>
</head>
<body>
<h2>FORMULARIO</h2>
	<form action="/InsertForm" method="post">
		<span>Nombre:</span> <input type="text" name="name">
		<br></br>
		<span>Fecha de nacimiento:</span> <input type="text" placeholder="yyyy-mm-dd" pattern="(?:19|20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31))" 
		name="birthdate">
		<br></br>
		<span>Curso:</span>
		<select name="year">
            <option value="first">Primero</option>
            <option value="second">Segundo</option>
    	</select>
    	<br></br>
		<input type="submit">
	</form>
</body>
</html>