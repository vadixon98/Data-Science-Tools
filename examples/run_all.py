"""
Run All Examples
================
Simple script to run all example scripts in sequence.
Useful for verifying everything works correctly.
"""

import subprocess
import sys
import os


def run_script(script_name):
    """Run a Python script and display results"""
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    
    if not os.path.exists(script_path):
        print(f"⚠️  Script not found: {script_name}")
        return False
    
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print(f"{'='*60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=False,
            text=True
        )
        if result.returncode == 0:
            print(f"\n✅ {script_name} completed successfully")
            return True
        else:
            print(f"\n❌ {script_name} failed with exit code {result.returncode}")
            return False
    except Exception as e:
        print(f"\n❌ Error running {script_name}: {e}")
        return False


def main():
    """Run all example scripts"""
    scripts = [
        'arithmetic_operations.py',
        'time_converter.py',
        'libraries_demo.py'  # This one requires dependencies
    ]
    
    print("\n" + "="*60)
    print("Running All Example Scripts")
    print("="*60)
    
    results = []
    for script in scripts:
        results.append(run_script(script))
    
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    
    successful = sum(results)
    total = len(results)
    
    print(f"\n✅ Successful: {successful}/{total}")
    print(f"❌ Failed: {total - successful}/{total}")
    
    if successful == total:
        print("\n🎉 All scripts ran successfully!")
    else:
        print("\n⚠️  Some scripts failed. Check the output above for details.")
        print("Note: libraries_demo.py requires pandas, numpy, and matplotlib.")
        print("Install with: pip install -r ../requirements.txt")


if __name__ == "__main__":
    main()

