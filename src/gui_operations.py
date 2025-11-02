"""
GUI Operations Handler
Handles long-running voice operations in background threads to prevent UI freezing
"""

import threading
import queue
from typing import Callable, Optional
from .voice_id_system import VoiceIDSystem

class VoiceOperationThread(threading.Thread):
    """Thread for running voice operations in the background"""
    
    def __init__(self, operation: Callable, callback: Callable, error_callback: Callable, *args, **kwargs):
        super().__init__()
        self.operation = operation
        self.callback = callback
        self.error_callback = error_callback
        self.args = args
        self.kwargs = kwargs
        self.daemon = True
    
    def run(self):
        """Run the operation"""
        try:
            result = self.operation(*self.args, **self.kwargs)
            self.callback(result)
        except Exception as e:
            self.error_callback(str(e))

class GUIVoiceIDSystem:
    """Wrapper around VoiceIDSystem for GUI operations with threading support"""
    
    def __init__(self, status_callback: Optional[Callable] = None):
        """
        Initialize GUI Voice ID System
        
        Args:
            status_callback: Callback function for status updates
        """
        self.voice_system: Optional[VoiceIDSystem] = None
        self.status_callback = status_callback
        self._initialized = False
        
    def initialize(self, success_callback: Callable, error_callback: Callable):
        """Initialize the voice system in a background thread"""
        def _init():
            try:
                self.voice_system = VoiceIDSystem()
                self._initialized = True
                return True
            except Exception as e:
                raise e
        
        thread = VoiceOperationThread(_init, success_callback, error_callback)
        thread.start()
    
    def is_initialized(self) -> bool:
        """Check if the system is initialized"""
        return self._initialized
    
    def enroll_user(self, username: str, full_name: str, email: str, 
                    success_callback: Callable, error_callback: Callable,
                    progress_callback: Optional[Callable] = None):
        """
        Enroll a new user in a background thread
        
        Args:
            username: Username for enrollment
            full_name: Full name
            email: Email address
            success_callback: Called on success with result
            error_callback: Called on error with error message
            progress_callback: Called with progress updates (sample number)
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _enroll():
            # Create a modified version that sends progress updates
            original_enroll = self.voice_system.enroll_user
            result = original_enroll(username, full_name, email)
            return result
        
        thread = VoiceOperationThread(_enroll, success_callback, error_callback)
        thread.start()
    
    def identify_user(self, username_hint: Optional[str], 
                     success_callback: Callable, error_callback: Callable):
        """
        Identify a user by voice in a background thread
        
        Args:
            username_hint: Optional username hint
            success_callback: Called on success with result dict
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _identify():
            return self.voice_system.identify_user(username_hint=username_hint)
        
        thread = VoiceOperationThread(_identify, success_callback, error_callback)
        thread.start()
    
    def list_users(self, success_callback: Callable, error_callback: Callable):
        """
        List all users in a background thread
        
        Args:
            success_callback: Called with list of users
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _list():
            return self.voice_system.list_users()
        
        thread = VoiceOperationThread(_list, success_callback, error_callback)
        thread.start()
    
    def get_user_info(self, username: str, success_callback: Callable, error_callback: Callable):
        """
        Get user information in a background thread
        
        Args:
            username: Username to query
            success_callback: Called with user info dict
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _get_info():
            return self.voice_system.get_user_info(username)
        
        thread = VoiceOperationThread(_get_info, success_callback, error_callback)
        thread.start()
    
    def delete_user(self, username: str, success_callback: Callable, error_callback: Callable):
        """
        Delete a user in a background thread
        
        Args:
            username: Username to delete
            success_callback: Called on successful deletion
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _delete():
            return self.voice_system.delete_user(username, confirm=True)
        
        thread = VoiceOperationThread(_delete, success_callback, error_callback)
        thread.start()
    
    def test_microphone(self, success_callback: Callable, error_callback: Callable):
        """
        Test microphone in a background thread
        
        Args:
            success_callback: Called on success
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _test():
            self.voice_system.test_microphone()
            return True
        
        thread = VoiceOperationThread(_test, success_callback, error_callback)
        thread.start()
    
    def get_system_stats(self, success_callback: Callable, error_callback: Callable):
        """
        Get system statistics in a background thread
        
        Args:
            success_callback: Called with stats dict
            error_callback: Called on error with error message
        """
        if not self.voice_system:
            error_callback("Voice system not initialized")
            return
        
        def _stats():
            return self.voice_system.get_system_stats()
        
        thread = VoiceOperationThread(_stats, success_callback, error_callback)
        thread.start()
    
    def cleanup(self):
        """Cleanup resources"""
        if self.voice_system:
            try:
                self.voice_system.cleanup()
            except:
                pass
