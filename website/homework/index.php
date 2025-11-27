<HTML>
<HEAD>
<TITLE>Anth/Biol 5221: Human Evolutionary Genetics: Homework</TITLE>
</HEAD>
<style type="text/css">
body {font-family :Arial}
</style>
<BODY>

<?php
function datedlink($filename, $text) {
   echo "<a href=" . $filename . ">" . $text . "</a>";
   if (file_exists($filename)) {
       echo "&nbsp;&nbsp;<small>[";
       echo date ("d F Y H:i:s.", filemtime($filename));
       echo "]&nbsp;</small>";
   }
}
?>

<H1>Homework for Anth/Biol 5221 (Human Evolutionary Genetics)</H1>

<p>
<dl>
<dt> <?php datedlink("homework.pdf", "Homework problems");?></dt> 
</dl>
  
</BODY>
