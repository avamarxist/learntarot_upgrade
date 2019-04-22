<?php

	$cardname = $_REQUEST["cardpick"];


	$dbconn = pg_connect("host=b4h4r.online port=5432 dbname=Tarot user=postgres password=dbpass");

	$act_query = pg_query($dbconn, "SELECT * FROM actions WHERE root_card = '$cardname';");
	
	$desc_query = pg_query($dbconn, "SELECT * FROM descriptions WHERE card_id = '$cardname';");
	$name_query = pg_query($dbconn, "SELECT * FROM card_info WHERE card_id = '$cardname';");
	if (!$desc_query || !$name_query || !$act_query) {
		echo "An error occured.\n";
		exit;
	}

	$name = pg_fetch_result($name_query, 0,'name');
	$actions = pg_fetch_all($act_query);
	$desc = pg_fetch_result($desc_query, 0,'desc_text');
	
	echo $name."<br><br>";
	echo "hello<br>";
	foreach($actions as $act){
		echo $act["act_text"]."<br><br>";
	}
	echo $desc;
?>
