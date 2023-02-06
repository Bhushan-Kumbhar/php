<?php

if ($_SERVER['REQUEST_METHOD'] == "POST") {

    $number = $_POST["number"];

    for ($i = 1; $i <= $number; $i++) {
        for ($j = 1; $j <= $i; $j++) {
            echo "$i";
        }
        echo "\n";
    }
}

?>