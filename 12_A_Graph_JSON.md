## Graph. Path. File. JSON.

<!-- - Filename: month letter others .md -->

The Unix path is derived from graph theory path. After many years of winding paths (pun intended) of developments in computer programming, we finally have JSON (JavaScript Object Notation).

Using Phoscript, we define the following functions for storing JSON as Unix files:

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

```
$ date
Sabtu 26 Dis 2020 03:27:01  +08
$ php phos.php 1221 device dev_A mn wn:
$ ls -lR Graph
Graph:
total 8
drwxrwxr-x 2 hongwu hongwu 4096 Dis  26 10:06 dev_A
drwxrwxr-x 2 hongwu hongwu 4096 Dis  25 19:39 dev_B

Graph/dev_A:
total 16
-rw-rw-r-- 1 hongwu hongwu 1 Dis  26 10:06 address
-rw-rw-r-- 1 hongwu hongwu 5 Dis  26 15:27 name
-rw-rw-r-- 1 hongwu hongwu 4 Dis  26 15:27 pbk
-rw-rw-r-- 1 hongwu hongwu 6 Dis  26 15:27 role

Graph/dev_B:
total 12
-rw-rw-r-- 1 hongwu hongwu 5 Dis  25 19:39 name
-rw-rw-r-- 1 hongwu hongwu 4 Dis  25 19:39 pbk
-rw-rw-r-- 1 hongwu hongwu 6 Dis  25 19:39 role
```
Note the date/time above in subdirectory `dev_A`.


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

PHP associative arrays can be coverted to and from JSON using the following commands:

- `je:` maps to `json_encode()`
- `jd:` maps to `json_decode()`

Examples:

```
$ php phos.php dev_B Graph rn: je: s:

fgl_s 451 < 5 > array ( 0 => array ( 0 => 'phos.php', 1 => 'dev_B', 2 => 'Graph', 3 => 'rn:', 4 => 'je:', 5 => 's:', ), 1 => 'phos.php', 2 => 'dev_B', 3 => 'Graph', 4 => '{"Graph":[],"Graph\\/dev_A":{"Graph\\/dev_A":[],"Graph\\/dev_A\\/address":"Graph\\/dev_A\\/address","Graph\\/dev_A\\/name":"Graph\\/dev_A\\/name","Graph\\/dev_A\\/pbk":"Graph\\/dev_A\\/pbk","Graph\\/dev_A\\/role":"Graph\\/dev_A\\/role"},"Graph\\/dev_B":{"Graph\\/dev_B":[],"Graph\\/dev_B\\/name":"Graph\\/dev_B\\/name","Graph\\/dev_B\\/pbk":"Graph\\/dev_B\\/pbk","Graph\\/dev_B\\/role":"Graph\\/dev_B\\/role"}}', )
```

```
$ php phos.php dev_B Graph rn: je: jd: s:

fgl_s 451 < 5 > array ( 0 => array ( 0 => 'phos.php', 1 => 'dev_B', 2 => 'Graph', 3 => 'rn:', 4 => 'je:', 5 => 'jd:', 6 => 's:', ), 1 => 'phos.php', 2 => 'dev_B', 3 => 'Graph', 4 => array ( 'Graph' => array ( ), 'Graph/dev_A' => array ( 'Graph/dev_A' => array ( ), 'Graph/dev_A/address' => 'Graph/dev_A/address', 'Graph/dev_A/name' => 'Graph/dev_A/name', 'Graph/dev_A/pbk' => 'Graph/dev_A/pbk', 'Graph/dev_A/role' => 'Graph/dev_A/role', ), 'Graph/dev_B' => array ( 'Graph/dev_B' => array ( ), 'Graph/dev_B/name' => 'Graph/dev_B/name', 'Graph/dev_B/pbk' => 'Graph/dev_B/pbk', 'Graph/dev_B/role' => 'Graph/dev_B/role', ), ), )
```
