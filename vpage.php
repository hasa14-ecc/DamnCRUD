<?php
include "functions.php";
session_start();
if (!isset($_SESSION['user'])) {
    header("location: login.php");
} else {
?>

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <?= style_script() ?>

        <title>Profil</title>
    </head>

    <body>
        <div class="container">
            <h2>Dummy Page XSS Detect</h2>
            <div class="row">
                <div class="col">
                    <a type="button" class="btn btn-primary" href="index.php">Dashboard</a>
                    <div class="action float-right">
                        <a type="button" class="btn btn-danger" href="logout.php">Sign out</a>
                    </div>
                </div>
            </div>
            <br><br>
            <div class="row">
                <div class="col-md-12 order-md-1">
                    <form class="needs-validation" novalidate="">

                        <form method="GET" action="" name="form">
                            <p>Type everything:<input type="text" name="thing"></p>
                            <input type="submit" name="submit" value="Submit">
                        </form>
                </div>
                <?php
                if (isset($_GET["thing"]))
                    echo ("Your thing is " . $_GET["thing"]) ?>

            </div>

            </form>
        </div>
        </div>
        </div>

        <div class="text-center">
        <p class="mt-5 mb-3 text-muted">Your Damn Exercise &copy; 2023</p>
        </div>
    </body>

    </html>



<?php

}
?>