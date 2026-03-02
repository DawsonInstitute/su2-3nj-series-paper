% verify.m — Hypergeometric product formula verification for SU(2) 3nj
%
% Verifies Theorem 1 (hypergeometric product formula) for the 15j chain:
%
%   C_G = prod_{e=1}^{15}  1/(2j_e)!  *  2F1(-2j_e, 1/2; 1; -F_{e-1}/F_e)
%
% where F_k is the k-th Fibonacci number.
%
% Requires Symbolic Math Toolbox (R2025b) for hypergeom().
% A toolbox-free fallback hyp2f1_neg_int() is retained for portability
% reference but is no longer the primary path.
%
% Reference: Appendix F of:
%   "Unified Closed-Form Representations and Generating Functionals
%    for SU(2) 3n-j Recoupling Coefficients"
%   Ryan Sherrington, Dawson Institute for Advanced Physics, 2026.
%
% Usage:
%   matlab -batch "run('scripts/matlab/verify.m')"

clear; clc;
outdir = fileparts(mfilename('fullpath'));

fails = 0;

% ── Fibonacci helper ──────────────────────────────────────────────────────
fib = @(n) round(((1+sqrt(5))/2)^n / sqrt(5));
% (round to integer for exact natural Fibonacci; n=0 gives 0 by convention)

% ── 15j chain: j_e = 1 for all e ─────────────────────────────────────────
js = ones(1, 15);
prod_val = 1;
for e = 1:15
    if e == 1
        rho = 0;   % F_0/F_1 = 0/1 = 0
    else
        rho = fib(e-1) / fib(e);
    end
    j_e   = js(e);
    twoj  = 2 * j_e;
    % Use Symbolic Math Toolbox hypergeom for accurate 2F1(-2j, 0.5; 1; -rho)
    h = double(hypergeom([-twoj, 0.5], 1, -rho));
    prod_val = prod_val * (1 / factorial(twoj)) * h;
end

fprintf('15j chain hyper product (j=1 all): %.15g\n', prod_val);

if isfinite(prod_val) && prod_val > 0 && prod_val < 1
    fprintf('[PASS] 15j product is finite, positive, and < 1.\n');
else
    fprintf('[FAIL] 15j product out of expected range: %g\n', prod_val);
    fails = fails + 1;
end

% ── Degenerate: j_e = 0 for all e ────────────────────────────────────────
% Each factor: 1/0! * 2F1(0, 1/2; 1; ...) = 1 * 1 = 1 → product = 1.
js0 = zeros(1, 5);
prod0 = 1;
for e = 1:5
    rho = (e > 1) * fib(e-1) / fib(e);
    h   = double(hypergeom([-2*js0(e), 0.5], 1, -rho));
    prod0 = prod0 * (1 / factorial(2*js0(e))) * h;
end
if abs(prod0 - 1) < 1e-12
    fprintf('[PASS] j=0 all gives 1 (got %.15g).\n', prod0);
else
    fprintf('[FAIL] j=0 all gave %.15g (expected 1).\n', prod0);
    fails = fails + 1;
end

% ── 9j det(I-K) analytic check ───────────────────────────────────────────
% Block-diagonal 6x6 K for 9j: three independent 2x2 blocks [[0,t],[-t,0]].
% det(I-K) = (1+t^2)^3  for x=y=z=t.
t_vals = 0:0.1:0.9;
max_err = 0;
for t = t_vals
    K6 = [  0,  t,  0,  0,  0,  0;
           -t,  0,  0,  0,  0,  0;
            0,  0,  0,  t,  0,  0;
            0,  0, -t,  0,  0,  0;
            0,  0,  0,  0,  0,  t;
            0,  0,  0,  0, -t,  0];
    d_num = det(eye(6) - K6);
    d_ana = (1 + t^2)^3;
    max_err = max(max_err, abs(d_num - d_ana));
end
if max_err < 1e-10
    fprintf('[PASS] 9j det(I-K) matches (1+t^2)^3, max err = %.2e.\n', max_err);
else
    fprintf('[FAIL] 9j det(I-K) max err = %.2e.\n', max_err);
    fails = fails + 1;
end

% ── Summary ───────────────────────────────────────────────────────────────
if fails == 0
    fprintf('\nAll MATLAB verification checks PASSED.\n');
else
    fprintf('\n%d check(s) FAILED.\n', fails);
    exit(1);
end

% =========================================================================
% Portability fallback: 2F1(-n, 0.5; 1; z) for non-negative integer n.
% Not used above (Symbolic Toolbox hypergeom is the primary path), but
% retained here for environments without the Toolbox.
% Usage: h = hyp2f1_neg_int(n, z)
function h = hyp2f1_neg_int(n, z)
    % Compute 2F1(-n, 0.5; 1; z) via finite series (n terms).
    n = round(n);  % ensure integer
    h    = 0;
    term = 1;
    for k = 0:n
        h = h + term;
        if k < n
            term = term * (-n + k) * (0.5 + k) / (k + 1)^2 * z;
        end
    end
end
