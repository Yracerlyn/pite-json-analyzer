#!/usr/bin/env python3
"""
Pre-push verification script
Run this before pushing to ensure CI will pass
"""

import subprocess
import sys

def run_command(cmd, description):
    """Run a command and report results."""
    print(f"\n{'='*60}")
    print(f"🔍 {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print(f"✅ {description} - PASSED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(e.stdout)
        print(e.stderr)
        return False

def main():
    """Run all pre-push checks."""
    print("\n" + "="*60)
    print("🚀 Pre-Push CI Verification")
    print("="*60)
    
    checks = [
        ("python -m pytest test/ -v", "Running unit tests"),
        ("python src/cli.py --help", "Testing CLI --help"),
        ("python src/cli.py --file data/sample.json", "Testing CLI with sample file"),
    ]
    
    results = []
    for cmd, desc in checks:
        results.append(run_command(cmd, desc))
    
    print("\n" + "="*60)
    print("📊 Summary")
    print("="*60)
    
    total = len(results)
    passed = sum(results)
    
    for i, (cmd, desc) in enumerate(checks):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"{status} - {desc}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All checks passed! Ready to push to GitHub.")
        print("Run: git push origin main")
        return 0
    else:
        print("\n⚠️  Some checks failed. Fix issues before pushing.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
