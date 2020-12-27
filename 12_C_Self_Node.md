
Special self node `I`:

```
$ p 1221 self I mn wn: s:
```

It can be linked to `dev_A` on `dev_A`:

```
$ p Graph/dev_A Graph/I/link w:
$ p Graph/I/link fi: s:

fgl_s 451 < 3 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph/I/link', 2 => 'fi:', 3 => 's:', ), 
1 => 'phos.php', 
2 => array ( 0 => 'Graph/dev_A', ), )
```

On `dev_B`, `I` can be linked to `dev_B`. And so on.

```
$ p Graph/dev_B Graph/I/link w:
```

To show details of `I`:

```
$ p Graph rn: av: 1 i: s:

fgl_s 451 < 4 > array ( 
0 => array ( 0 => 'phos.php', 1 => 'Graph', 2 => 'rn:', 
             3 => 'av:', 4 => '1', 5 => 'i:', 6 => 's:', ), 

1 => 'phos.php', 2 => 'Graph', 

3 => array ( 
'Graph/I' => array ( ), 
'Graph/I/link' => 'Graph/I/link',
'Graph/I/name' => 'Graph/I/name', 
'Graph/I/pbk' => 'Graph/I/pbk', 
'Graph/I/role' => 'Graph/I/role', 
), )
```
