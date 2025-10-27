"""
GUI Components and Styling for VoiceGuard
Reusable UI components with consistent styling
"""

import tkinter as tk
from tkinter import ttk

# Color Scheme
class Colors:
    PRIMARY = "#2563eb"  # Blue
    PRIMARY_DARK = "#1e40af"
    SUCCESS = "#10b981"  # Green
    SUCCESS_DARK = "#059669"
    DANGER = "#ef4444"  # Red
    DANGER_DARK = "#dc2626"
    WARNING = "#f59e0b"  # Orange
    INFO = "#3b82f6"
    BG_DARK = "#1e293b"  # Dark blue-gray
    BG_LIGHT = "#f8fafc"
    CARD_BG = "#ffffff"
    TEXT_DARK = "#0f172a"
    TEXT_LIGHT = "#64748b"
    BORDER = "#e2e8f0"

# Fonts
class Fonts:
    TITLE = ("Segoe UI", 24, "bold")
    HEADING = ("Segoe UI", 16, "bold")
    SUBHEADING = ("Segoe UI", 12, "bold")
    BODY = ("Segoe UI", 10)
    BODY_LARGE = ("Segoe UI", 11)
    BUTTON = ("Segoe UI", 10, "bold")
    MONO = ("Consolas", 9)

class StyledButton(tk.Button):
    """Custom styled button with hover effects"""
    
    def __init__(self, parent, text, command=None, style="primary", width=20, **kwargs):
        # Set colors based on style
        if style == "primary":
            bg = Colors.PRIMARY
            hover_bg = Colors.PRIMARY_DARK
            fg = "white"
        elif style == "success":
            bg = Colors.SUCCESS
            hover_bg = Colors.SUCCESS_DARK
            fg = "white"
        elif style == "danger":
            bg = Colors.DANGER
            hover_bg = Colors.DANGER_DARK
            fg = "white"
        elif style == "secondary":
            bg = Colors.BG_LIGHT
            hover_bg = Colors.BORDER
            fg = Colors.TEXT_DARK
        else:
            bg = Colors.PRIMARY
            hover_bg = Colors.PRIMARY_DARK
            fg = "white"
        
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            font=Fonts.BUTTON,
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            width=width,
            **kwargs
        )
        
        self.default_bg = bg
        self.hover_bg = hover_bg
        
        # Bind hover events
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        self.config(bg=self.hover_bg)
    
    def _on_leave(self, event):
        self.config(bg=self.default_bg)

class Card(tk.Frame):
    """Card container for grouping related content"""
    
    def __init__(self, parent, title=None, **kwargs):
        super().__init__(
            parent,
            bg=Colors.CARD_BG,
            relief="flat",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=Colors.BORDER,
            **kwargs
        )
        
        if title:
            title_label = tk.Label(
                self,
                text=title,
                font=Fonts.HEADING,
                bg=Colors.CARD_BG,
                fg=Colors.TEXT_DARK
            )
            title_label.pack(pady=(15, 10), padx=15, anchor="w")

class StatusLabel(tk.Label):
    """Label for displaying status messages with color coding"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="",
            font=Fonts.BODY_LARGE,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_LIGHT,
            wraplength=500,
            justify="left",
            **kwargs
        )
    
    def set_status(self, message, status_type="info"):
        """Set status message with appropriate color"""
        self.config(text=message)
        
        if status_type == "success":
            self.config(fg=Colors.SUCCESS)
        elif status_type == "error":
            self.config(fg=Colors.DANGER)
        elif status_type == "warning":
            self.config(fg=Colors.WARNING)
        elif status_type == "info":
            self.config(fg=Colors.INFO)
        else:
            self.config(fg=Colors.TEXT_LIGHT)
    
    def clear(self):
        """Clear the status message"""
        self.config(text="", fg=Colors.TEXT_LIGHT)

class ProgressFrame(tk.Frame):
    """Frame for showing progress with a progress bar"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=Colors.BG_LIGHT, **kwargs)
        
        self.progress_label = tk.Label(
            self,
            text="",
            font=Fonts.BODY,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_DARK
        )
        self.progress_label.pack(pady=(0, 5))
        
        self.progress_bar = ttk.Progressbar(
            self,
            mode='indeterminate',
            length=300
        )
        self.progress_bar.pack()
        
        self.hide()
    
    def show(self, message="Processing..."):
        """Show progress bar with message"""
        self.progress_label.config(text=message)
        self.progress_bar.start(10)
        self.pack(pady=10)
    
    def hide(self):
        """Hide progress bar"""
        self.progress_bar.stop()
        self.pack_forget()

class InputField(tk.Frame):
    """Labeled input field"""
    
    def __init__(self, parent, label, placeholder="", **kwargs):
        super().__init__(parent, bg=Colors.BG_LIGHT)
        
        # Label
        label_widget = tk.Label(
            self,
            text=label,
            font=Fonts.SUBHEADING,
            bg=Colors.BG_LIGHT,
            fg=Colors.TEXT_DARK
        )
        label_widget.pack(anchor="w", pady=(0, 5))
        
        # Entry
        self.entry = tk.Entry(
            self,
            font=Fonts.BODY_LARGE,
            relief="solid",
            borderwidth=1,
            **kwargs
        )
        self.entry.pack(fill="x", ipady=5)
        
        # Placeholder
        if placeholder:
            self.entry.insert(0, placeholder)
            self.entry.config(fg=Colors.TEXT_LIGHT)
            self.entry.bind("<FocusIn>", self._on_focus_in)
            self.entry.bind("<FocusOut>", self._on_focus_out)
            self.placeholder = placeholder
    
    def _on_focus_in(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=Colors.TEXT_DARK)
    
    def _on_focus_out(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg=Colors.TEXT_LIGHT)
    
    def get(self):
        """Get entry value"""
        value = self.entry.get()
        return value if value != getattr(self, 'placeholder', '') else ''
    
    def set(self, value):
        """Set entry value"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
        self.entry.config(fg=Colors.TEXT_DARK)
    
    def clear(self):
        """Clear entry"""
        self.entry.delete(0, tk.END)

class ScrollableFrame(tk.Frame):
    """Scrollable frame for long content"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self, bg=Colors.BG_LIGHT, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # Create frame inside canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg=Colors.BG_LIGHT)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mouse wheel binding
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class UserCard(Card):
    """Card for displaying user information"""
    
    def __init__(self, parent, user_data, on_select=None):
        super().__init__(parent)
        
        # User icon and name
        header = tk.Frame(self, bg=Colors.CARD_BG)
        header.pack(fill="x", padx=15, pady=10)
        
        icon_label = tk.Label(
            header,
            text="👤",
            font=("Segoe UI", 20),
            bg=Colors.CARD_BG
        )
        icon_label.pack(side="left", padx=(0, 10))
        
        info_frame = tk.Frame(header, bg=Colors.CARD_BG)
        info_frame.pack(side="left", fill="x", expand=True)
        
        username_label = tk.Label(
            info_frame,
            text=user_data.get('username', 'Unknown'),
            font=Fonts.HEADING,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_DARK,
            anchor="w"
        )
        username_label.pack(anchor="w")
        
        if user_data.get('full_name'):
            name_label = tk.Label(
                info_frame,
                text=user_data['full_name'],
                font=Fonts.BODY,
                bg=Colors.CARD_BG,
                fg=Colors.TEXT_LIGHT,
                anchor="w"
            )
            name_label.pack(anchor="w")
        
        # Stats
        stats_frame = tk.Frame(self, bg=Colors.CARD_BG)
        stats_frame.pack(fill="x", padx=15, pady=(0, 10))
        
        profiles_label = tk.Label(
            stats_frame,
            text=f"🎤 Profiles: {user_data.get('enrollment_count', 0)}",
            font=Fonts.BODY,
            bg=Colors.CARD_BG,
            fg=Colors.TEXT_LIGHT
        )
        profiles_label.pack(side="left", padx=(0, 15))
        
        if user_data.get('created_at'):
            date_label = tk.Label(
                stats_frame,
                text=f"📅 {user_data['created_at'][:10]}",
                font=Fonts.BODY,
                bg=Colors.CARD_BG,
                fg=Colors.TEXT_LIGHT
            )
            date_label.pack(side="left")
        
        # Select button if callback provided
        if on_select:
            select_btn = StyledButton(
                self,
                text="Select",
                command=lambda: on_select(user_data),
                style="primary",
                width=15
            )
            select_btn.pack(pady=(0, 10))
