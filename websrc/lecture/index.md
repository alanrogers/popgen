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

# Biol 5221: Lectures and Reading Assignments

In the list below, the numbers indicate lecture topics.  Click on one,
and you'll get the slides we showed in class.  Lectures are assigned on
dates listed in the [syllabus](../syllabus.pdf). More than one lecture
may be assigned on a given date. The dates in the list below tell you
when the lecture slides were added to this website.  Under each
lecture topic, the open circles indicate additional readings.  Some of
these are clickable too and take you to the reading itself, in pdf
format.  You'll need a pdf reader such as Adobe Acrobat Reader or
xpdf. If the reading is under copyright, you'll be asked for a
username and password.  If you didn't get this in class, then email
one of us.

For students who want to dip into the professional literature, there
are links labeled "optional".

1. <?php datedlink("prob-2x3.pdf", "Probability");?>

  * [Rogers. Just enough probability.] [rogers:JEPr]

1. <?php datedlink("anova.pdf", "Partitioning variance");?>

1. <?php datedlink("variance_and_genomes.pdf", "Genomes and variation");?>

   * [Rogers. 2024.] [rogers:vocab] The confusing vocabulary of
      population genetics. 

   * Gillespie sections 1.0-1.3

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

1. <?php datedlink("hardywei-2x3.pdf", "Random mating");?>

   * Gillespie section 1.4

1. <?php datedlink("hetzdecay-2x3.pdf", "Decay of heterozygosity");?>

  * Gillespie sections 1.4, 2.0-2.2

1. <?php datedlink("mutdrift-2x3.pdf", "Mutation versus drift");?>

  * Gillespie section 2.3

  <dl>
  <dt>Optional</dt>
  * [Coop] [Coop:PQG-20] sections 4-4.1.1

  * [Pritchard] [Pritchard:OGH-24] sections 1.5, 2.1
  </dl>

1. <?php datedlink("seqvar-2x3.pdf", "Describing DNA sequence variation");?>

   * [Rogers. Lecture notes on gene genealogies.] [rogers:LNGG] Ch. 1.

1. <?php datedlink("ggeneal-2x3.pdf", "Gene genealogies");?>

   * [Rogers. Lecture notes on gene genealogies.] [rogers:LNGG] Chs. 4-5.

   * Gillespie section 2.6

1. <?php datedlink("python.pdf", "Python");?>

1. <?php datedlink("spectrum-2x3.pdf", "Site frequency spectrum");?>

  * [Rogers. Lecture notes on gene genealogies.] [rogers:LNGG] Ch. 6.

  <dl>
  <dt>Optional</dt>
  * [Rogers and Wooding. 2021] [rogers:spectrum] Expectation of the
  site frequency spectrum.
  </dl>

1. <?php datedlink("mismatch-2x3.pdf",
"Mismatch distribution and population growth");?>

   * [Rogers. Lecture notes on gene genealogies.] [rogers:LNGG] Ch. 7.

1. <?php datedlink("popgrow-2x3.pdf", "Population growth");?>

1. <?php datedlink("neutral_theory.pdf",
"The neutral theory of molecular evolution");?>

   * Gillespie section 2.4-2.5

1. <?php datedlink("selection.pdf", "Selection");?>

   * Gillespie sections 3.0-3.3

   * [Not quite enough selection](../unprotected/Rogers-seln.pdf) Not
     quite enough selection (or perhaps a bit too much).

  <dl>
  <dt>Optional</dt>
   * [Pritchard] [Pritchard:OGH-24] sections 2.5-2.7
  </dl>

1. <?php datedlink("mut_sel.pdf",
  	"When bad things happen to good genes: mutation vs selection");?>

   * Gillespie section 3.4

   * [Fu 2013] [Fu:N-493-216]

1. <?php datedlink("load.pdf", "Genetic load");?>

   * Gillespie section 3.5

1. <?php datedlink("adaptfix.pdf", "Fixation of mutations");?>

  * Gillespie sections 3.9-3.10

  * [Islands simulation](islands.html)

1. <?php datedlink("ld-2x3.pdf", "Neutral evolution at two loci");?>

   * Gillespie sections 4.0-4.1

1. <?php datedlink("twolocseln-2x3.pdf", "Selection two loci");?>

   * Gillespie section 4.2

1. <?php datedlink("ldseln-2x3.pdf", "Why LD helps us find selective
     sweeps");?>

  * [Rogers. 2018] [rogers:ldseln] Why LD hels us find selective sweeps.

1. <?php datedlink("inbreed-2x3.pdf", "Inbreeding");?>

  *  Gillespie, sections 5.0-5.2

1. <?php datedlink("inbreed2-2x3.pdf", "Inbreeding, drift, and
    fitness");?>

  *  Gillespie, section 5.3

1. <?php datedlink("popstruc-2x3.pdf", "Population structure");?>

  * Gillespie, section 5.5.

  * [Rogers, 2020.](../unprotected/popstruc.pdf) Geographic population
    structure.
  
  <dl>
  <dt>Optional</dt>
  * [Pritchard] [Pritchard:OGH-24] section 2.4
  </dl>

1. <?php datedlink("popstruc-hancock.pdf", "Population structure part 2");?>

1. <?php datedlink("detectseln.pdf",
"Detecting natural selection with genomic data");?>

  * [Vitti et al] [Vitti:ARG-47-1]

  * [Hejase et al 2020] [Hejase:TG-36-243] Summary statistics to gene
  trees: methods for inferring positive selection.

1. <?php datedlink("gdraft.pdf", "Genetic draft");?>

  * Gillespie section 4.3.

1. <?php datedlink("pophist-2x3.pdf", "Population history from whole
     genomes");?>

  * [Li and Durbin](../protected/Li-N-475-493)

  <dl>
  <dt>Optional</dt>
  * [Rogers 2024](https://doi.org/10.1101/2023.07.28.551046)
  </dl>

1. <?php datedlink("speda-2x3.pdf", "Archaic genes in modern humans");?>

  * [Rogers. 2022.] [rogers:speda] Using genetic data to build
    intuition about population history. 

  <dl>
  <dt>Optional</dt>
  * [Mendez et al, 2012](../protected/Mendez-MBE-29-1513.pdf) Global
    Genetic Variation at OAS1 Provides Evidence of Archaic Admixture
    in Melanesian Populations.

  * [Vernot and Akey, 2014](../protected/Vernot-Science-343-1017.pdf)
    Resurrecting surviving Neandertal lineages from modern human
    genomes.

  * [Castellano et al, 2014](../protected/Castellano-PNA-111-6666.pdf)
  </dl>

1. <?php datedlink("QTs1a.pdf",
"QTs 1: genes and environment");?>

  * Gillespie, sections 6.0-6.1

1. <?php datedlink("QTs2a.pdf",
"QTs 2: heritability");?>

  * Gillespie, sections 6.0-6.1

1. <?php datedlink("QTs3a.pdf", "QTs 3: response to selection");?>

  * Gillespie, section 6.2

  * [Response to selection on quantitative traits] [rogers:lande]

1. <?php datedlink("trait_mapping.pdf", "Trait mapping");?>

  * [Tam et al. 2019] [Tam:NRG-20-467] Benefits and limitations of
    genome-wide association studies.

  * [Uffelmann et al 2021] [Uffelmann:NRM-1-59] Genome-wide
    association studies.

1. <?php datedlink("missing_heritability.pdf",
"Missing heritability: trait prediction and prospects for personalized
medicine");?>

 * [Manolio et al. 2009] [Manolio:N-461-747] Finding the missing
   heritability of complex diseases

 * [Polygenic risk scores] [NHGRI:PRS]

 * [Massarat et al. 2023] [Massarat:N-617-256] Human pangenome
   supports analysis of complex genomic regions 

  <dl>
  <dt>Optional</dt>
  * [Liao et al 2023] [Liao:N-617-312] A draft human pangenome reference.

  * [Povysil et al. 2019] [Povysil:NRG-20-747] Rare-variant collapsing
  analyses for complex traits: guidelines and applications. 

  * [Choi et al. 2020] [Choi:NP-15-2759] Tutorial: a guide to performing
  polygenic risk score analyses. 
  </dl>

1. <?php datedlink("gwas.pdf", "Genome-Wide Association Studies (GWAS)");?>

1. <?php datedlink("QTevol.pdf", "Evolution of quantitative
   traits");?>

 * [Barghi et al. 2020] [Barghi:NRG-21-769] Polygenic adaptation: a
   unifying framework to understand positive selection.

[rogers20:chpc]:
https://www.chpc.utah.edu/news/newsletters/spring2020_newsletter.pdf

[rogers20:sa]:
https://advances.sciencemag.org/content/6/8/eaay5483

[rogers:JEPr]:
http://content.csbs.utah.edu/~rogers/pubs/Rogers-JEP.pdf

[rogers:lande]:
../unprotected/Rogers-lande.pdf

[rogers:LNGG]:
../ggeneal.pdf

[rogers:ldseln]:
../unprotected/ldseln.pdf

[rogers:spectrum]:
https://arxiv.org/abs/2103.00335

[rogers:speda]:
https://arxiv.org/abs/2201.02668

[rogers:vocab]:
../unprotected/vocab.pdf

[Mgenomes:N-467-1061]:
../protected/Mgenomes-N-467-1061.pdf

[Mgenomes:N-491-56]:
../protected/Mgenomes-N-491-56.pdf

[Mgenomes:N-526-68]:
../protected/Mgenomes-N-526-68.pdf

[Halldorsson:N-607-732]:
../protected/Halldorsson-N-607-732.pdf

[Vitti:ARG-47-1]:
../protected/Vitti-ARG-47-1.pdf

[Hejase:TG-36-243]:
../protected/Hejase-TG-36-243.pdf

[Pritchard:OGH-24]:
https://web.stanford.edu/group/pritchardlab/HGbook.html

[Coop:PQG-20]:
https://github.com/cooplab/popgen-notes/releases/tag/v1.1

[Fu:N-493-216]:
../protected/Fu-N-493-216.pdf

[Tam:NRG-20-467]:
../protected/Tam-NRG-20-467.pdf

[Uffelmann:NRM-1-59]:
../protected/Uffelmann-NRM-1-59.pdf

[Manolio:N-461-747]:
../protected/Manolio-N-461-747.pdf

[NHGRI:PRS]:
https://www.genome.gov/Health/Genomics-and-Medicine/Polygenic-risk-scores

[Massarat:N-617-256]:
https://www.nature.com/articles/d41586-023-01490-3.pdf

[Barghi:NRG-21-769]:
../protected/Barghi-NRG-21-769.pdf

[Liao:N-617-312]:
../protected/Liao-N-617-312.pdf

[Povysil:NRG-20-747]:
../protected/Povysil-NRG-20-747.pdf

[Choi:NP-15-2759]:
../protected/Choi-NP-15-2759.pdf
