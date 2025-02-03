AllUsers = "SELECT Username, Firstname, Lastname FROM User"
SingleUser = "SELECT CONCAT(Firstname,' ',Lastname) AS Name FROM User WHERE Username = %s"
GameDetailSingle = "SELECT G.WordPerMinute, G.Accuracy, G.Level, G.LivesLeft FROM User U INNER JOIN Game G ON U.Id = G.User_Id WHERE U.Username = %s"
AllScores = "SELECT CONCAT(U.Firstname, ' ', U.Lastname) AS Name, G.WordPerMinute, G.Accuracy, G.Level, G.LivesLeft FROM User U INNER JOIN Game G ON U.Id = G.User_Id ORDER BY G.Level DESC"