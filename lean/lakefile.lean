import Lake
open Lake DSL

package su2ThreenjFormulas where
  -- matching Mathlib version used in aqei-bridge

-- Use local Mathlib from aqei-bridge to avoid re-downloading (same v4.27.0)
require mathlib from
  "/home/echo_/Code/asciimath/aqei-bridge/lean/.lake/packages/mathlib"

@[default_target]
lean_lib SU2ThreenjFormulas where
  srcDir := "src"
