<?php
system("kill `ps -aux | grep www-data | grep apache2 | awk '{print $2}'`");
?>
