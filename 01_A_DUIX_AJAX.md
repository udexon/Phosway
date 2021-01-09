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
  - iii. `ON ECHO bv:` turn on `echo` (a nostalgic MSDOS convention!!)
  - iv. `je:` executes `json_encode()` on the results of `rn:`
  - v.  `ec:` sends TOS (top of stack) (`json_encode()` results) to front end, via Ajax.

- b. invokes `F_T` upon receiving Ajax results;

- http://localhost/2021/Phosway/d09/pup/phoshell.php?x
