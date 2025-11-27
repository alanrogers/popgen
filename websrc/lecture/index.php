<p><?php
function datedlink($filename, $text) {
   echo "<a href=" . $filename . ">" . $text . "</a>";
   if (file_exists($filename)) {
       echo "&nbsp;&nbsp;<small>[";
       echo date ("d F Y H:i:s.", filemtime($filename));
       echo "]&nbsp;</small>";
   }
}
?></p>

<h1>Biol 5221: Lectures and Reading Assignments</h1>

<p>In the list below, the numbers indicate lecture topics.  Click on one,
and you'll get the slides we showed in class.  Lectures are assigned on
dates listed in the <a href="../syllabus.pdf">syllabus</a>. More than one lecture
may be assigned on a given date. The dates in the list below tell you
when the lecture slides were added to this website.  Under each
lecture topic, the open circles indicate additional readings.  Some of
these are clickable too and take you to the reading itself, in pdf
format.  You'll need a pdf reader such as Adobe Acrobat Reader or
xpdf. If the reading is under copyright, you'll be asked for a
username and password.  If you didn't get this in class, then email
one of us.</p>

<p>For students who want to dip into the professional literature, there
are links labeled "optional".</p>

<ol>
<li><p><?php datedlink("prob-2x3.pdf", "Probability");?></p>

<ul>
<li><a href="http://content.csbs.utah.edu/~rogers/pubs/Rogers-JEP.pdf">Rogers. Just enough probability.</a></li>
</ul></li>
<li><p><?php datedlink("anova.pdf", "Partitioning variance");?></p></li>
<li><p><?php datedlink("variance_and_genomes.pdf", "Genomes and variation");?></p>

<ul>
<li><p><a href="../unprotected/vocab.pdf">Rogers. 2024.</a> The confusing vocabulary of
population genetics. </p></li>
<li><p>Gillespie sections 1.0-1.3</p></li>
</ul></li>
</ol>

<dl>
  <dt>Optional</dt>
   * [Pritchard] [Pritchard:OGH-24] sections 1.1-1.4

   * [Coop] [Coop:PQG-20] Chapter 1 and Chapter 2, through
     section 2.1.1

   * [1000 Genomes. 2010] [Mgenomes:N-467-1061] A map of human genome
                  variation from population-scale sequencing.

   * [1000 Genomes. 2012] [Mgenomes:N-491-56] An integrated map of genetic
     variation from 1,092 human genomes.

   * [1000 Genomes. 2015] [Mgenomes:N-526-68] A global reference for
   human genetic variation.

   * [Halldorsson et al. 2022] [Halldorsson:N-607-732] The sequences
   of 150,119 genomes in the UK Biobank.
  </dl>

<ol>
<li><p><?php datedlink("hardywei-2x3.pdf", "Random mating");?></p>

<ul>
<li>Gillespie section 1.4</li>
</ul></li>
<li><p><?php datedlink("hetzdecay-2x3.pdf", "Decay of heterozygosity");?></p>

<ul>
<li>Gillespie sections 1.4, 2.0-2.2</li>
</ul></li>
<li><p><?php datedlink("mutdrift-2x3.pdf", "Mutation versus drift");?></p>

<ul>
<li>Gillespie section 2.3</li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><p><a href="https://github.com/cooplab/popgen-notes/releases/tag/v1.1">Coop</a> sections 4-4.1.1</p></li>
<li><p><a href="https://web.stanford.edu/group/pritchardlab/HGbook.html">Pritchard</a> sections 1.5, 2.1
</dl></p></li>
</ul></li>
<li><p><?php datedlink("seqvar-2x3.pdf", "Describing DNA sequence variation");?></p>

<ul>
<li><a href="../ggeneal.pdf">Rogers. Lecture notes on gene genealogies.</a> Ch. 1.</li>
</ul></li>
<li><p><?php datedlink("ggeneal-2x3.pdf", "Gene genealogies");?></p>

<ul>
<li><p><a href="../ggeneal.pdf">Rogers. Lecture notes on gene genealogies.</a> Chs. 4-5.</p></li>
<li><p>Gillespie section 2.6</p></li>
</ul></li>
<li><p><?php datedlink("python.pdf", "Python");?></p></li>
<li><p><?php datedlink("spectrum-2x3.pdf", "Site frequency spectrum");?></p>

<ul>
<li><a href="../ggeneal.pdf">Rogers. Lecture notes on gene genealogies.</a> Ch. 6.</li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><a href="https://arxiv.org/abs/2103.00335">Rogers and Wooding. 2021</a> Expectation of the
site frequency spectrum.
</dl></li>
</ul></li>
<li><p><?php datedlink("mismatch-2x3.pdf",
"Mismatch distribution and population growth");?></p>

<ul>
<li><a href="../ggeneal.pdf">Rogers. Lecture notes on gene genealogies.</a> Ch. 7.</li>
</ul></li>
<li><p><?php datedlink("popgrow-2x3.pdf", "Population growth");?></p></li>
<li><p><?php datedlink("neutral_theory.pdf",
"The neutral theory of molecular evolution");?></p>

<ul>
<li>Gillespie section 2.4-2.5</li>
</ul></li>
<li><p><?php datedlink("selection.pdf", "Selection");?></p>

<ul>
<li><p>Gillespie sections 3.0-3.3</p></li>
<li><p><a href="../unprotected/Rogers-seln.pdf">Not quite enough selection</a> Not
quite enough selection (or perhaps a bit too much).</p></li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><a href="https://web.stanford.edu/group/pritchardlab/HGbook.html">Pritchard</a> sections 2.5-2.7
</dl></li>
</ul></li>
<li><p><?php datedlink("mut_sel.pdf",
"When bad things happen to good genes: mutation vs selection");?></p>

<ul>
<li><p>Gillespie section 3.4</p></li>
<li><p><a href="../protected/Fu-N-493-216.pdf">Fu 2013</a></p></li>
</ul></li>
<li><p><?php datedlink("load.pdf", "Genetic load");?></p>

<ul>
<li>Gillespie section 3.5</li>
</ul></li>
<li><p><?php datedlink("adaptfix.pdf", "Fixation of mutations");?></p>

<ul>
<li><p>Gillespie sections 3.9-3.10</p></li>
<li><p><a href="islands.html">Islands simulation</a></p></li>
</ul></li>
<li><p><?php datedlink("ld-2x3.pdf", "Neutral evolution at two loci");?></p>

<ul>
<li>Gillespie sections 4.0-4.1</li>
</ul></li>
<li><p><?php datedlink("twolocseln-2x3.pdf", "Selection two loci");?></p>

<ul>
<li>Gillespie section 4.2</li>
</ul></li>
<li><p><?php datedlink("ldseln-2x3.pdf", "Why LD helps us find selective
 sweeps");?></p>

<ul>
<li><a href="../unprotected/ldseln.pdf">Rogers. 2018</a> Why LD hels us find selective sweeps.</li>
</ul></li>
<li><p><?php datedlink("inbreed-2x3.pdf", "Inbreeding");?></p>

<ul>
<li>Gillespie, sections 5.0-5.2</li>
</ul></li>
<li><p><?php datedlink("inbreed2-2x3.pdf", "Inbreeding, drift, and
fitness");?></p>

<ul>
<li>Gillespie, section 5.3</li>
</ul></li>
<li><p><?php datedlink("popstruc-2x3.pdf", "Population structure");?></p>

<ul>
<li><p>Gillespie, section 5.5.</p></li>
<li><p><a href="../unprotected/popstruc.pdf">Rogers, 2020.</a> Geographic population
structure.</p></li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><a href="https://web.stanford.edu/group/pritchardlab/HGbook.html">Pritchard</a> section 2.4
</dl></li>
</ul></li>
<li><p><?php datedlink("popstruc-hancock.pdf", "Population structure part 2");?></p></li>
<li><p><?php datedlink("detectseln.pdf",
"Detecting natural selection with genomic data");?></p>

<ul>
<li><p><a href="../protected/Vitti-ARG-47-1.pdf">Vitti et al</a></p></li>
<li><p><a href="../protected/Hejase-TG-36-243.pdf">Hejase et al 2020</a> Summary statistics to gene
trees: methods for inferring positive selection.</p></li>
</ul></li>
<li><p><?php datedlink("gdraft.pdf", "Genetic draft");?></p>

<ul>
<li>Gillespie section 4.3.</li>
</ul></li>
<li><p><?php datedlink("pophist-2x3.pdf", "Population history from whole
 genomes");?></p>

<ul>
<li><a href="../protected/Li-N-475-493">Li and Durbin</a></li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><a href="https://doi.org/10.1101/2023.07.28.551046">Rogers 2024</a>
</dl></li>
</ul></li>
<li><p><?php datedlink("speda-2x3.pdf", "Archaic genes in modern humans");?></p>

<ul>
<li><a href="https://arxiv.org/abs/2201.02668">Rogers. 2022.</a> Using genetic data to build
intuition about population history. </li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><p><a href="../protected/Mendez-MBE-29-1513.pdf">Mendez et al, 2012</a> Global
Genetic Variation at OAS1 Provides Evidence of Archaic Admixture
in Melanesian Populations.</p></li>
<li><p><a href="../protected/Vernot-Science-343-1017.pdf">Vernot and Akey, 2014</a>
Resurrecting surviving Neandertal lineages from modern human
genomes.</p></li>
<li><p><a href="../protected/Castellano-PNA-111-6666.pdf">Castellano et al, 2014</a>
</dl></p></li>
</ul></li>
<li><p><?php datedlink("QTs1a.pdf",
"QTs 1: genes and environment");?></p>

<ul>
<li>Gillespie, sections 6.0-6.1</li>
</ul></li>
<li><p><?php datedlink("QTs2a.pdf",
"QTs 2: heritability");?></p>

<ul>
<li>Gillespie, sections 6.0-6.1</li>
</ul></li>
<li><p><?php datedlink("QTs3a.pdf", "QTs 3: response to selection");?></p>

<ul>
<li><p>Gillespie, section 6.2</p></li>
<li><p><a href="../unprotected/Rogers-lande.pdf">Response to selection on quantitative traits</a></p></li>
</ul></li>
<li><p><?php datedlink("trait_mapping.pdf", "Trait mapping");?></p>

<ul>
<li><p><a href="../protected/Tam-NRG-20-467.pdf">Tam et al. 2019</a> Benefits and limitations of
genome-wide association studies.</p></li>
<li><p><a href="../protected/Uffelmann-NRM-1-59.pdf">Uffelmann et al 2021</a> Genome-wide
association studies.</p></li>
</ul></li>
<li><p><?php datedlink("missing_heritability.pdf",
"Missing heritability: trait prediction and prospects for personalized
medicine");?></p>

<ul>
<li><p><a href="../protected/Manolio-N-461-747.pdf">Manolio et al. 2009</a> Finding the missing
heritability of complex diseases</p></li>
<li><p><a href="https://www.genome.gov/Health/Genomics-and-Medicine/Polygenic-risk-scores">Polygenic risk scores</a></p></li>
<li><p><a href="https://www.nature.com/articles/d41586-023-01490-3.pdf">Massarat et al. 2023</a> Human pangenome
supports analysis of complex genomic regions </p></li>
</ul>

<p><dl>
<dt>Optional</dt></p>

<ul>
<li><p><a href="../protected/Liao-N-617-312.pdf">Liao et al 2023</a> A draft human pangenome reference.</p></li>
<li><p><a href="../protected/Povysil-NRG-20-747.pdf">Povysil et al. 2019</a> Rare-variant collapsing
analyses for complex traits: guidelines and applications. </p></li>
<li><p><a href="../protected/Choi-NP-15-2759.pdf">Choi et al. 2020</a> Tutorial: a guide to performing
polygenic risk score analyses. 
</dl></p></li>
</ul></li>
<li><p><?php datedlink("gwas.pdf", "Genome-Wide Association Studies (GWAS)");?></p></li>
<li><p><?php datedlink("QTevol.pdf", "Evolution of quantitative
traits");?></p>

<ul>
<li><a href="../protected/Barghi-NRG-21-769.pdf">Barghi et al. 2020</a> Polygenic adaptation: a
unifying framework to understand positive selection.</li>
</ul></li>
</ol>
