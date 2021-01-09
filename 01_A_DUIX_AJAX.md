## DUIX: Unconventional Procedures in AJAX

1. DUIX stands for Decentralized User Interactions, a new framework within the Phosway architure to complement or replace existing MVC type frameworks.

2. Figure 1 shows a PHOS command window, containing commands in Phoscript, that perform the following functions:

- a. querying a graph database at the back end
- b. displaying the query results in a HTML table in the front end
- Figure 1
<img src="https://github.com/udexon/Phosway/blob/master/img/DUIX_AJAX.png" width=600>

3. Many readers may be wondering, how it is possible to introduce any innovation to AJAX, one of the oldest procedure in web programming?

To summarize, DUIX, by "Decentralized" in its name, shifts the authority of programming from the server in the conventional systems, to the User.

This is demonstrated by the ability of the User to enter Phoscript commands in the front end, to control both the front end and the back end.

Readers may raise objections concerning security. We shall address them later.


4. The Phoscript commands are reformatted as follow for better readability:

```
: cell G0 gv: swap: i: th tn: ; 
: row 0 cell 1 cell 2 cell 3 ms: tr tn: ; 
: F_T jd: ak: alert: G0 sv: 
body getn: 0 i: div ce: 
row row row 3 ms: 
table tn: alert: 
ih: alert: ac: alert: ; 
: B_G Graph rn: 
ON ECHO bv: je: ec: ; 
: F_A 333 ; 
B: B_G F_T
```

Folloing Forth convention, `: NAME definition words ... ;` enclosed within `:` colon and `;` semicolon is analogues for function definitions in modern programming languages.

As such, the following "functions" (Colon Definition Words (CDW) in Forth terminology) are defined:

- a. `cell`
- b. `row`
- c. `F_T`
- d. `B_G`
- e. `F_A`

5. The "main program" is:

```
B: B_G F_T
```

`B:` maps to JavaScript function `f_B()` which does the following:

- a. sends commands defined by `B_G` to the back end (`B_` signifies back end while `G` denotes Graph Query) and;
  - i. `B_G` definition: 
```  
: B_G Graph rn: 
ON ECHO bv: je: ec: ;
```
- ...
  - ii. `Graph rn:` `rn:` maps to PHP (back end) function `f_rn()` (read node) named `Graph` (root node);
  - `ON ECHO bv:` turns on `echo` (a nostalgic MSDOS convention!!)
  - `je:` executes `json_encode()` on the results of `rn:`
  - `ec:` sends TOS (top of stack) (`json_encode()` results) to front end, via Ajax.

- b. invokes `F_T` upon receiving Ajax results;
  - i. `F_T` definition:
```
: F_T jd: ak: alert: G0 sv: 
body getn: 0 i: div ce: 
row row row 3 ms: 
table tn: alert: 
ih: alert: ac: alert: ; 
```
- &mdash;
  - ii. `jd:` originally maps to PHP `json_decode()`. We retain the same function name in JavaScript for uniformity.
  - `ak:` originally maps to PHP `array_keys()`, returns an array of keys from the input object.
  - `alert:` shows TOS (top of stack) in `alert()` window for debugging. This is useful as DUIX is designed for development on mobile in mind, where the browser console is not available.
  - `G0 sv:` saves the results of `ak:` as global variable `G0`, which will be read many times later while constructing a HTML table;
  - `body getn:` calls `getElementsByTagName()` to get `<body>`.
  - `0 i:` extracts the 0-th element from array returned by `getn:`
  - `div ce:` calls `createElement()` to create `<div>`
  - `row` calls Colon Definition Word `row`. This is called 3 times to make 3 rows in HTML table.
  - `3 ms:` merge HTML code for 3 rows into one string;
  - `table tn:` creates `<table> ... </table>`
  - `ih:` defines `.innerHTML` for `<div>`
  - `ac:` calls `appendChild()` to append `<div>` to end of `<body>`
- c. Definitions for `row` and `cell`:
```
: cell G0 gv: swap: i: th tn: ; 
: row 0 cell 1 cell 2 cell 3 ms: tr tn: ; 
```
- &mdash;
  - `row` definitions:
    - `0 cell` passes `0` to `cell`, etc.
    - `3 ms:` merges HTML code for 3 cells into one string;
    - `tr tn:` creates `<tr> ... </tr>`
  - `cell` definitions:
    - `G0 gv:` get global variable G0, i.e. keys of Graph query results;
    - `swap:` changes order of array and index, so that `i:` extracts the element from the array;
    - `th tn:` creates `<th> ... </tn>`
    

- http://localhost/2021/Phosway/d09/pup/phoshell.php?x
