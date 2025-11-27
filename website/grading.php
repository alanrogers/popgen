<html>
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
<head>
<title>Biol 5221: How We Curve Grades</TITLE>
</head>
<style type="text/css">
body {font-family :Arial}
</style>
<body>
<h1>How We Curve Grades</h1>
<p>
Each assignment is curved separately, as explained below.  Students
then get the higher of the raw and curved scores.  This accomplishes
two goals: (a) the class is not penalized when an assignment is harder
than it should be, and (b) if everyone does well, then everyone gets a
high grade.
</p>

<p>
The initial curved score, y, is equal to a + b*x, where x is the raw
score (percent of answers correct), and the two constants (a and b)
are chosen so that y has median 85 and maximum value 100.  Then the student
gets the maximum of x and y.  Thus, the curve never reduces a
student's score.
</p>

<p>
For each student, the curved scores of the various assignments are
averaged to get the final score.  We assign letter grades
subjectively, based on these final scores.
</p>

<h1>Anonymized scores</h1>
<p>
The link below will take you to a page that contains anonymized
scores.  If you know the (uncurved) score you got on each assignment,
you can look up your current grade in the course.

Click
<?php datedlink("curve.html", "here");?> for the scores.
</body>

</html>
