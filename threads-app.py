import json
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
                    config = json.load(f)
                    # Validate that config contains expected keys with appropriate types
                    if not isinstance(config, dict):
                        return default_config
                    # Ensure width and height are positive integers
                    if 'width' in config and isinstance(config['width'], int) and config['width'] > 0:
                        default_config['width'] = config['width']
                    if 'height' in config and isinstance(config['height'], int) and config['height'] > 0:
                        default_config['height'] = config['height']
                    # x and y can be None or integers
                    if 'x' in config and (config['x'] is None or isinstance(config['x'], int)):
                        default_config['x'] = config['x']
                    if 'y' in config and (config['y'] is None or isinstance(config['y'], int)):
                        default_config['y'] = config['y']
                    return default_config
            except (json.JSONDecodeError, IOError, OSError) as e:
                # Log error but continue with defaults - don't crash the app
                print(f"Warning: Could not load config file: {e}")
                
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
            
            # Ensure config directory exists with proper permissions
            CONFIG_DIR.mkdir(mode=0o755, exist_ok=True)
            
            # Save configuration with formatting for readability
            try:
                with open(CONFIG_FILE, 'w') as f:
                    json.dump(config, f, indent=2)
            except (IOError, OSError) as e:
                print(f"Warning: Could not save config file: {e}")
    
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