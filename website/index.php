<HTML>
<HEAD>
<TITLE>Biol 5221: Human Evolutionary Genetics</TITLE>
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

<H1>Biol 5221: Human Evolutionary Genetics</H1>

<p>
<dl>

  <dt> <?php datedlink("syllabus.pdf", "Lecture syllabus");?></dt>

  <dt> <?php datedlink("lab/labsyl.pdf", "Lab syllabus");?></dt>

  <dt> <?php datedlink("quizsyl.pdf", "Quiz schedule");?></dt>

  <dt> <a href="welcome_essay.pdf">Welcome essay</a></dt>

<dt> <a href="lecture/index.php">Lectures</a></dt> 

<dt> <a href="readings.php">Readings</a></dt> 

<dt> <a href="lab/index.php">Lab</a></dt> 

<dt> <a href="homework/index.php">Homework</a></dt>

<dt> <a href="studyguide.pdf">Study guide</a></dt>

<dt><a href="grading.php">Grading</a></dt>

<dt><a href="submitting.pdf">Submitting handwritten assignments to Canvas</a></dt>

<dt><a href="algebraxcred.html">Extra credit algebra
    assignment</a></dt>
</dl>


</BODY>
