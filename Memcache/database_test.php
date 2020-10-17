<?php
 
$mem = new Memcached();
 
$mem->addServer('localhost', 11211);
$servername = "localhost";
$database = "memcached_test";
$username = "apeksha";
$password = "mytesting123";

$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection

if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

$query = 'SELECT name FROM sample_data WHERE id = 101';

$key = md5($query);


$result = $mem->get($key);

if ($result) {
 
print '<p>Data was: ' . $result[0] . '</p>';
 
print '<p>Caching success!</p><p>Retrieved data from memcached!</p>';

}else {

$result = mysqli_fetch_array(mysqli_query($conn, $query)) or die(mysql_error());
 
$mem->set($key, $result, 5);

print '<p>Data was: ' . $result[0] . '</p>';
 
print '<p>Data not found in memcached.</p><p>Data retrieved from MySQL and stored in memcached for next time.</p>';
 
}
 
?>
