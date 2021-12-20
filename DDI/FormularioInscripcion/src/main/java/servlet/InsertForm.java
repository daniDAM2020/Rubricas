package servlet;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Entities.users;

public class InsertForm extends HttpServlet {
	private String jdbcUrl = "jdbc:h2:file:./src/main/resources/test;MODE=MYSQL";

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String name = req.getParameter("name");
		String year = req.getParameter("year");
		String birthdate = req.getParameter("birthdate");

		Connection conn;
		try {
			Class.forName("org.h2.Driver");
			conn = DriverManager.getConnection(jdbcUrl, "sa", "");
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
		PreparedStatement preparedStatement = null;
		try {
			preparedStatement = conn.prepareStatement("set mode MySQL; create table IF NOT EXISTS FORM(\r\n"
					+ "name varchar(25) PRIMARY KEY,\r\n" + "birthdate date,\r\n" + "year varchar(25)\r\n" + ");");
			preparedStatement.executeUpdate();
			preparedStatement.close();
			preparedStatement = conn
					.prepareStatement("set mode MySQL; INSERT INTO FORM (name, birthdate, year) VALUES (?,?,?)"
							+ "ON DUPLICATE KEY UPDATE\r\n" + "form.birthdate=?, form.year=?");
			preparedStatement.setString(1, name);
			preparedStatement.setString(2, birthdate);
			preparedStatement.setString(3, year);
			preparedStatement.setString(4, birthdate);
			preparedStatement.setString(5, year);
			preparedStatement.executeUpdate();
			preparedStatement.close();
			preparedStatement = conn.prepareStatement(
					"SELECT name, DATEDIFF(year, ?, NOW()), year FROM form WHERE " + "form.name LIKE CONCAT( '%',?,'%')"
							+ "AND form.birthdate LIKE CONCAT( '%',?,'%') " + "AND form.year LIKE CONCAT( '%',?,'%')");
			preparedStatement.setString(1, birthdate);
			preparedStatement.setString(2, name);
			preparedStatement.setString(3, birthdate);
			preparedStatement.setString(4, year);
			preparedStatement.executeQuery();
			ResultSet resultSet = preparedStatement.executeQuery();
			ArrayList<users> userList = new ArrayList<users>();
			while (resultSet.next()) {
				users user = new users();
				String userName = resultSet.getString(1);
				user.setName(userName);
				Integer userBirthdate = resultSet.getInt(2);
				user.setAge(userBirthdate);
				String userYear = resultSet.getString(3);
				user.setYear(userYear);
				userList.add(user);
			}
			req.setAttribute("userList", userList);
			preparedStatement.close();
			conn.close();

			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			if (null != conn) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
					throw new RuntimeException(e);
				}
			}
			if (preparedStatement != null) {
				try {
					preparedStatement.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}

		RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/fin.jsp");
		dispatcher.forward(req, resp);
	}

}