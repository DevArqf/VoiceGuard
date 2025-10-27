"""
VoiceGuard GUI Application
Modern graphical interface for voice authentication system
"""

import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import Config
from src.gui_components import *
from src.gui_operations import GUIVoiceIDSystem

class VoiceGuardGUI:
    """Main GUI Application for VoiceGuard"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("VoiceGuard - AI Voice Authentication")
        self.root.geometry("900x700")
        self.root.configure(bg=Colors.BG_LIGHT)
        
        # Initialize voice system
        self.voice_system = GUIVoiceIDSystem()
        
        # Current view
        self.current_view = None
        
        # Setup UI
        self.setup_ui()
        
        # Check configuration and initialize
        self.check_config()
    
    def setup_ui(self):
        """Setup the main UI layout"""
        # Header
        self.create_header()
        
        # Main content area
        self.content_frame = tk.Frame(self.root, bg=Colors.BG_LIGHT)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Show home view by default
        self.show_home()
    
    def create_header(self):
        """Create the application header"""
        header = tk.Frame(self.root, bg=Colors.PRIMARY, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header,
            text="🛡️ VoiceGuard",
            font=Fonts.TITLE,
            bg=Colors.PRIMARY,
            fg="white"
        )
        title_label.pack(side="left", padx=20, pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(
            header,
            text="AI Voice Authentication System",
            font=Fonts.BODY,
            bg=Colors.PRIMARY,
            fg="white"
        )
        subtitle_label.place(x=20, y=50)
    
    def clear_content(self):
        """Clear the current content"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def check_config(self):
        """Check if configuration is valid"""
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == "your_openai_api_key_here":
            messagebox.showerror(
                "Configuration Error",
                "OpenAI API key not configured!\n\n"
                "Please create a .env file with your API key:\n"
                "OPENAI_API_KEY=sk-your-key-here"
            )
            self.show_config_error()
        else:
            self.initialize_system()
    
    def show_config_error(self):
        """Show configuration error view"""
        self.clear_content()
        
        error_card = Card(self.content_frame)
        error_card.pack(pady=50)
        
        error_label = tk.Label(
            error_card,
            text="⚠️ Configuration Error",
            font=Fonts.HEADING,
            bg=Colors.CARD_BG,
            fg=Colors.DANGER
        )
        error_label.pack(pady=20, padx=30)
        
        msg_label = tk.Label(
            error_card,
            text="OpenAI API key is not configured.\n\n"
                 "Please create a .env file in the application directory\n"
                 "with your OpenAI API key:\n\n"
                 "OPENAI_API_KEY=sk-your-key-here",
            font=Fonts.BODY_LARGE,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_DARK,
            justify="center"
        )
        msg_label.pack(pady=20, padx=30)
        
        retry_btn = StyledButton(
            error_card,
            text="Retry",
            command=self.check_config,
            style="primary"
        )
        retry_btn.pack(pady=(10, 30))
    
    def initialize_system(self):
        """Initialize the voice system"""
        self.clear_content()
        
        # Show loading screen
        loading_card = Card(self.content_frame)
        loading_card.pack(pady=100)
        
        loading_label = tk.Label(
            loading_card,
            text="Initializing VoiceGuard...",
            font=Fonts.HEADING,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_DARK
        )
        loading_label.pack(pady=30, padx=50)
        
        progress = ProgressFrame(loading_card)
        progress.show("Please wait...")
        
        def on_success(result):
            self.root.after(0, self.show_home)
        
        def on_error(error):
            self.root.after(0, lambda: messagebox.showerror("Initialization Error", str(error)))
            self.root.after(0, self.show_config_error)
        
        self.voice_system.initialize(on_success, on_error)
    
    def show_home(self):
        """Show the home screen with main menu"""
        self.clear_content()
        
        # Welcome message
        welcome_label = tk.Label(
            self.content_frame,
            text="Welcome to VoiceGuard",
            font=Fonts.HEADING,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_DARK
        )
        welcome_label.pack(pady=(20, 10))
        
        subtitle_label = tk.Label(
            self.content_frame,
            text="Select an action below to get started",
            font=Fonts.BODY,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_LIGHT
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Button grid
        button_frame = tk.Frame(self.content_frame, bg=Colors.BG_LIGHT)
        button_frame.pack(pady=20)
        
        # Row 1
        row1 = tk.Frame(button_frame, bg=Colors.BG_LIGHT)
        row1.pack(pady=10)
        
        StyledButton(
            row1,
            text="📝 Enroll New User",
            command=self.show_enroll_view,
            style="primary",
            width=25
        ).pack(side="left", padx=10)
        
        StyledButton(
            row1,
            text="🔍 Verify User",
            command=self.show_verify_view,
            style="primary",
            width=25
        ).pack(side="left", padx=10)
        
        # Row 2
        row2 = tk.Frame(button_frame, bg=Colors.BG_LIGHT)
        row2.pack(pady=10)
        
        StyledButton(
            row2,
            text="🎯 Identify Speaker",
            command=self.show_identify_view,
            style="primary",
            width=25
        ).pack(side="left", padx=10)
        
        StyledButton(
            row2,
            text="👥 Manage Users",
            command=self.show_users_view,
            style="primary",
            width=25
        ).pack(side="left", padx=10)
        
        # Row 3
        row3 = tk.Frame(button_frame, bg=Colors.BG_LIGHT)
        row3.pack(pady=10)
        
        StyledButton(
            row3,
            text="🎤 Test Microphone",
            command=self.test_microphone,
            style="secondary",
            width=25
        ).pack(side="left", padx=10)
        
        StyledButton(
            row3,
            text="📊 System Stats",
            command=self.show_stats_view,
            style="secondary",
            width=25
        ).pack(side="left", padx=10)
    
    def show_enroll_view(self):
        """Show user enrollment view"""
        self.clear_content()
        
        # Back button
        StyledButton(
            self.content_frame,
            text="← Back to Home",
            command=self.show_home,
            style="secondary",
            width=15
        ).pack(anchor="w", pady=(0, 20))
        
        # Enrollment form
        enroll_card = Card(self.content_frame, title="📝 Enroll New User")
        enroll_card.pack(fill="x", pady=10)
        
        form_frame = tk.Frame(enroll_card, bg=Colors.CARD_BG)
        form_frame.pack(fill="x", padx=30, pady=20)
        
        # Username field
        username_field = InputField(form_frame, "Username *", placeholder="Enter username")
        username_field.pack(fill="x", pady=10)
        
        # Full name field
        fullname_field = InputField(form_frame, "Full Name", placeholder="Enter full name (optional)")
        fullname_field.pack(fill="x", pady=10)
        
        # Email field
        email_field = InputField(form_frame, "Email", placeholder="Enter email (optional)")
        email_field.pack(fill="x", pady=10)
        
        # Status label
        status_label = StatusLabel(form_frame)
        status_label.pack(pady=10)
        
        # Progress bar
        progress = ProgressFrame(form_frame)
        
        # Enroll button
        def start_enrollment():
            username = username_field.get().strip()
            if not username:
                status_label.set_status("❌ Username is required!", "error")
                return
            
            full_name = fullname_field.get().strip()
            email = email_field.get().strip()
            
            # Disable button and show progress
            enroll_btn.config(state="disabled")
            progress.show("Recording voice samples... Please speak when prompted.")
            status_label.set_status("🎤 Starting enrollment... Follow console prompts for recording.", "info")
            
            def on_success(result):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: enroll_btn.config(state="normal"))
                if result:
                    self.root.after(0, lambda: status_label.set_status(f"✅ User '{username}' enrolled successfully!", "success"))
                    self.root.after(2000, self.show_home)
                else:
                    self.root.after(0, lambda: status_label.set_status("❌ Enrollment failed!", "error"))
            
            def on_error(error):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: enroll_btn.config(state="normal"))
                self.root.after(0, lambda: status_label.set_status(f"❌ Error: {error}", "error"))
            
            self.voice_system.enroll_user(username, full_name, email, on_success, on_error)
        
        enroll_btn = StyledButton(
            form_frame,
            text="Start Enrollment",
            command=start_enrollment,
            style="success",
            width=20
        )
        enroll_btn.pack(pady=20)
        
        # Info
        info_label = tk.Label(
            enroll_card,
            text="ℹ️ You will be prompted to record 3 voice samples.\nPlease speak clearly when recording.",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT,
            justify="center"
        )
        info_label.pack(pady=(0, 20))
    
    def show_verify_view(self):
        """Show user verification view"""
        self.clear_content()
        
        # Back button
        StyledButton(
            self.content_frame,
            text="← Back to Home",
            command=self.show_home,
            style="secondary",
            width=15
        ).pack(anchor="w", pady=(0, 20))
        
        # Verification form
        verify_card = Card(self.content_frame, title="🔍 Verify User Identity")
        verify_card.pack(fill="x", pady=10)
        
        form_frame = tk.Frame(verify_card, bg=Colors.CARD_BG)
        form_frame.pack(fill="x", padx=30, pady=20)
        
        # Username field
        username_field = InputField(form_frame, "Username *", placeholder="Enter username to verify")
        username_field.pack(fill="x", pady=10)
        
        # Status label
        status_label = StatusLabel(form_frame)
        status_label.pack(pady=10)
        
        # Progress bar
        progress = ProgressFrame(form_frame)
        
        # Verify button
        def start_verification():
            username = username_field.get().strip()
            if not username:
                status_label.set_status("❌ Username is required!", "error")
                return
            
            verify_btn.config(state="disabled")
            progress.show("Recording voice... Please speak when prompted.")
            status_label.set_status("🎤 Recording... Speak clearly into your microphone.", "info")
            
            def on_success(result):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: verify_btn.config(state="normal"))
                
                if result['success']:
                    confidence = result['confidence'] * 100
                    msg = f"✅ User '{result['username']}' verified! Confidence: {confidence:.1f}%"
                    if result.get('transcript'):
                        msg += f"\n📝 You said: \"{result['transcript']}\""
                    self.root.after(0, lambda: status_label.set_status(msg, "success"))
                else:
                    error_msg = result.get('error', 'Verification failed')
                    self.root.after(0, lambda: status_label.set_status(f"❌ {error_msg}", "error"))
            
            def on_error(error):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: verify_btn.config(state="normal"))
                self.root.after(0, lambda: status_label.set_status(f"❌ Error: {error}", "error"))
            
            self.voice_system.identify_user(username, on_success, on_error)
        
        verify_btn = StyledButton(
            form_frame,
            text="Start Verification",
            command=start_verification,
            style="success",
            width=20
        )
        verify_btn.pack(pady=20)
        
        # Info
        info_label = tk.Label(
            verify_card,
            text="ℹ️ Speak clearly when recording. The system will verify your voice\nagainst the stored profile.",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT,
            justify="center"
        )
        info_label.pack(pady=(0, 20))
    
    def show_identify_view(self):
        """Show unknown speaker identification view"""
        self.clear_content()
        
        # Back button
        StyledButton(
            self.content_frame,
            text="← Back to Home",
            command=self.show_home,
            style="secondary",
            width=15
        ).pack(anchor="w", pady=(0, 20))
        
        # Identification card
        identify_card = Card(self.content_frame, title="🎯 Identify Unknown Speaker")
        identify_card.pack(fill="x", pady=10)
        
        form_frame = tk.Frame(identify_card, bg=Colors.CARD_BG)
        form_frame.pack(fill="x", padx=30, pady=20)
        
        # Status label
        status_label = StatusLabel(form_frame)
        status_label.pack(pady=10)
        
        # Progress bar
        progress = ProgressFrame(form_frame)
        
        # Identify button
        def start_identification():
            identify_btn.config(state="disabled")
            progress.show("Recording voice... Please speak when prompted.")
            status_label.set_status("🎤 Recording... Speak clearly into your microphone.", "info")
            
            def on_success(result):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: identify_btn.config(state="normal"))
                
                if result['success']:
                    confidence = result['confidence'] * 100
                    username = result['username']
                    full_name = result.get('full_name', '')
                    name_str = f" ({full_name})" if full_name else ""
                    msg = f"✅ Speaker identified: {username}{name_str}\nConfidence: {confidence:.1f}%"
                    if result.get('transcript'):
                        msg += f"\n📝 Transcript: \"{result['transcript']}\""
                    self.root.after(0, lambda: status_label.set_status(msg, "success"))
                else:
                    error_msg = result.get('error', 'Could not identify speaker')
                    self.root.after(0, lambda: status_label.set_status(f"❌ {error_msg}", "error"))
            
            def on_error(error):
                self.root.after(0, lambda: progress.hide())
                self.root.after(0, lambda: identify_btn.config(state="normal"))
                self.root.after(0, lambda: status_label.set_status(f"❌ Error: {error}", "error"))
            
            self.voice_system.identify_user(None, on_success, on_error)
        
        identify_btn = StyledButton(
            form_frame,
            text="Start Identification",
            command=start_identification,
            style="primary",
            width=20
        )
        identify_btn.pack(pady=20)
        
        # Info
        info_label = tk.Label(
            identify_card,
            text="ℹ️ The system will attempt to identify who is speaking by comparing\nyour voice against all enrolled users.",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT,
            justify="center"
        )
        info_label.pack(pady=(0, 20))
    
    def show_users_view(self):
        """Show users management view"""
        self.clear_content()
        
        # Back button
        StyledButton(
            self.content_frame,
            text="← Back to Home",
            command=self.show_home,
            style="secondary",
            width=15
        ).pack(anchor="w", pady=(0, 20))
        
        # Users card
        users_card = Card(self.content_frame, title="👥 Manage Users")
        users_card.pack(fill="both", expand=True, pady=10)
        
        # Loading
        loading_label = tk.Label(
            users_card,
            text="Loading users...",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT
        )
        loading_label.pack(pady=20)
        
        def on_success(users):
            self.root.after(0, lambda: loading_label.destroy())
            
            if not users:
                no_users_label = tk.Label(
                    users_card,
                    text="No users enrolled in the system.",
                    font=Fonts.BODY_LARGE,
                    bg=Colors.CARD_BG,
                    fg=Colors.TEXT_LIGHT
                )
                no_users_label.pack(pady=50)
                return
            
            # Scrollable frame for users
            scroll_frame = ScrollableFrame(users_card)
            scroll_frame.pack(fill="both", expand=True, padx=15, pady=15)
            
            # Display users
            for user in users:
                user_card = UserCard(
                    scroll_frame.scrollable_frame,
                    user,
                    on_select=lambda u: self.show_user_detail(u)
                )
                user_card.pack(fill="x", pady=5)
        
        def on_error(error):
            self.root.after(0, lambda: loading_label.config(
                text=f"Error loading users: {error}",
                fg=Colors.DANGER
            ))
        
        self.voice_system.list_users(on_success, on_error)
    
    def show_user_detail(self, user_data):
        """Show detailed user information"""
        username = user_data['username']
        
        # Create a new window for details
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"User Details - {username}")
        detail_window.geometry("500x600")
        detail_window.configure(bg=Colors.BG_LIGHT)
        
        # Loading
        loading_label = tk.Label(
            detail_window,
            text="Loading user information...",
            font=Fonts.BODY,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_LIGHT
        )
        loading_label.pack(pady=50)
        
        def on_success(info):
            detail_window.after(0, lambda: loading_label.destroy())
            
            if not info:
                error_label = tk.Label(
                    detail_window,
                    text="User not found!",
                    font=Fonts.BODY_LARGE,
                    bg=Colors.BG_LIGHT,
                    fg=Colors.DANGER
                )
                error_label.pack(pady=50)
                return
            
            # User info card
            info_card = Card(detail_window)
            info_card.pack(fill="both", expand=True, padx=20, pady=20)
            
            # Header
            header_frame = tk.Frame(info_card, bg=Colors.CARD_BG)
            header_frame.pack(fill="x", padx=20, pady=20)
            
            icon_label = tk.Label(
                header_frame,
                text="👤",
                font=("Segoe UI", 40),
                bg=Colors.CARD_BG
            )
            icon_label.pack(pady=10)
            
            username_label = tk.Label(
                header_frame,
                text=info['user_info']['username'],
                font=Fonts.TITLE,
                bg=Colors.CARD_BG,
                fg=Colors.TEXT_DARK
            )
            username_label.pack()
            
            if info['user_info'].get('full_name'):
                name_label = tk.Label(
                    header_frame,
                    text=info['user_info']['full_name'],
                    font=Fonts.BODY_LARGE,
                    bg=Colors.CARD_BG,
                    fg=Colors.TEXT_LIGHT
                )
                name_label.pack(pady=5)
            
            # Details
            details_frame = tk.Frame(info_card, bg=Colors.CARD_BG)
            details_frame.pack(fill="x", padx=20, pady=10)
            
            details = [
                ("📧 Email", info['user_info'].get('email', 'N/A')),
                ("🆔 User ID", info['user_info']['user_id']),
                ("📅 Created", info['user_info']['created_at']),
                ("🎤 Voice Profiles", info['voice_profiles']),
                ("✅ Successful Auths", info['recent_authentications']),
                ("❌ Failed Attempts", info['failed_attempts']),
            ]
            
            for label, value in details:
                detail_row = tk.Frame(details_frame, bg=Colors.CARD_BG)
                detail_row.pack(fill="x", pady=5)
                
                tk.Label(
                    detail_row,
                    text=label,
                    font=Fonts.SUBHEADING,
                    bg=Colors.CARD_BG,
                    fg=Colors.TEXT_DARK,
                    anchor="w"
                ).pack(side="left")
                
                tk.Label(
                    detail_row,
                    text=str(value),
                    font=Fonts.BODY,
                    bg=Colors.CARD_BG,
                    fg=Colors.TEXT_LIGHT,
                    anchor="e"
                ).pack(side="right")
            
            # Actions
            actions_frame = tk.Frame(info_card, bg=Colors.CARD_BG)
            actions_frame.pack(pady=20)
            
            StyledButton(
                actions_frame,
                text="Delete User",
                command=lambda: self.delete_user_confirm(username, detail_window),
                style="danger",
                width=20
            ).pack()
        
        def on_error(error):
            detail_window.after(0, lambda: loading_label.config(
                text=f"Error: {error}",
                fg=Colors.DANGER
            ))
        
        self.voice_system.get_user_info(username, on_success, on_error)
    
    def delete_user_confirm(self, username, parent_window):
        """Confirm and delete user"""
        result = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete user '{username}'?\n\n"
            "This will remove all voice profiles and cannot be undone.",
            parent=parent_window
        )
        
        if result:
            def on_success(deleted):
                if deleted:
                    parent_window.after(0, lambda: messagebox.showinfo(
                        "Success",
                        f"User '{username}' has been deleted.",
                        parent=parent_window
                    ))
                    parent_window.after(0, parent_window.destroy)
                    self.root.after(0, self.show_users_view)
                else:
                    parent_window.after(0, lambda: messagebox.showerror(
                        "Error",
                        f"Failed to delete user '{username}'.",
                        parent=parent_window
                    ))
            
            def on_error(error):
                parent_window.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Error deleting user: {error}",
                    parent=parent_window
                ))
            
            self.voice_system.delete_user(username, on_success, on_error)
    
    def test_microphone(self):
        """Test microphone"""
        result = messagebox.showinfo(
            "Microphone Test",
            "The microphone test will start.\n\n"
            "Follow the prompts in the console window to test your microphone.",
            parent=self.root
        )
        
        def on_success(result):
            self.root.after(0, lambda: messagebox.showinfo(
                "Success",
                "Microphone test completed successfully!",
                parent=self.root
            ))
        
        def on_error(error):
            self.root.after(0, lambda: messagebox.showerror(
                "Error",
                f"Microphone test failed: {error}",
                parent=self.root
            ))
        
        self.voice_system.test_microphone(on_success, on_error)
    
    def show_stats_view(self):
        """Show system statistics"""
        self.clear_content()
        
        # Back button
        StyledButton(
            self.content_frame,
            text="← Back to Home",
            command=self.show_home,
            style="secondary",
            width=15
        ).pack(anchor="w", pady=(0, 20))
        
        # Stats card
        stats_card = Card(self.content_frame, title="📊 System Statistics")
        stats_card.pack(fill="x", pady=10)
        
        # Loading
        loading_label = tk.Label(
            stats_card,
            text="Loading statistics...",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT
        )
        loading_label.pack(pady=20)
        
        def on_success(stats):
            stats_card.after(0, lambda: loading_label.destroy())
            
            # Stats grid
            stats_frame = tk.Frame(stats_card, bg=Colors.CARD_BG)
            stats_frame.pack(padx=30, pady=20)
            
            stats_data = [
                ("👥 Total Users", stats['total_users'], Colors.PRIMARY),
                ("🔐 Total Authentications", stats['total_authentications'], Colors.INFO),
                ("✅ Successful", stats['successful_authentications'], Colors.SUCCESS),
                ("❌ Failed", stats['failed_authentications'], Colors.DANGER),
                ("📈 Success Rate", f"{stats['success_rate']:.1%}", Colors.PRIMARY),
            ]
            
            for i, (label, value, color) in enumerate(stats_data):
                row = i // 2
                col = i % 2
                
                stat_frame = tk.Frame(stats_frame, bg=Colors.CARD_BG)
                stat_frame.grid(row=row, column=col, padx=20, pady=15, sticky="w")
                
                value_label = tk.Label(
                    stat_frame,
                    text=str(value),
                    font=("Segoe UI", 28, "bold"),
                    bg=Colors.CARD_BG,
                    fg=color
                )
                value_label.pack()
                
                label_widget = tk.Label(
                    stat_frame,
                    text=label,
                    font=Fonts.BODY,
                    bg=Colors.CARD_BG,
                    fg=Colors.TEXT_LIGHT
                )
                label_widget.pack()
        
        def on_error(error):
            stats_card.after(0, lambda: loading_label.config(
                text=f"Error loading stats: {error}",
                fg=Colors.DANGER
            ))
        
        self.voice_system.get_system_stats(on_success, on_error)
    
    def on_closing(self):
        """Handle window closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit VoiceGuard?"):
            self.voice_system.cleanup()
            self.root.destroy()

def main():
    """Main entry point for GUI application"""
    root = tk.Tk()
    app = VoiceGuardGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
