<HTML>
<HEAD>
<TITLE>Biol 5221: Human Evolutionary Genetics Lab</TITLE>
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

<H1>Biol 5221: Human Evolutionary Genetics Lab</H1>

<h2>Text</h2>
<dl>
<dt><?php datedlink("labsyl.pdf", "Lab syllabus");?></dt>
<dt> <?php datedlink("../jepy.pdf", "<em>Just Enough
		Python</em>");?></dt> 
<dt><?php datedlink("manual.pdf", "Lab manual");?></dt>
<dt><?php datedlink("lab-examp.pdf", "Example lab report");?></dt>
</dl>


<h2>Data</h2>
<p>
  <ul>
	<li> <a href="ftp://ftp.ncbi.nlm.nih.gov/hapmap/genotypes/2008-10_phaseII/fwd_strand/non-redundant">
		HapMap ftp site</a></li>
<li> <a href="CEU_7q31.dat">Encode SNPs from region 7q31 of human
chromosome 7</a></li>
<li> <a href="CEU_7q31_short.dat">Short version preceding file,
containing just four SNPs.</a> (For debugging.)</li>
<li> <a
href="genotypes_chr99_CEU_r23a_nr.b36_fwd.txt">genotypes_chr99_CEU_r23a_nr.b36_fwd.txt</a>
Shortened version the HapMap file for chromosome 2, population
CEU. (For debugging.)</li>  
</ul>
</p>

<h2>Matplotlib Tutorial and Code</h2>
<p>Matplotlib is a Python package for graphics. It isn't required for
  this course, but you are welcome to use it. The graphics it makes
  are much better than the character-based graphics provided by
  pgen.py. The links below contain documentation and sample code. They
  were provided by Todd Islam.</p>
<ul>
<li> <a href="using_matplotlib.pdf">Documentation</a></li>
<li> <a href="using_matplotlib.py">Code</a></li>
</ul>

<h2>Computer Programs</h2>
<p>
<ul>
<li> <A HREF="pgen.py">pgen.py</a>, a Python module that includes
  classes for accessing and manipulating HapMap data.
<li> <A HREF="wolfinc.py">Wolf_2_incomplete.py</A> Simulate Wolf's dice.</li>
<li> <A HREF="drift.py">drift.py</A> Forward time simulation of drift.</li>
<li> <A HREF="coal_depth.py">coal_depth.py</A> Coalescent simulation
of genetic drift.</li>
<li> <A HREF="cointest.py">cointest.py</A> Use simulation to test a
hypothesis.</li>
<li> <A HREF="coin_ci.py">coin_ci.py</A> Use simulation to generate a
confidence interval.</li>
<li> <A HREF="twolocinc.py">twolocinc.py</A> Simulate
selection, drift, and recombination at two loci.  This version is
incomplete; it will be completed as part of a lab project.</li>
<li> <a href="haphetinc.py">haphetinc.py</a> Calculate observed
and expected heterozygosity from a sample of HapMap SNPs.</li>
<li> <a href="hapspecinc.py">hapspecinc.py</a> Calculate the
site frequency spectrum from HapMap data</li>
<li> <a href="var.py">var.py</a> Calculate variances</li>
<li> <A HREF="snptabinc.py">snptabinc.py</A> Tabulate
 data from a pair of adjacent HapMap SNPs, and use these data to
 estimate linkage disequilibrium.</li>
<li> <A HREF="rscaninc.py">rscaninc.py</A> Scan HapMap for LD</li>
<li> <A HREF="lactaseinc.py">lactaseinc.py</A> Compare LD around
  lactase gene with that in rest of chromosome 2.</li>
</ul>

</BODY>

