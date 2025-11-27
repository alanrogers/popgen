# Human Evolutionary Genetics

## Introduction

This repository contains materials for a course I taught from 2000
through 2024 under the title *Human Evolutionary Genetics*. I taught
it first on my own, then with Henry Harpending, and then (for years
and years) with Jon Seger. During the final semester, Jon and I taught
it together with Angela Hancock.  It was cross-listed at the
University of Utah between the Anthropology and Biology Departments
under the designations Anth5221 and Biol5221.

The files on the website for this course are of several types: lecture
slides, tutorials, and so on. Most of these are written in LaTeX or
Markdown, and the sources are in various subdirectories below:

* **homework** contains a 43-page collection of algebraic homework
  exercises, with answers to even-numbered exercises at the back.

* **lab** contains a 59-page lab manual

* **slides** contains lecture slides

* **tutorial** contains tutorials on a variety of subjects

* **exam** contains source code for 3 exams

* **src** contains Python source code for all the lab assignments

* **syllabus** contains the main course syllabus

* **labsyl** contains the lab syllabus

* **studyguide** contains some outdated study guides. I stopped
  updating these a few years ago, because the homework, lecture
  slides, and lab materials are better sources than the study guides
  ever were.

* **txt** contains a 74-page introduction to gene genealogies, also
  known as "coalescent theory".

* **websrc** contains Markdown code, which creates HTML or PHP files,
  which provide much of the structure of the website.

* **website** contains the entire website. When I update any of the
  files mentioned above, the next step is to copy it into the
  appropriate position with the `website` subdirectory.

## Pushing files onto a remote web server

On my websites, I use PHP code to display the time at which each file
was last modified. This enables students to tell whether they are
looking at a new version the file, or one from some previous
semester. Unfortunately, github doesn't allow PHP on pages it hosts,
so I don't use its hosting service. The following paragraphs describe
the method I use for pushing files from the `website` directory below
onto a web server at the University of Utah.


    #!/bin/sh
    find ~/website -name "*~" -exec rm {} \;
    chmod -R go+r ~/website/* 
    find ~/website -type d -exec chmod +x {} \;
	
	# Removed "-e ssh" from rsync command because (in my U's computing
	# environment) it is no longer to transfer files between machines
	# using "rsync". One must instead mount a remote directory using
	# SMB (Windows) or SAMBA (Linux or Mac). In this new setup, "-e
    # ssh" would not save time or improve security, because the
    # encryption and decryption steps would both happen on the local
	# machine. In this new setup, the process of pushing to the server
	# is *much* slower.
	
    cd; rsync -rptvz --copy-links --delete website/    \
	  /Volumes/u0028949/html-docs/public_html/
