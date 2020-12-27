- Story / 

## Scenario to Code

In this article, we describe a scenario where 
Adam decides to recycle a empty can (a Coke can, shown below)
by giving it away to Brian, who works for 
a recycling company:

1. Adam passes Can A to Brian.

2. Brian carries Can A to a store room.

Expressed in JavaScript or equivalent programming languages:

```
begin: can_A.location = p_Adam.location

end:   can_A.location = p_Brian.location
```



Create nodes for the above.




```
alias p='php phos.php'
```

```
$ p Graph rn: av: 1 i: s:

fgl_s 451 < 4 > array ( 

0 => array ( 0 => 'phos.php', 1 => 'Graph', 2 => 'rn:', 3 => 'av:', 4 => '1', 5 => 'i:', 6 => 's:', ), 1 => 'phos.php', 

2 => 'Graph', 

3 => array ( 
  'Graph/can_A' => array ( ), 
  'Graph/can_A/address' => 'Graph/can_A/address', 
  'Graph/can_A/location' => 'Graph/can_A/location', 
  'Graph/can_A/name' => 'Graph/can_A/name', 
  'Graph/can_A/pbk' => 'Graph/can_A/pbk', 
  'Graph/can_A/role' => 'Graph/can_A/role', 
  ), )

```

```
$ ls -R Graph/can_A
Graph/can_A:
address  location  name  pbk  role
```

```
$ p p_Adam.location Graph/can_A/location w: s:
$ p Graph/can_A/location fi: s:

fgl_s 451 < 3 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph/can_A/location', 2 => 'fi:', 3 => 's:', ), 
1 => 'phos.php', 
2 => array ( 0 => 'p_Adam.location', ), )

$ p p_Brian.location Graph/can_A/location w: s:
$ p Graph/can_A/location fi: s:

fgl_s 451 < 3 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph/can_A/location', 2 => 'fi:', 3 => 's:', ), 
1 => 'phos.php', 
2 => array ( 0 => 'p_Brian.location', ), )
```

- Add intermediate steps: p_Adam 

From the examples above, we hope to demonstrate that:
- Phoscript is equivalent to "pseudocode" in the literal sense,
- Yet, it is a full fledged programming language, 
- Capable of being translated to any other known
Programming languages and platforms.
- Hence, we describe Phoscript as a metaprogramming script.


Phoscript is the least cost common denominator that can be translated into any platforms or programming languages.
