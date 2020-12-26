

## Graph. Path. File. JSON.

- Filename: month letter others .md

Unix path is derived from graph theory path.

1. `mn` make node
2. `wn:` write node; `:` in Phoscript signifies native (PHP) function.
3. `rn:` read node

- `mn` is defined using Phoscript alias as follows. `mknode` is retained for compatibility.

```
F(": mknode array: over: name apk: swap: . over: role apk: swap: . over: pbk apk: ;");
// 1221 device dev_B mknode s:
// definition followed by example

F(": mn mknode ;"); // mn make node; wn: write node; rn: read node;
```
`pbk role node_name mn wn:` creates a node in the form of a PHP associative array (object) &mdash; when written to file using `wn:` it becomes a directory tree `node_name`, with files `pbk` containing public key, and `role` containing role description.

They can be displayed with `ls -R Graph`:

```
$ ls -R Graph
Graph:
dev_A  dev_B

Graph/dev_A:
address  name  pbk  role

Graph/dev_B:
name  pbk  role
```

`rn:` recursively read the directory tree and reconstruct a PHP associative array (object), which is displayed with the `s:` (show stack) command:

```
$ php phos.php dev_B Graph rn: s:

fgl_s 451 < 5 > array ( 0 => array ( 0 => 'phos.php', 1 => 'dev_B', 2 => 'Graph', 3 => 'rn:', 4 => 's:', ), 1 => 'phos.php', 2 => 'dev_B', 3 => 'Graph', 4 => array ( 'Graph' => array ( ), 'Graph/dev_A' => array ( 'Graph/dev_A' => array ( ), 'Graph/dev_A/address' => 'Graph/dev_A/address', 'Graph/dev_A/name' => 'Graph/dev_A/name', 'Graph/dev_A/pbk' => 'Graph/dev_A/pbk', 'Graph/dev_A/role' => 'Graph/dev_A/role', ), 'Graph/dev_B' => array ( 'Graph/dev_B' => array ( ), 'Graph/dev_B/name' => 'Graph/dev_B/name', 'Graph/dev_B/pbk' => 'Graph/dev_B/pbk', 'Graph/dev_B/role' => 'Graph/dev_B/role', ), ), )
```

The output above is reformatted for clarity:

```
fgl_s 451 < 5 > array ( 0 => array ( 0 => 'phos.php', 1 => 'dev_B', 2 => 'Graph', 3 => 'rn:', 4 => 's:', ), 1 => 'phos.php', 2 => 'dev_B', 3 => 'Graph', 

4 => array ( 
    
    'Graph' => array ( ), 
    
    'Graph/dev_A' => array ( 'Graph/dev_A' => array ( ), 'Graph/dev_A/address' => 'Graph/dev_A/address', 'Graph/dev_A/name' => 'Graph/dev_A/name', 'Graph/dev_A/pbk' => 'Graph/dev_A/pbk', 'Graph/dev_A/role' => 'Graph/dev_A/role', ), 
    
    'Graph/dev_B' => array ( 'Graph/dev_B' => array ( ), 'Graph/dev_B/name' => 'Graph/dev_B/name', 'Graph/dev_B/pbk' => 'Graph/dev_B/pbk', 'Graph/dev_B/role' => 'Graph/dev_B/role', ), ), )


```
