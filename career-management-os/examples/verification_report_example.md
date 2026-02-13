# Verification Report Example

## Summary

| Verdict | Count | Percentage |
|---------|-------|------------|
| ✅ VERIFIED | 18 | 72% |
| ⚠️ MODIFIED | 4 | 16% |
| ❌ HALLUCINATED | 2 | 8% |
| 🔍 UNVERIFIABLE | 1 | 4% |

## Detail — Draft V1 (Impact-First)

| Line | Claim | Source | Verdict | Note |
|------|-------|--------|---------|------|
| 3 | "Led team of 8 engineers" | applicantinfo L42: "managed 8-person team" | ✅ | Exact match |
| 5 | "Reduced inference latency by 40%" | applicantinfo L58: "improved latency" | ❌ | No "40%" in source — rewrite to qualitative |
| 7 | "Implemented TensorRT integration" | applicantinfo L61: "TensorRT provider integration" | ⚠️ | Reworded, semantically same |
| 12 | "Saved $200K annually" | Not found in source | 🔍 | Plausible but unconfirmed — ask user |

## Corrected V1

Line 5 corrected:
- Before: "Reduced inference latency by 40%"
- After: "Significantly reduced inference latency through TensorRT optimization"
