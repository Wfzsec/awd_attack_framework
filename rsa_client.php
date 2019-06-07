<?php
class Rsa {
private static $PRIVATE_KEY = '-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCrFxyAYGqDE9OR3CNPEjGpQDAcIcsc9ZG/2HPgzHsME8n45x1y
P75Ki0MIYj4uhoygoYlnZPk3gKj60GdM8oD7hvL6R24LZij0zixRz+mBU/xac+dJ
HIK/5xAMtnQeyWcu+QMSLArDln9Wxp7nmONA1Ry54iX4iJ1PVODtw/BZbQIDAQAB
AoGADC0A4kH6Uom+rMq12JK65gijY90jz1PKo5SL6puixiFCZmxMNC1FJZjzlE0p
j7YTm/rjBHCzK7gETpU2RMudUitgsXnwWD9BY2xfcJzukdDYCrgJCuqgGuZ+4D9J
sAWcWmGDpXXVnvROvJF6Yz4230DN754Af+B6vOsRsK+FhSECQQDZwv7iPnPcG9Pr
Ac8T+KMBex0XbEk4Lh4cRuQN224zkdVEkAsldWcWNBQuUeGXgseywz2xcO0GH238
zjc364gXAkEAySIabW3TR6f8kHTiqKo9pBO0y15LqAHGwQckXkfuibzCxM36pj/p
WVcRZy2WcFrnXjj3zXZecopRb9x/Jx9ZGwJBAJ/t+kwnGehZ97XtSiycuvrndGIz
gULle+/AkNUshy8Qt9T3BXipVOCVtwydzlT8E7ZSdgjPqwSIKLs2qI9FSFkCQEW3
8Ysu/4aeHzj/mzW11SoTvp6j7/urqfZtAFlB+9h4uta3Q4PvMXbLbHfkYHpPuFV7
z8HDnxd7BKGOv/CSuDMCQEAEJukly0GbEX8VZxFJ5/Ki3m2toGTD1CePObwW1DaS
dmNxKgsScUdcVw0WUVRL4KV4C2XLib6M9hjwqer0OQM=
-----END RSA PRIVATE KEY-----';

private static function getPrivateKey()
{
$privKey = self::$PRIVATE_KEY;
return openssl_pkey_get_private($privKey);
}

public static function privEncrypt($data = '')
{
if (!is_string($data)) {
return null;
}
return openssl_private_encrypt($data,$encrypted,self::getPrivateKey()) ? base64_encode($encrypted) : null;
}
}

$rsa = new Rsa();
$cmd = $_POST['cmd'];
$action = "enc";
if($action!==Null){
    if($action==="enc"){
        $privEncrypt = $rsa->privEncrypt($cmd);
        echo $privEncrypt;
    }
}



