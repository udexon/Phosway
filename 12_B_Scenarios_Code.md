## Translating Real Life Scenarios to Code for Decentralized E Commerce (DECCOM) using Phoscript

In this article, we describe a scenario where 
Adam decides to recycle a empty can (a Coke can, shown below)
by giving it away to Brian, who works for 
a recycling company:

1. Adam passes Can A to Brian.

2. Brian carries Can A to a store room.

<img src="https://github.com/udexon/Phosway/blob/master/img/Can_A_Coke_Can.jpg" width=300>

Expressed in JavaScript or equivalent programming languages:

```
begin: can_A.location = p_Adam.location

end:   can_A.location = p_Brian.location
```

Although in this example, there is no monetary transaction, it demonstrates the potential complexties in terms of coding for a seemingly trivial transaction in real life. Further, we show that how such complications in coding can be simplified using Phoscript, a metaprogramming script derived from the Foth programming language.

1. The examples below are executed in Linux `bash` shell. 

We created an alias `p` for `php phos.php` for convenience:

```
$ alias p='php phos.php'
```

2. Make node for empty coke can `can_A`:

```
$ p 1221 drink_can can_A mn wn: s:
```

(Please refer to [previous tutorial](https://github.com/udexon/Phosway/blob/master/12_A_Graph_JSON.md) for definitions and details.)


3.  Read node for `can_A`:

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

`Graph rn:` recursively reads directory `Graph`
and construct object (PHP associative array).

`av:` executes `array_values()` to obtain numerical
indices for array.

`1 i:` selects item 1.

`s:` shows results on stack.

The commands above are equivalent to `ls -R`:

```
$ ls -R Graph/can_A
Graph/can_A:
address  location  name  pbk  role
```

4. The following commands write the locations of `can_A` 
to the file `Graph/can_A/location` before and after Adam
passes it to Brian:

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

`string filename w:` writes `string` to `filename`
using `file_put_contents()`.

`filename fi:` reads `filename` using `file_get_contents()`.



5. From the examples above, we hope to demonstrate that:
- Phoscript is equivalent to "pseudocode" in the literal sense,
- Yet, it is a full fledged programming language, 
- Capable of being translated to any other known
Programming languages and platforms.
- Hence, we describe Phoscript as a metaprogramming script.

Phoscript is the least cost common denominator that can be translated into any platforms or programming languages.

<!--
- Story / 

Create nodes for the above.

- Add intermediate steps: p_Adam 
-->
