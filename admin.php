<?php

//Initalization 
$host = 'localhost';
$username = 'admin';
$password = 'zebraa';
$dbname = 'icc';


// Get the Active Orders and Bearers

$conn = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
$a_orders = $conn->query("SELECT * FROM `order` where orderStatus = 'Active'");
$a_result = $a_orders->fetchAll(PDO::FETCH_ASSOC);

$a2_orders = $conn->query("SELECT * FROM `bearer` where assignedOrders != ''");
$a2_result = $a2_orders->fetchAll(PDO::FETCH_ASSOC);

?>

<!--

Table Heading That lists the Active Orders 
Expands on the Active Orders and Active Bearers
!-->

<table>
<tr>
    <th>orderID</th>

</tr>

<?php foreach ($a_result as $row): ?>
<tr>
      <td><?= $row['orderID'];?><button class = "collapsible">+</button></td>
        <tr class = "content">
        <th> orderID </th>
        <td><?= $row['orderID'];?>
        <th> assignedCustomer </th>
        <td><?= $row['assignedCustomer'];?>
        <th> assignedBearer </th>
        <td><?= $row['assignedBearer'];?>
        <th> subtotal </th>
        <td><?= $row['subtotal'];?>
        <th> orderStatus </th>
        <td><?= $row['orderStatus'];?>
        
        <tr>

  </tr>
<?php endforeach; ?>
</table>

<table>
<tr>
    <th>Name</th>

</tr>
<?php foreach ($a2_result as $row): ?>
<tr>
      <td><?= $row['name'];?><button class = "collapsible">+</button></td>
      <tr class = "content">
        <th> assignedCustomer </th>
        <td><?= $row['ID'];?>
        <th> assignedBearer </th>
        <td><?= $row['assignedOrders'];?>
        <th> subtotal </th>
        <td><?= $row['location'];?>

  </tr>
<?php endforeach; ?>
</table>


<?php 

// Used to add a bearer to the database 

if (isset($_POST['set-bearer'])){

    $name = $_POST['bearer-input'];

    $pdoQuery = "INSERT INTO bearer(`name`) VALUES (:name)";

    $pdoQuery_run = $conn->prepare($pdoQuery);
    
    $pdoQuery_exec = $pdoQuery_run->execute(array(":name"=>$name));



}

// Used to delete a bearer from the database

if (isset($_POST['delete-bearer'])){

    $name = $_POST['bearer-input'];

    $pdoQuery = ("DELETE FROM bearer WHERE name=:name");

    $pdoQuery_run = $conn->prepare($pdoQuery);
    
    $pdoQuery_exec = $pdoQuery_run->execute(array(":name"=>$name));



}


?>

<?php

// Under is the html part with basic outline of how code should look cleanup needed


?>

<html>
<head>
    <meta charset="UTF-8">
    <title>JAK Cohert</title>
    <link rel="stylesheet" href="styles\admin.css">
    <script src="app.js" type="text/javascript"></script>
</head>
<body>
    <!-- STAFF & OWNER PAGE -->
    <header>
        <h1>Admin Page</h1>
    </header>

    <main>
        <!--This section displays current data-->
        <section class="admin-overview">
            <!-- This div will display the current orders not yet delivered
            Each order can be expanded to show more info
            Once a customer's order is delivered it should be removed-->
            <div class="current-orders">
                <h3>Active Orders</h3>
                <ul>
                    <!--Example Expanded Info-->
                    <li>Example Order <button>-</button> 
                        <div>
                            <table>
                                <tr>
                                    <td>Test Info</td>
                                    <td>Test Content</td>
                                </tr>
                                <tr>
                                    <td>Test Info</td>
                                    <td>Test Content</td>
                                </tr>
                            </table>
                        </div>
                    </li>
                    <li>Example Order <button>+</button></li>
                    <li>Example Order <button>+</button></li>
                </ul>
            </div>
            <div class="current-bearers">
                <h3>Active Bearers</h3>
                <ul>
                    <li>Example Bearer <button>+</button></li>
                    <li>Example Bearer <button>+</button></li>
                </ul>
            </div>
        </section>

        <section class="admin-tools">
            <div class="checkin-bearer">
            <form method="post">
                
                <input id="bearer-input" type="text" name="bearer-input" placeholder="Enter Bearer name" />
				<div id="controls">
					<button name="set-bearer" type = "submit">Set Bearer</button>
                    <button name ="delete-bearer" type = "submit">Delete Bearer</button>
				</div>
            </div>
        </section>

        <section class="admin-log">
            <div class="log-result">
                <ul>
                    <li>Log example</li>
                    <li>Log example</li>
                    <li>Log example</li>
                    <li>Log example</li>
                    <li>Log example</li>
                    <li>Log example</li>
                </ul>
            </div>
        </section>

    </main>

    <footer>

    </footer>
</body>

</html>