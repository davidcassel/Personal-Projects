#!/usr/bin/perl
print "Content-type: text/html\n\n";

# June 17, 2010
# A personal project by David Cassel
#
# This script generates a valid Sudoku puzzle (with three rows of three 9-number boxes).
#
# It then displays its solution on a web page.


$data = "$ENV{'QUERY_STRING'}";
print " $data <BR><BR>";

$startnums = index($data," = ")+1;
$allnums = substr($data,$startnums,9);
@newnums =  split(undef,$allnums);


$data = ~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$data = ~ tr/+/ /;
$data = ~ s/'/&#146;/g;
$data = ~ s/"/&#34;/g;

# $starttitle = index($data,"ptitle = ")+7;
# $endtitle = index($data,"pgoal = ")-1;
# $title = substr($data,$starttitle,($endtitle-$starttitle));




STARTOVER:

@box1 = &fillabox;

@row1 = ($box1[0],$box1[1],$box1[2]);
@row2 = ($box1[3],$box1[4],$box1[5]);
@row3 = ($box1[6],$box1[7],$box1[8]);


@box2 = &fillanotherboxinarow;

push(@row1, ($box2[0],$box2[1],$box2[2])  );
push(@row2, ($box2[3],$box2[4],$box2[5]) );
push(@row3, ($box2[6],$box2[7],$box2[8])  );

@box3 = &fillanotherboxinarow;

push(@row1, ($box3[0],$box3[1],$box3[2]) );
push(@row2, ($box3[3],$box3[4],$box3[5]) );
push(@row3, ($box3[6],$box3[7],$box3[8]) );


STARTOVER2:

@col1 = ($box1[0],$box1[3],$box1[6]);
@col2 = ($box1[1],$box1[4],$box1[7]);
@col3 = ($box1[2],$box1[5],$box1[8]);


@box4 = &fillinaboxinacolumn;

@col4 = ($box2[0],$box2[3],$box2[6]);
@col5 = ($box2[1],$box2[4],$box2[7]);
@col6 = ($box2[2],$box2[5],$box2[8]);

STARTOVER3:
@row4 = ($box4[0],$box4[1],$box4[2]);
@row5 = ($box4[3],$box4[4],$box4[5]);
@row6 = ($box4[6],$box4[7],$box4[8]);

@box5 = &fillinamiddlecolumnbox;

push(@col1, ($box4[0],$box4[3],$box4[6]) );
push(@col2, ($box4[1],$box4[4],$box4[7]) );
push(@col3, ($box4[2],$box4[5],$box4[8]) );

@box7 = &fillinaboxinacolumn;

@col7 = ($box3[0],$box3[3],$box3[6]);
@col8 = ($box3[1],$box3[4],$box3[7]);
@col9 = ($box3[2],$box3[5],$box3[8]);

push(@row4, ($box5[0],$box5[1],$box5[2])  );
push(@row5, ($box5[3],$box5[4],$box5[5]) );
push(@row6, ($box5[6],$box5[7],$box5[8])  );

@box6 = &fillinalastcolumnbox;

push(@col4, ($box5[0],$box5[3],$box5[6]) );
push(@col5, ($box5[1],$box5[4],$box5[7]) );
push(@col6, ($box5[2],$box5[5],$box5[8]) );

@row7 = ($box7[0],$box7[1],$box7[2]);
@row8 = ($box7[3],$box7[4],$box7[5]);
@row9 = ($box7[6],$box7[7],$box7[8]);

@box8 = &fillinbox8;

push(@row7, ($box8[0],$box8[1],$box8[2]) );
push(@row8, ($box8[3],$box8[4],$box8[5]) );
push(@row9, ($box8[6],$box8[7],$box8[8]) );

push(@col7, ($box6[0],$box6[3],$box6[6]) );
push(@col8, ($box6[1],$box6[4],$box6[7]) );
push(@col9, ($box6[2],$box6[5],$box6[8]) );

@box9 = &fillinbox9;

sub fillabox {
    @mybox = ();
    for ($boxpos = 0; $boxpos <9; $boxpos++)
    {
        GETARANDOMNUMBER:
        $pick = 1+int(rand(9));
        @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box
        if (@dummy == 0)
        {push(@mybox,$pick) }
        else {goto GETARANDOMNUMBER};
    };
    return @mybox;
};


sub fillanotherboxinarow {
    @mybox = ();
   for ($boxpos = 0; $boxpos <9; $boxpos++)
   {
        $tries = 0;

        GETARANDOMNUMBER2:
   $pick = 1+int(rand(9));
   @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the ROW!

    if ($boxpos<3){ @dummy2 = grep(/$pick/, @row1)};
    if (($boxpos>2)&&($boxpos<6)){ @dummy2 = grep(/$pick/, @row2)};
    if ($boxpos>5){ @dummy2 = grep(/$pick/, @row3)};

    if ((@dummy == 0) && ( @dummy2 == 0)) {push(@mybox,$pick) 
    } else {$tries++ ;
         if ($tries>20){goto STARTOVER};
         goto GETARANDOMNUMBER2};
    };
    return @mybox;
};


sub fillinaboxinacolumn {
    @mybox = ();
        # boxpos is higher so the modulus will work
   for ($boxpos = 3; $boxpos <12; $boxpos++)
   {     $tries = 0;
        GETARANDOMNUMBER3:
   $pick = 1+int(rand(9));
   @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the COLUMN!!!


if (($boxpos)%3 == 0){ @dummy2 = grep(/$pick/, @col1)}
 elsif ( ($boxpos)%3 == 1){
@dummy2 = grep(/$pick/, @col2)}  else { @dummy2 = grep(/$pick/, @col3)};


  if ((@dummy == 0) && ( @dummy2 == 0))
     {push(@mybox,$pick) }
     else {$tries++ ; if ($tries>20){goto STARTOVER2};
     goto GETARANDOMNUMBER3};
  };
  return @mybox;
};


sub fillinamiddlecolumnbox
{ @mybox = ();
        # boxpos is +3 higher so the modulus will work
  for ($boxpos = 3; $boxpos <12; $boxpos++)
  {
        $tries = 0;
        GETARANDOMNUMBER4:
  $pick = 1+int(rand(9));
  @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the COLUMN!!!


if (($boxpos)%3 == 0){ @dummy2 = grep(/$pick/, @col4)}
 elsif ( ($boxpos)%3 == 1){
@dummy2 = grep(/$pick/, @col5)}  else { @dummy2 = grep(/$pick/, @col6)};

        # Then check if this number's already in a ROW!!!!!

if ($boxpos<6){ @dummy3 = grep(/$pick/, @row4)};
if (($boxpos>5)&&($boxpos<9)){ @dummy3 = grep(/$pick/, @row5)};
if ($boxpos>8){ @dummy3 = grep(/$pick/, @row6)};


  if ((@dummy == 0) && ( @dummy2 == 0) && (@dummy3 == 0))
     {push(@mybox,$pick) }
     else {$tries++ ; if ($tries>20){goto STARTOVER2};
     goto GETARANDOMNUMBER4};
  };
  return @mybox;
};



sub fillinalastcolumnbox
{ @mybox = ();
        # boxpos is +3 higher so the modulus will work
  for ($boxpos = 3; $boxpos <12; $boxpos++)
  {
        $tries = 0;
        GETARANDOMNUMBER5:
  $pick = 1+int(rand(9));
  @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the COLUMN!!!


if (($boxpos)%3 == 0){ @dummy2 = grep(/$pick/, @col7)}
 elsif ( ($boxpos)%3 == 1){
@dummy2 = grep(/$pick/, @col8)}  else { @dummy2 = grep(/$pick/, @col9)};

        # Then check if this number's already in a ROW!!!!!

if ($boxpos<6){ @dummy3 = grep(/$pick/, @row4)};
if (($boxpos>5)&&($boxpos<9)){ @dummy3 = grep(/$pick/, @row5)};
if ($boxpos>8){ @dummy3 = grep(/$pick/, @row6)};


  if ((@dummy == 0) && ( @dummy2 == 0) && (@dummy3 == 0))
     {push(@mybox,$pick) }
     else {$tries++ ; if ($tries>20){goto STARTOVER3};
     goto GETARANDOMNUMBER5};
  };
  return @mybox;
};







sub fillinbox8
{ @mybox = ();
        # boxpos is +3 higher so the modulus will work
  for ($boxpos = 3; $boxpos <12; $boxpos++)
  {
        $tries = 0;
        GETARANDOMNUMBER6:
  $pick = 1+int(rand(9));
  @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the COLUMN!!!


if (($boxpos)%3 == 0){ @dummy2 = grep(/$pick/, @col4)}
 elsif ( ($boxpos)%3 == 1){
@dummy2 = grep(/$pick/, @col5)}  else { @dummy2 = grep(/$pick/, @col6)};

        # Then check if this number's already in a ROW!!!!!

if ($boxpos<6){ @dummy3 = grep(/$pick/, @row7)};
if (($boxpos>5)&&($boxpos<9)){ @dummy3 = grep(/$pick/, @row8)};
if ($boxpos>8){ @dummy3 = grep(/$pick/, @row9)};


  if ((@dummy == 0) && ( @dummy2 == 0) && (@dummy3 == 0))
     {push(@mybox,$pick) }
   else {$tries++ ; if ($tries>20){goto STARTOVER3};
     goto GETARANDOMNUMBER6};
  };
  return @mybox;
};




sub fillinbox9
{ @mybox = ();
        # boxpos is +3 higher so the modulus will work
  for ($boxpos = 3; $boxpos <12; $boxpos++)
  {
        $tries = 0;
        GETARANDOMNUMBER9:
  $pick = 1+int(rand(9));
  @dummy = grep(/$pick/, @mybox); # Check if this number's already in the box

        # Then check if this number's already in the COLUMN!!!


if (($boxpos)%3 == 0){ @dummy2 = grep(/$pick/, @col7)}
 elsif ( ($boxpos)%3 == 1){
@dummy2 = grep(/$pick/, @col8)}  else { @dummy2 = grep(/$pick/, @col9)};

        # Then check if this number's already in a ROW!!!!!

if ($boxpos<6){ @dummy3 = grep(/$pick/, @row7)};
if (($boxpos>5)&&($boxpos<9)){ @dummy3 = grep(/$pick/, @row8)};
if ($boxpos>8){ @dummy3 = grep(/$pick/, @row9)};


  if ((@dummy == 0) && ( @dummy2 == 0) && (@dummy3 == 0))
     {push(@mybox,$pick) }
     else {$tries++ ; if ($tries>20){goto STARTOVER3};
     goto GETARANDOMNUMBER9};
  };
  return @mybox;
};


for ($boxpos = 0; $boxpos <9; $boxpos++)
{

$arraypos = $box1[$boxpos]-1;
$newbox1[$boxpos] = $newnums[$arraypos];

};
print "NEW BOX IS @newbox1 ";



print "<BR>
<table>
<tr>
<td>$box1[0]</td>
<td>$box1[1]</td>
<td>$box1[2]</td>
<td>$box2[0]</td>
<td>$box2[1]</td>
<td>$box2[2]</td>
<td>$box3[0]</td>
<td>$box3[1]</td>
<td>$box3[2]</td>
</tr>

<tr>
<td>$box1[3]</td>
<td>$box1[4]</td>
<td>$box1[5]</td>
<td>$box2[3]</td>
<td>$box2[4]</td>
<td>$box2[5]</td>
<td>$box3[3]</td>
<td>$box3[4]</td>
<td>$box3[5]</td>
</tr>

<tr>
<td>$box1[6]</td>
<td>$box1[7]</td>
<td>$box1[8]</td>
<td>$box2[6]</td>
<td>$box2[7]</td>
<td>$box2[8]</td>
<td>$box3[6]</td>
<td>$box3[7]</td>
<td>$box3[8]</td>
</tr>

<tr>

<td>$box4[0]</td><td>$box4[1]</td><td>$box4[2]</td>
<td>$box5[0]</td><td>$box5[1]</td><td>$box5[2]</td>
<td>$box6[0]</td><td>$box6[1]</td><td>$box6[2]</td>

</tr>
<tr>
<td>$box4[3]</td><td>$box4[4]</td><td>$box4[5]</td>
<td>$box5[3]</td><td>$box5[4]</td><td>$box5[5]</td>
<td>$box6[3]</td><td>$box6[4]</td><td>$box6[5]</td>
</tr>

<tr>
<td>$box4[6]</td><td>$box4[7]</td><td>$box4[8]</td>
<td>$box5[6]</td><td>$box5[7]</td><td>$box5[8]</td>
<td>$box6[6]</td><td>$box6[7]</td><td>$box6[8]</td>
</tr>





<tr>

<td>$box7[0]</td><td>$box7[1]</td><td>$box7[2]</td>
<td>$box8[0]</td><td>$box8[1]</td><td>$box8[2]</td>
<td>$box9[0]</td><td>$box9[1]</td><td>$box9[2]</td>

</tr>

<tr>
<td>$box7[3]</td><td>$box7[4]</td><td>$box7[5]</td>
<td>$box8[3]</td><td>$box8[4]</td><td>$box8[5]</td>
<td>$box9[3]</td><td>$box9[4]</td><td>$box9[5]</td>

</tr>

<tr>
<td>$box7[6]</td><td>$box7[7]</td><td>$box7[8]</td>
<td>$box8[6]</td><td>$box8[7]</td><td>$box8[8]</td>
<td>$box9[6]</td><td>$box9[7]</td><td>$box9[8]</td>

</tr>



</table>
<BR>
";
