#!/usr/bin/perl
use Switch;
print "Content-type: text/html\n\n";
print "<BODY bgcolor=\"#000000\" text = \"#ffffff\" link = \"#990022\"
vlink=\"#002299\">";

$guessed="$ENV{'QUERY_STRING'}";

$startq  = index($guessed,"question=")+9;
$question_number = substr($guessed,$startq,1);

$all_answers =~ s/%3D/=/g;
$all_answers =~ s/%26/&/g;
$guessed =~ s/%3D/=/g;
$guessed =~ s/%26/&/g;

$start1  = index($guessed,"q1=")+3;
$answer1 = substr($guessed,$start1,1);

if ($answer1 < 1) {$answer1 = 0}

if (  ($question_number == 2) && ( index($guessed,"q2=") < 0 ) ) {  $guessed = $guessed . "&q2=0" };
if (  ($question_number == 3) && ( index($guessed,"q3=") < 0 ) ) {  $guessed = $guessed . "&q3=0" };
if (  ($question_number == 4) && ( index($guessed,"q4=") < 0 ) ) {  $guessed = $guessed . "&q4=0" };
$all_answers = substr($guessed,$startq+2,299);

print "
<center><BR><BR>

<img src=\"http://www.destinyland.org/cgi-bin/San%20Francisco%20Giants%20NLCS.jpg\" width=200px>
<h3><em>Which San Francisco Giant are You?</em></h3></center>
</div>

<center>
<table style=\"border: 2px solid #FB5B1F\; padding-top:30px\; padding-bottom:15px\; padding-left:40px\; padding-right:40px\">
<tr><td style=\"color:white\">

<form Method=\"get\" action=http://www.destinyland.org/cgi-bin/giantsquiz.cgi> 
<em>";

if ( $question_number  == 1 ){

        print "<INPUT TYPE=\"hidden\" NAME=\"question\" VALUE=\"2\">";
        print "<INPUT TYPE=\"hidden\" NAME=\"q1\" VALUE=\"$answer1\">";

	print "The quality for which I am most known is...
	<blockquote>
	<input type=\"radio\" name=\"q2\" value=\"1\"> Intelligence<br>
	<input type=\"radio\" name=\"q2\" value=\"2\"> Raw power<br>
	<input type=\"radio\" name=\"q2\" value=\"3\"> A charming personality<br>
	<input type=\"radio\" name=\"q2\" value=\"4\"> Versatility<br>
	<input type=\"radio\" name=\"q2\" value=\"5\"> Erratic brilliance<br>
	";
	}

elsif ( $question_number  == 2 ){

        print "<INPUT TYPE=\"hidden\" NAME=\"question\" VALUE=\"3\">";
        print "<INPUT TYPE=\"hidden\" NAME=\"previous\" VALUE=\"$all_answers\">";

	print "My day-to-day philosophy is: 
	<blockquote>
	<input type=\"radio\" name=\"q3\" value=\"1\"> Have fun<br>
	<input type=\"radio\" name=\"q3\" value=\"2\"> Win at all costs<br>
	<input type=\"radio\" name=\"q3\" value=\"3\"> Do the best I can<br>
	<input type=\"radio\" name=\"q3\" value=\"4\"> Go for it!<br>
	<input type=\"radio\" name=\"q3\" value=\"5\"> Just keep being awesome<br>
	";
	}


elsif ( $question_number  == 3 ){

        print "<INPUT TYPE=\"hidden\" NAME=\"question\" VALUE=\"4\">";
        print "<INPUT TYPE=\"hidden\" NAME=\"previous\" VALUE=\"$all_answers\">";

	print "How do you feel about the rest of the world? 
	<blockquote>
	<input type=\"radio\" name=\"q4\" value=\"1\"> I want to travel and make new friends<br>
	<input type=\"radio\" name=\"q4\" value=\"2\"> There's really no place like home<br>
	<input type=\"radio\" name=\"q4\" value=\"3\"> I'm contented no matter where I am<br>
	<input type=\"radio\" name=\"q4\" value=\"4\"> It's not where you are, it's what you're doing<br>
	<input type=\"radio\" name=\"q4\" value=\"5\"> I don't like to travel too far away<br>
	";
	}


else {


	$start1  =  index($all_answers,"q1=")+3;
	$answer1 = substr($all_answers,$start1,1);
	$answer2 = substr($all_answers,$start1+5,1);
	$answer3 = substr($all_answers,$start1+10,1);
	$answer4 = substr($all_answers,$start1+15,1);

	$panda  = 0;
	$tim    = 0;
	$hunter = 0;
	$bocchi = 0;
	$mascot  = 0;

	switch ($answer1) {
	    case 0 { $tim++	}
	    case 1 { $bocchi++  }
	    case 2 { $mascot++  }
	    case 3 { $hunter++  }
	    case 4 { $tim++	}
	    case 5 { $panda++ 	}
	};


	switch ($answer2) {
	    case 0 { $tim++	}
	    case 1 { $bocchi++  }
	    case 2 { $panda++   }
	    case 3 { $mascot++  }
	    case 4 { $hunter++  }
	    case 5 { $tim++	}
	};

	switch ($answer3) {
	    case 0 { $tim++	}
	    case 1 { $mascot++	}
	    case 2 { $bocchi++ }
	    case 3 { $tim++	}
	    case 4 { $panda	}
	    case 5 { $hunter++	}
	};

	switch ($answer4) {
	    case 0 { $tim++	}
	    case 1 { $panda++	}
	    case 2 { $mascot++  }
	    case 3 { $tim++	}
	    case 4 { $hunter	}
	    case 5 { $bocchi	}
	};



	@ranks = sort ($mascot, $tim, $hunter, $bocchi, $panda);


	
	$winner = pop(@ranks); 

	if ($winner == $hunter) {

print "
 <img src=\"Hunter Pence.gif\" align=\"left\" style=\"padding-right:30px; padding-bottom:15px\" width=400>

You are: Hunter Pence!

<P>
<div style=\"position:relative; left:20px; padding-right:10px\">

You're talented, wholesome, and too good to be true.  After piling up an impressive stack of awards,
you've achieved an exciting pace that sets you apart from the others around you.
<P>
All the buzz around you may stir up the occasional wise crack, but you take it with a smile.  Maybe it's because you're
a good person, or because you're humble.
<P>Or 
because you know that they don't make fun of nobodies...


</div>

"


	}

	elsif ($winner == $tim) {


print "
<img src=\"Tim Lincecum.jpg\" align=\"left\" style=\"padding-right:30px; padding-bottom:15px\">
You are: Tim Lincecum!
<div style=\"position:relative; left:20px; padding-right:10px\">
<P>
So fly your \"Freak\" flag high! And be proud, because when you're at your best, you just can't be beaten.
<P>
You know the greatness within, and any hard times that come your way are just
an opportunity to show the world your strong spirit.  (And to surprise any doubters with the brilliance that lurks within...)
<P>
They may not understand you, but they'll eventually learn just how much you're capable of...</div>
"



	}


	elsif ($winner == $mascot) {


print "
 <img src=\"LouSeal_with_Twins.JPG\" align=\"left\" style=\"padding-right:30px; padding-bottom:15px\" width=400>

You are: Lou Seal!

<P>
<div style=\"position:relative; left:20px; padding-right:10px\">

You're a winner! A party animal!  And everyone's happy to see you...
<P>
You inspire cheers, delight, and enthusiasm wherever you go. 
And though you may greet visitors from around the world,
you're happiest on your home turf.  People appreciate your
loyalty and your down-to-earth enthusiasm.  <P>And 
the things you like most are good times, hanging with friends, being outdoors,
and most of all, celebrating!
</div>

"



	}

	elsif ($winner == $bocchi) {


print "
 <img src=\"Bruce BOCHY.jpg\" align=\"left\" style=\"padding-right:30px; padding-bottom:15px\" width=400>

You are: Bruce Bochy!

<P>
<div style=\"position:relative; left:20px; padding-right:10px\">

You're a winner, and part of a rare elite, reaching that high pinnacle where your insights
are valued and shared with those around you...  

<P>Your long experience is respected, and your years of accumuluated knowledge have been transformed into tangible
victories.  But you're ready for fresh challenges, and every day you dive back into the fight -- surrounded by your loyal team.
<P>By now everyone who matters already knows just how good you are, and each day you set out with confidence to do it
one more time...

</div>

"



	}


	elsif ($winner == $panda) {
		print " <img src=\"pablo-sandoval.jpg\" align=\"left\" style=\"padding-right:30px; padding-bottom:15px\" width=400>

You are: Pablo Sandoval!

<P>
<div style=\"position:relative; left:20px; padding-right:10px\">

Your raw power combines with a positive personality. And you have the sharp instincts of a Kung Fu Panda!<P>

You know that records were made to be broken, and you're not afraid to take on the world.  You can take 
a moment in time and turn it into a powerful performance just through willpower and determination.  You're a 
mountain of talent, a beloved local hero...
<P>
And you face each day with strenth, confidence, and 
the smile of success.

<P>

</div>
"
	}


exit

}


print "
</blockquote>
<center><BR>
<input type=\"submit\" Value=\"Click here to continue\" ></center>
</em></td></tr></table>
</body>
</html>
";
