- Story / 

Scenario to Code.

Adam passes Can A to Brian.

Brian carries Can A to store room.

```
begin: can_A.address = p_Adam.address

end:   can_A.address = p_Brian.address
```

Create nodes for the above.

Phoscript is the least cost common denominator that can be translated into any platforms or programming languages.

```
alias p='php phos.php'
```

```
$ p Graph rn: av: 1 i: s:

fgl_s 451 < 4 > array ( 0 => array ( 0 => 'phos.php', 1 => 'Graph', 2 => 'rn:', 3 => 'av:', 4 => '1', 5 => 'i:', 6 => 's:', ), 1 => 'phos.php', 2 => 'Graph', 

3 => array ( 
  'Graph/can_A' => array ( ), 
  'Graph/can_A/address' => 'Graph/can_A/address', 
  'Graph/can_A/name' => 'Graph/can_A/name', 
  'Graph/can_A/pbk' => 'Graph/can_A/pbk', 
  'Graph/can_A/role' => 'Graph/can_A/role', 
  ), )
```

```
$ ls -R Graph/can_A
Graph/can_A:
address  name  pbk  role
```

```
$ p p_Adam.address Graph/can_A/address w: s:
$ p Graph/can_A/address fi: s:

fgl_s 451 < 3 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph/can_A/address', 2 => 'fi:', 3 => 's:', ), 
1 => 'phos.php', 
2 => array ( 0 => 'p_Adam.address', ), )

$ p p_Brian.address Graph/can_A/address w: s:
$ p Graph/can_A/address fi: s:

fgl_s 451 < 3 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph/can_A/address', 2 => 'fi:', 3 => 's:', ), 
1 => 'phos.php', 
2 => array ( 0 => 'p_Brian.address', ), )
```
