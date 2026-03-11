import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;

@WebServlet("/AuctionServlet")
public class AuctionServlet extends HttpServlet {
    private static final String DB_URL = "jdbc:mysql://localhost:3306/auction_inv?useSSL=false&serverTimezone=UTC";
    private static final String DB_USER = "root";
    private static final String DB_PASSWORD = "";

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String itemId = request.getParameter("itemId");
        String bidderName = request.getParameter("bidderName");
        double bidAmount = Double.parseDouble(request.getParameter("bidAmount"));

        try {
            // Load MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
                String checkQuery = "SELECT highest_bid, starting_price FROM AuctionItems WHERE item_id = ?";
                PreparedStatement checkStmt = conn.prepareStatement(checkQuery);
                checkStmt.setInt(1, Integer.parseInt(itemId));
                ResultSet rs = checkStmt.executeQuery();

                if (rs.next()) {
                    double highestBid = rs.getDouble("highest_bid");
                    double startingPrice = rs.getDouble("starting_price");

                    if (bidAmount > highestBid && bidAmount >= startingPrice) {
                        String updateQuery = "UPDATE AuctionItems SET highest_bid = ?, bidder_name = ? WHERE item_id = ?";
                        PreparedStatement updateStmt = conn.prepareStatement(updateQuery);
                        updateStmt.setDouble(1, bidAmount);
                        updateStmt.setString(2, bidderName);
                        updateStmt.setInt(3, Integer.parseInt(itemId));
                        updateStmt.executeUpdate();

                        out.println("<h1>Bid placed successfully!</h1>");
                    } else {
                        out.println("<h1>Your bid must be higher than the current highest bid and starting price!</h1>");
                    }
                } else {
                    out.println("<h1>Item not found!</h1>");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
            out.println("<h1>Error: " + e.getMessage() + "</h1>");
        }
    }
}