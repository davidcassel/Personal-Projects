#!usr/bin/perl

# Implements 'Fizzbuzz' without using the modulo operation.
# Uses a comically long cycle of variables
#
# Inspired by this discussion on Reddit. 
#
#   http://www.reddit.com/r/learnprogramming/comments/2xkf3i/how_do_we_write_fizzbuzz_or_how_i_interviewed/


$false = 0;
$true  = 1;
$print_number = $true;

		 $one_of_three   = $true;
    	         $two_of_three   = $false; 
	         $three_of_three = $false;

		 $one_of_five   = $true;
	 	 $two_of_five   = $false;
		 $three_of_five = $false;
		 $four_of_five  = $false;
	         $five_of_five  = $false;

for ($x = 1; $x <= 100; $x++) {

    if ($three_of_three == $true ) {

	print "fizz";
        $print_number = $false;

        $three_of_three = $false;
	$one_of_three   = $true;
	
    } elsif ($one_of_three == $true) {
        $one_of_three = $false;
        $two_of_three = $true;
    } else {
        $two_of_three  = $false;
        $three_of_three = $true;
    };

    if ($five_of_five == $true) {

        print "buzz";
        $print_number = $false;

        $five_of_five = $false;        
	$one_of_five  = $true;

    } elsif ($one_of_five == $true) {
        $one_of_five = $false;
        $two_of_five = $true;
    } elsif ($two_of_five == $true) {
       $two_of_five = $false;
       $three_of_five = $true;
    } elsif ($three_of_five == $true) {
       $three_of_five = $false;
       $four_of_five = $true;
    } else { 
       $four_of_five = $false;
       $five_of_five = $true;
    }

    # If not fizz or buzz, then print the number. 
    # Otherwise, toggle the $print_number flag so we're ready for next time

    if ($print_number == $true) { print "  $x  " 
    } else {$print_number = $true};

    print "\n";

}
