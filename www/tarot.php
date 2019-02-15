<?php

	$cardname = $_REQUEST["cardpick"];

	$dbconn = pg_connect("host=localhost dbname=Tarot user=postgres password=dbpass");
	$desc_query = pg_query($dbconn, "SELECT * FROM descriptions WHERE card_id = '$cardname';");
	$name_query = pg_query($dbconn, "SELECT * FROM card_info WHERE card_id = '$cardname';");
	if (!$desc_query || !$name_query) {
		echo "An error occured.\n";
		exit;
	}

	$name = pg_fetch_result($name_query, 0,'name');
	$desc = pg_fetch_result($desc_query, 0,'desc_text');
		echo $name, "<br><br>", $desc
?>
