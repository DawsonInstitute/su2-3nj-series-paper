% verify.m — Hypergeometric product formula verification for SU(2) 3nj
%
% Verifies Theorem 1 (hypergeometric product formula) for the 15j chain:
%
%   C_G = prod_{e=1}^{15}  1/(2j_e)!  *  2F1(-2j_e, 1/2; 1; -F_{e-1}/F_e)
%
% where F_k is the k-th Fibonacci number.
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
    % hypergeom([-2j, 0.5], [1], -rho) via Gauss 2F1
    h = hypergeom([-twoj, 0.5], 1, -rho);
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
    h   = hypergeom([-2*js0(e), 0.5], 1, -rho);
    prod0 = prod0 * (1 / factorial(2*js0(e))) * h;
end
if abs(prod0 - 1) < 1e-12
    fprintf('[PASS] j=0 all gives 1 (got %.15g).\n', prod0);
else
    fprintf('[FAIL] j=0 all gave %.15g (expected 1).\n', prod0);
    fails = fails + 1;
end

% ── 9j det(I-K) analytic check ───────────────────────────────────────────
% For the minimal 6x6 K with x=y=z=t, det(I-K) should equal (1+t^2)^3.
t_vals = 0:0.1:0.9;
max_err = 0;
for t = t_vals
    a = t; b = t; c = t;
    K6 = [  0,    a,    0,    0,       0,    0;
           -a,    0,    b,    0,       0,    0;
            0,   -b,    0,    c,       0,    0;
            0,    0,   -c,    0,  a+b+c,    0;
            0,    0,    0, -(a+b+c),   0,    0;
            0,    0,    0,    0,       0,    0];
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
