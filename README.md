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

* **Makefile** is described below.

## Pushing files onto a remote web server

On my websites, I use PHP code to display the time at which each file
was last modified. This enables students to tell whether they are
looking at a new version the file, or one from some previous
semester. Unfortunately, github doesn't allow PHP on pages it hosts,
so I don't use its hosting service. The following paragraphs describe
the method I use for pushing files from the `website` directory below
onto a web server at the University of Utah.

On my personal computer, there is a directory for each course, and
each of these has a subdirectory called `website`. When I modify a
file, the next step is to copy the file (sometimes changing its name)
into the appropriate place within the `website` subdirectory for the
course.

There is also a global `website` directory immediately below the home
directory on my personal computer. This is a mirror image of my
website on the remote server. It contains (among other things) a
subdirectory for each course. When I've made changes to the `website`
subdirectory of a course, the next step is to push them into this
global `website` directory. To do this, `cd` into the top-level
directory of the course and type `make website`. This calls the `make`
command, which reads the file `Makefile` in the current directory and
then copies the course `website` tree into the global `website`.

The final step is to push the global `website` onto the remote server.
The details of this step will depend on the hosting service you use,
so all I can do is describe how it works in my own computing
environment. I use a shell script whose contents are shown below. It uses
the `rsync` command to copy an entire directory tree from one place to
another. The `--delete` option deletes remote files that are not in
the local `website` directory. This means that you can delete files
from the server simply by removing them from the local directory.

If your hosting service allows you to use the rsync command directly,
then add `-e ssh` to the rsync command below. This compresses and
encrypts the content and makes things much faster. My university's
hosting service no longer supports this. One must instead mount the
remote directory using SMB (Windows) or SAMBA (Linux or Mac). In this
setup, `-e ssh` would not save time or improve security, because the
compression and decompression steps would both happen on the local
machine. In this new setup, the process of pushing to the server is
*much* slower.

The shell script below should be copied into a file within your own
`$HOME/bin` directory and marked as executable. You'll need to modify
the rsync command so that it specifies a destination on your own web
hosting service.

    #!/bin/sh

    # Remove backup files made by the text editor
    find ~/website -name "*~" -exec rm {} \;

    # Make everything readable by everyone
    chmod -R go+r ~/website/*

    # Make directories executable
    find ~/website -type d -exec chmod +x {} \;
	
    # Copy the directory tree below $HOME/website onto the remote
	# server, which is mounted using SMB/SAMBA.
    cd; rsync -rptvz --copy-links --delete website/    \
	  /Volumes/u0028949/html-docs/public_html/

On my machine, this executable shell script is called
`installcsbs`. After mounting the remote directory using SAMBA, I type
`installcsbs` to copy the `website` directory from my local machine
onto the remote server.
