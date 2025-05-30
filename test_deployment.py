#!/usr/bin/env python3
"""
Test script for AgenticSeek deployment
Tests basic functionality without audio packages
"""

import os
import sys
import requests
import json
from typing import Dict, Any

def test_imports():
    """Test that all required packages can be imported"""
    print("Testing imports...")
    
    try:
        # Core packages
        import fastapi
        import uvicorn
        import openai
        import selenium
        print("✅ Core packages imported successfully")
        
        # Optional audio packages
        try:
            import pyaudio
            import librosa
            import soundfile
            print("✅ Audio packages available")
        except ImportError:
            print("⚠️  Audio packages not available (expected in production)")
        
        # Test our modules
        from sources.browser import Browser
        from sources.utility import pretty_print
        print("✅ AgenticSeek modules imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_browser_setup():
    """Test browser setup with Chromium"""
    print("\nTesting browser setup...")
    
    try:
        from sources.browser import Browser
        
        # Test browser initialization
        browser = Browser(headless=True)
        print("✅ Browser initialized successfully")
        
        # Test basic navigation
        browser.goto("https://httpbin.org/get")
        title = browser.get_title()
        print(f"✅ Browser navigation successful, title: {title}")
        
        browser.quit()
        return True
    except Exception as e:
        print(f"❌ Browser test failed: {e}")
        return False

def test_api_server(base_url: str = "http://localhost:8000"):
    """Test API endpoints"""
    print(f"\nTesting API server at {base_url}...")
    
    try:
        # Test health endpoint
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health endpoint working")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
            return False
        
        # Test search endpoint (if available)
        search_data = {
            "query": "test search",
            "max_results": 1
        }
        
        response = requests.post(
            f"{base_url}/search", 
            json=search_data, 
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Search endpoint working")
        else:
            print(f"⚠️  Search endpoint returned: {response.status_code}")
        
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server")
        return False
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def test_openai_config():
    """Test OpenAI configuration"""
    print("\nTesting OpenAI configuration...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OPENAI_API_KEY not set")
        return False
    
    if api_key.startswith("sk-"):
        print("✅ OpenAI API key format looks correct")
        return True
    else:
        print("❌ OpenAI API key format incorrect")
        return False

def main():
    """Run all tests"""
    print("AgenticSeek Deployment Test")
    print("=" * 40)
    
    tests = [
        ("Package Imports", test_imports),
        ("Browser Setup", test_browser_setup),
        ("OpenAI Config", test_openai_config),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    # Test API server if requested
    if len(sys.argv) > 1 and sys.argv[1] == "--test-api":
        base_url = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:8000"
        results["API Server"] = test_api_server(base_url)
    
    # Summary
    print("\n" + "=" * 40)
    print("Test Summary:")
    
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready for deployment.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the issues above.")
        return 1

if __name__ == "__main__":
    exit(main())