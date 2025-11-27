<html>
<head>
<title>Biol 5221: Readings</TITLE>
</head>
<style type="text/css">
body {font-family :Arial}
</style>
<body>

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

<h1>Main texts</h1>
<ul>
<li>Gillespie, John. 2004. <em>Population Genetics: A Concise
    Guide</em>, 2nd edn. (bookstore)</li>
<dd>Chapter 2 is available
  <?php datedlink("protected/Gillespie-ch2.pdf", "here");?>
</dd>  

<li> Rogers, Alan R. <?php datedlink("ggeneal.pdf", "<em>Lecture Notes on Gene
Genealogies</em>");?></li>

<li> Rogers, Alan
  R. <a href="http://content.csbs.utah.edu/~rogers/pubs/Rogers-JEP.pdf">
		   <em>Just Enough Probability</em></a></li>

<li> Seger, Jon. <?php datedlink("jepy.pdf", "<em>Just Enough
		Python</em>");?></li>
<li><a href="https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python">Using
    Python's f stings</a></li>
</ul>
Additional readings, both required and optional, are listed for each
lecture
on <a href="https://content.csbs.utah.edu/~rogers/tch/ant5221/lecture/index.php">this page</a>.

<h1>Optional readings</h1>
<ul>
<li>Coop, Graham. <a
href="https://github.com/cooplab/popgen-notes/releases/tag/v1.1">
    <em>Population and Quantitative Genetics</em></a>.
</li>  

<li>Felsenstein, Joe. <a
href="https://felsenst.github.io/pgbook/pgbook.html">
<em>Theoretical Evolutionary Genetics</em></a>.
An excellent text, but more advanced than the one we use for this
  course.
</li>

<li>Pritchard, Jonathan. <a
href="https://web.stanford.edu/group/pritchardlab/HGbook.html">
<em>An Owner's Guide to the Human Genome:
An Introduction to Human Population Genetics, Variation and Disease</em></a>.
</li>    

<li>Alternate treatment of the decay of heterozygosity:
<a href="protected/CrowKimura-hetzdecay.pdf">Crow and Kimura</a></li>

<li>Alternate treatments of linkage
disequilibrium: <a href="protected/CrowKimura-LD.pdf">Crow and
Kimura</a>, or the section titled "Linkage" in Felsenstein's book
(linked above)</li>
</ul>

</body>
</html>
