import sys
import json
import os
from pathlib import Path
import webview
import platform

# Configuration file path
CONFIG_DIR = Path.home() / ".threads-app"
CONFIG_FILE = CONFIG_DIR / "window-config.json"

class ThreadsApp:
    def __init__(self):
        self.window = None
        self.config = self.load_config()
        
    def load_config(self):
        """Load window configuration from file"""
        default_config = {
            "width": 1024,
            "height": 768,
            "x": None,
            "y": None
        }
        
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            except:
                pass
                
        return default_config
    
    def save_config(self):
        """Save current window configuration"""
        if self.window:
            # Get current window position and size
            x, y = self.window.x, self.window.y
            width, height = self.window.width, self.window.height
            
            config = {
                "width": width,
                "height": height,
                "x": x,
                "y": y
            }
            
            # Ensure config directory exists
            CONFIG_DIR.mkdir(exist_ok=True)
            
            # Save configuration
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f)
    
    def on_closing(self):
        """Called when window is closing"""
        self.save_config()
        
    def run(self):
        """Create and run the application"""
        # Create window with saved configuration
        self.window = webview.create_window(
            'Threads',
            'https://www.threads.net',
            width=self.config['width'],
            height=self.config['height'],
            x=self.config['x'],
            y=self.config['y']
        )
        
        # Set up event handlers
        self.window.events.closing += self.on_closing
        
        # Configure storage persistence based on platform
        if platform.system() == 'Darwin':  # macOS
            # Use private mode = False to enable persistent storage
            webview.start(private_mode=False, storage_path=str(CONFIG_DIR))
        elif platform.system() == 'Windows':
            # Windows also supports storage path for Edge WebView2
            webview.start(private_mode=False, storage_path=str(CONFIG_DIR))
        else:
            # Linux and other platforms
            webview.start(private_mode=False)

if __name__ == '__main__':
    app = ThreadsApp()
    app.run()