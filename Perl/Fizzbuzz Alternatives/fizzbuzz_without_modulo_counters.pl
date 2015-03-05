#!usr/bin/perl

# Implements 'Fizzbuzz' without using the modulo operation.
# This one uses counters. 
#
#
# Inspired by this discussion on Reddit. 
#
#   http://www.reddit.com/r/learnprogramming/comments/2xkf3i/how_do_we_write_fizzbuzz_or_how_i_interviewed/


$true   = 1;
$false  = 0;

$threes = 0;
$fives  = 0;

$print_number = $true;


for ($x = 1; $x <= 100; $x++) {

    if ( $x - $threes * 3 == 3 ){
        $threes++;
	print "fizz";
	$print_number = $false;
    };

    if ($x - $fives * 5   == 5) {
        $fives++;
        print "buzz";
        $print_number = $false;
    }

    if ($print_number) { 
	print "  " . $x 
    } else { $print_number = $true } ;

    print "\n";

}
