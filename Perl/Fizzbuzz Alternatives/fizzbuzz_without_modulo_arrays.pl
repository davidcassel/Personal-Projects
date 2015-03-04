#!usr/bin/perl

# Implements 'Fizzbuzz' without using the modulo operation.
# This one replaces it with arrays and array functions.
#
# Inspired by this discussion on Reddit. 
#
#   http://www.reddit.com/r/learnprogramming/comments/2xkf3i/how_do_we_write_fizzbuzz_or_how_i_interviewed/


$false = 0;
$true  = 1;
$print_number = $true;


@threes = (1,0,0);
@fives  = (1,0,0,0,0);


for ($x = 1; $x <= 100; $x++) {

   $divisible = pop(@threes);
   if ($divisible == 1 ) {unshift(@threes, 1); 
   } else { unshift(@threes, 0) };

   $other_divisible = pop(@fives);
   if ($other_divisible == 1 ) { unshift(@fives, 1) ;
   } else { unshift(@fives, 0)  };

   if ( (!$divisible) && (!$other_divisible) ) { print "  $x"} 
   else {

	   if ($divisible) { print "fizz" };
	   if ($other_divisible) { print "buzz" };

    };

    print "\n";

}
