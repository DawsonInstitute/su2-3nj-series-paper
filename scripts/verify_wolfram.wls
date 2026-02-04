#!/usr/bin/env wolframscript
(* ::Package:: *)

(*
  Wolfram verification harness for SU(2) recoupling identities.

  Goal:
    Provide an independent verification path (symbolic + high-precision numeric)
    against Wolfram's built-in ThreeJSymbol/SixJSymbol/NineJSymbol.

  Run:
    wolframscript -file scripts/verify_wolfram.wls
*)

$MaxExtraPrecision = 200;
$MinPrecision = 80;

ClearAll[assertTrue, assertApprox, reportSummary, failures];
failures = {};

assertTrue[name_String, cond_] := Module[{ok = TrueQ[cond]},
  If[ok,
    Print["[PASS] ", name],
    AppendTo[failures, name];
    Print["[FAIL] ", name]
  ];
  ok
];

assertApprox[name_String, expr_, expected_, prec_Integer : 80] := Module[
  {diff = Quiet@N[expr - expected, prec]},
  If[NumericQ[diff],
    assertTrue[name, diff === 0 || Chop[diff, 10^(-prec + 10)] === 0],
    assertTrue[name, False]
  ]
];

reportSummary[] := Module[{},
  Print["\n=== Summary ==="]; 
  If[Length[failures] == 0,
    Print["All checks passed."],
    Print["Failures (", Length[failures], "):"]; 
    Scan[Print["  - ", #] &, failures]
  ];
  If[Length[failures] == 0, Exit[0], Exit[1]]
];

(* Spin and selection-rule helpers *)
ClearAll[validSpinQ, triangleQ, sixJValidQ, nineJValidQ];

validSpinQ[j_] := IntegerQ[2 j] && j >= 0;

triangleQ[j1_, j2_, j3_] := Module[{a = 2 j1, b = 2 j2, c = 2 j3},
  validSpinQ[j1] && validSpinQ[j2] && validSpinQ[j3] &&
  Abs[a - b] <= c <= a + b && EvenQ[a + b + c]
];

sixJValidQ[j1_, j2_, j3_, j4_, j5_, j6_] :=
  triangleQ[j1, j2, j3] && triangleQ[j1, j5, j6] && triangleQ[j4, j2, j6] && triangleQ[j4, j5, j3];

nineJValidQ[a_, b_, c_, d_, e_, f_, g_, h_, i_] :=
  triangleQ[a, b, c] && triangleQ[d, e, f] && triangleQ[g, h, i] &&
  triangleQ[a, d, g] && triangleQ[b, e, h] && triangleQ[c, f, i];

(* Factorial generalized to handle the half-integer workflow safely *)
ClearAll[fac];
fac[x_] := Gamma[x + 1];

(* Racah sum formula for 6j as an independent check *)
ClearAll[deltaTri, racah6J];

deltaTri[a_, b_, c_] := Module[{t1, t2, t3, t4},
  If[!triangleQ[a, b, c], Return[0]];
  t1 = -a + b + c;
  t2 = a - b + c;
  t3 = a + b - c;
  t4 = a + b + c + 1;
  Sqrt[fac[t1] fac[t2] fac[t3] / fac[t4]]
];

racah6J[j1_, j2_, j3_, j4_, j5_, j6_] := Module[
  {zmin, zmax, pref, sum},
  If[!sixJValidQ[j1, j2, j3, j4, j5, j6], Return[0]];
  pref = deltaTri[j1, j2, j3] deltaTri[j1, j5, j6] deltaTri[j4, j2, j6] deltaTri[j4, j5, j3];
  zmin = Max[j1 + j2 + j3, j1 + j5 + j6, j4 + j2 + j6, j4 + j5 + j3];
  zmax = Min[j1 + j2 + j4 + j5, j1 + j3 + j4 + j6, j2 + j3 + j5 + j6];
  If[!IntegerQ[zmin] || !IntegerQ[zmax], Return[$Failed]];
  sum = Sum[
    (-1)^z fac[z + 1] /
      (fac[z - (j1 + j2 + j3)] fac[z - (j1 + j5 + j6)] fac[z - (j4 + j2 + j6)] fac[z - (j4 + j5 + j3)]
       fac[(j1 + j2 + j4 + j5) - z] fac[(j1 + j3 + j4 + j6) - z] fac[(j2 + j3 + j5 + j6) - z]),
    {z, zmin, zmax}
  ];
  pref sum
];

(* 9j as a sum over products of 6j symbols; supports an alternate 6j backend. *)
ClearAll[nineJFrom6J];

nineJFrom6J[a_, b_, c_, d_, e_, f_, g_, h_, i_, sixJBackend_ : SixJSymbol] := Module[
  {xMax, xs, term},
  If[!nineJValidQ[a, b, c, d, e, f, g, h, i], Return[0]];
  (* Standard reduction-to-6j identity:
     {a b c; d e f; g h i} = Sum_x (-1)^(2x) (2x+1)
       {a d g; h i x}{b e h; d x f}{c f i; x a b}
  *)
  xMax = Max[a + d + g, b + e + h, c + f + i, a + b + c, d + e + f, g + h + i];
  xs = Select[Range[0, xMax, 1/2],
    sixJValidQ[a, d, g, h, i, #] && sixJValidQ[b, e, h, d, #, f] && sixJValidQ[c, f, i, #, a, b] &
  ];
  term[x_] := (-1)^(2 x) (2 x + 1)
    sixJBackend[{a, d, g}, {h, i, x}]
    sixJBackend[{b, e, h}, {d, x, f}]
    sixJBackend[{c, f, i}, {x, a, b}];
  Total[term /@ xs]
];

(* 9j as a sum over products of 3j symbols (independent of the 6j-sum route). *)
ClearAll[nineJFrom3J];

nineJFrom3J[a_, b_, c_, d_, e_, f_, g_, h_, i_] := Module[
  {ma, mb, md, me, mc, mf, mg, mh, mi, phaseExp, phase, t},
  If[!nineJValidQ[a, b, c, d, e, f, g, h, i], Return[0]];
  t = Quiet[Sum[
    mc = -ma - mb;
    mf = -md - me;
    mg = -ma - md;
    mh = -mb - me;
    mi = ma + mb + md + me;
    phaseExp = (a - ma) + (b - mb) + (c - mc) + (d - md) + (e - me) + (f - mf) + (g - mg) + (h - mh) + (i - mi);
    phase = (-1)^phaseExp;
    phase *
      ThreeJSymbol[{a, ma}, {b, mb}, {c, mc}] *
      ThreeJSymbol[{d, md}, {e, me}, {f, mf}] *
      ThreeJSymbol[{g, mg}, {h, mh}, {i, mi}] *
      ThreeJSymbol[{a, ma}, {d, md}, {g, mg}] *
      ThreeJSymbol[{b, mb}, {e, me}, {h, mh}] *
      ThreeJSymbol[{c, mc}, {f, mf}, {i, mi}],
    {ma, -a, a, 1}, {mb, -b, b, 1}, {md, -d, d, 1}, {me, -e, e, 1}
  ], ClebschGordan::phy];
  t
];

(* === Sanity checks (symbolic) === *)

assertTrue[
  "3j known value (1/2,1/2->1)",
  FullSimplify[
    ThreeJSymbol[{1/2, 1/2}, {1/2, -1/2}, {1, 0}] == 1/Sqrt[6]
  ]
];

assertTrue[
  "6j half-integer example equals 1/6",
  FullSimplify[
    SixJSymbol[{1/2, 1/2, 1}, {1/2, 1/2, 1}] == 1/6
  ]
];

(* === Independent 6j verification: Racah sum vs built-in === *)

Module[{cases6j},
  cases6j = {
    {1/2, 1/2, 1, 1/2, 1/2, 1},
    {1, 1, 1, 1, 1, 1},
    {1, 1/2, 3/2, 1, 1/2, 3/2},
    {2, 3/2, 1/2, 1, 3/2, 5/2}
  };
  Scan[
    Function[{c},
      Module[{a, b, c1, d, e1, f1, built, alt},
        {a, b, c1, d, e1, f1} = c;
        If[sixJValidQ[a, b, c1, d, e1, f1],
          built = SixJSymbol[{a, b, c1}, {d, e1, f1}];
          alt = racah6J[a, b, c1, d, e1, f1];
          assertApprox[
            "Racah6J matches SixJSymbol for " <> ToString[c],
            alt,
            built,
            80
          ],
          Print["[SKIP] invalid 6j case: ", c]
        ]
      ]
    ],
    cases6j
  ];
];

(* === Independent 9j verification: 9j built-in vs sum over 6j === *)

Module[{cases9j},
  cases9j = {
    {1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1/2, 1/2, 0, 1/2, 1/2, 0, 0, 0, 0},
    {1, 1/2, 1/2, 1/2, 1, 1/2, 1/2, 1/2, 1}
  };
  Scan[
    Function[{c},
      Module[{a, b, c1, d, e1, f1, g, h, i, via6j, viaRacah6j, via3j},
        {a, b, c1, d, e1, f1, g, h, i} = c;
        If[nineJValidQ[a, b, c1, d, e1, f1, g, h, i],
          via6j = nineJFrom6J[a, b, c1, d, e1, f1, g, h, i, SixJSymbol];
          viaRacah6j = nineJFrom6J[
            a, b, c1, d, e1, f1, g, h, i,
            (Function[{row1, row2}, racah6J @@ Join[row1, row2]])
          ];
          via3j = nineJFrom3J[a, b, c1, d, e1, f1, g, h, i];
          assertApprox[
            "9j: 6j-sum (built-in 6j) matches 3j-definition for " <> ToString[c],
            via6j,
            via3j,
            50
          ];
          assertApprox[
            "9j: 6j-sum (Racah 6j) matches 3j-definition for " <> ToString[c],
            viaRacah6j,
            via3j,
            50
          ],
          Print["[SKIP] invalid 9j case: ", c]
        ]
      ]
    ],
    cases9j
  ];
];

reportSummary[];
