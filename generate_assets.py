#!/usr/bin/env python3
"""
Professional Asset Generator for Play Store
Creates production-ready screenshots, icons, and graphics
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def create_directory():
    """Create assets directory structure."""
    directories = [
        "assets",
        "assets/screenshots",
        "assets/icons",
        "assets/graphics"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✅ Asset directories created")


def get_fonts():
    """Get fonts with fallback."""
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        font_title = font_large = font_medium = font_small = ImageFont.load_default()
    
    return font_title, font_large, font_medium, font_small


def draw_road_background(draw, width, height, line_color=(255, 255, 0)):
    """Draw animated road background."""
    # Road
    draw.rectangle([(0, 0), (width, height)], fill=(128, 128, 128))
    
    # Side lines
    draw.line([(0, 0), (0, height)], fill=(255, 255, 255), width=5)
    draw.line([(width-1, 0), (width-1, height)], fill=(255, 255, 255), width=5)
    
    # Center dashed line
    center_x = width // 2
    for y in range(0, height, 80):
        draw.line([(center_x, y), (center_x, y + 40)], fill=line_color, width=3)


def create_screenshot_1_menu():
    """Screenshot 1: Menu Screen (1080x1920)."""
    print("📸 Creating Menu Screen screenshot...")
    img = Image.new('RGB', (1080, 1920), color=(20, 20, 40))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Gradient background effect
    for i in range(1920):
        color = (20 + i//20, 20 + i//30, 40 + i//40)
        draw.line([(0, i), (1080, i)], fill=color)
    
    # Title with glow effect
    draw.text((540, 300), "RACING GAME", fill=(0, 200, 255), font=font_title, anchor="mm")
    draw.text((540, 302), "RACING GAME", fill=(0, 150, 200), font=font_title, anchor="mm")
    
    # Subtitle
    draw.text((540, 500), "Arcade Driving Challenge", fill=(255, 200, 0), font=font_large, anchor="mm")
    
    # High score section
    draw.rectangle([(150, 650), (930, 800)], outline=(0, 200, 255), width=3)
    draw.text((540, 725), "YOUR HIGH SCORE", fill=(0, 200, 255), font=font_medium, anchor="mm")
    
    # Score display
    draw.text((540, 900), "1500 POINTS", fill=(0, 255, 0), font=font_title, anchor="mm")
    
    # Play button
    button_box = [(250, 1100), (830, 1250)]
    draw.rectangle(button_box, fill=(0, 200, 255), outline=(255, 255, 255), width=4)
    draw.text((540, 1175), "TAP TO PLAY", fill=(255, 255, 255), font=font_large, anchor="mm")
    
    # Features section
    draw.text((540, 1400), "FEATURES:", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    features = ["✓ Smooth Controls", "✓ Dynamic Traffic", "✓ High Scores", "✓ User Profiles"]
    y = 1500
    for feature in features:
        draw.text((540, y), feature, fill=(0, 255, 200), font=font_small, anchor="mm")
        y += 90
    
    img.save("assets/screenshots/01_menu_screen.png")
    print("✅ Screenshot 1 saved: assets/screenshots/01_menu_screen.png")


def create_screenshot_2_gameplay():
    """Screenshot 2: Gameplay in Action (1080x1920)."""
    print("📸 Creating Gameplay screenshot...")
    img = Image.new('RGB', (1080, 1920))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Draw road background
    draw_road_background(draw, 1080, 1920)
    
    # Enemy cars (upper traffic)
    # Red car 1
    draw.rectangle([(150, 200), (320, 320)], fill=(255, 50, 50))
    draw.rectangle([(170, 220), (300, 280)], fill=(255, 200, 0))  # Window
    
    # Yellow car 2
    draw.rectangle([(730, 450), (900, 570)], fill=(255, 255, 0))
    draw.rectangle([(750, 470), (880, 530)], fill=(100, 100, 100))  # Window
    
    # Green car 3
    draw.rectangle([(300, 700), (470, 820)], fill=(100, 255, 100))
    draw.rectangle([(320, 720), (450, 780)], fill=(255, 200, 0))  # Window
    
    # Close call - red car near player
    draw.rectangle([(400, 900), (570, 1020)], fill=(255, 100, 100))
    draw.rectangle([(420, 920), (550, 980)], fill=(255, 200, 0))  # Window
    
    # Player car (blue) - center bottom
    draw.rectangle([(400, 1400), (680, 1600)], fill=(0, 100, 255))
    draw.rectangle([(430, 1430), (650, 1540)], fill=(255, 255, 100))  # Window
    draw.circle((450, 1620), 35, fill=(50, 50, 50))  # Left wheel
    draw.circle((630, 1620), 35, fill=(50, 50, 50))  # Right wheel
    
    # Score display (top)
    draw.rectangle([(50, 50), (400, 150)], fill=(0, 0, 0), outline=(0, 200, 255), width=3)
    draw.text((75, 75), "SCORE: 2850", fill=(0, 255, 0), font=font_large)
    
    draw.rectangle([(680, 50), (1030, 150)], fill=(0, 0, 0), outline=(255, 200, 0), width=3)
    draw.text((705, 75), "HIGH: 1500", fill=(255, 200, 0), font=font_large)
    
    # Action indicator
    draw.rectangle([(200, 1750), (880, 1850)], fill=(0, 100, 50), outline=(0, 255, 100), width=3)
    draw.text((540, 1800), "DODGE TRAFFIC • SURVIVE LONGER", fill=(0, 255, 100), font=font_medium, anchor="mm")
    
    img.save("assets/screenshots/02_gameplay_action.png")
    print("✅ Screenshot 2 saved: assets/screenshots/02_gameplay_action.png")


def create_screenshot_3_gameover():
    """Screenshot 3: Game Over Screen (1080x1920)."""
    print("📸 Creating Game Over screenshot...")
    img = Image.new('RGB', (1080, 1920), color=(30, 20, 20))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Dark background
    draw.rectangle([(0, 0), (1080, 1920)], fill=(30, 20, 20))
    
    # Collision effect (explosion-like)
    draw.ellipse([(300, 600), (780, 900)], fill=(255, 100, 50), outline=(255, 200, 0), width=5)
    
    # Game Over text with red glow
    draw.text((540, 400), "GAME OVER!", fill=(255, 50, 50), font=font_title, anchor="mm")
    draw.text((542, 402), "GAME OVER!", fill=(255, 100, 100), font=font_title, anchor="mm")
    
    # Final score section
    draw.rectangle([(150, 700), (930, 900)], fill=(50, 50, 100), outline=(255, 100, 255), width=4)
    draw.text((540, 760), "FINAL SCORE", fill=(255, 100, 255), font=font_medium, anchor="mm")
    draw.text((540, 860), "3850 POINTS", fill=(0, 255, 0), font=font_large, anchor="mm")
    
    # High score comparison
    draw.text((540, 1050), "YOUR HIGH SCORE: 3850 ⭐", fill=(255, 215, 0), font=font_large, anchor="mm")
    
    # Stats
    stats_y = 1200
    draw.text((540, stats_y), "Distance: 38.5 KM", fill=(100, 200, 255), font=font_medium, anchor="mm")
    draw.text((540, stats_y + 100), "Survival Time: 3m 52s", fill=(100, 200, 255), font=font_medium, anchor="mm")
    draw.text((540, stats_y + 200), "Cars Dodged: 15", fill=(100, 200, 255), font=font_medium, anchor="mm")
    
    # Restart button
    draw.rectangle([(250, 1550), (830, 1700)], fill=(0, 200, 100), outline=(255, 255, 255), width=4)
    draw.text((540, 1625), "TAP TO RESTART", fill=(255, 255, 255), font=font_large, anchor="mm")
    
    # Share prompt
    draw.text((540, 1820), "Share your score!", fill=(255, 150, 0), font=font_small, anchor="mm")
    
    img.save("assets/screenshots/03_game_over.png")
    print("✅ Screenshot 3 saved: assets/screenshots/03_game_over.png")


def create_screenshot_4_login():
    """Screenshot 4: Login Screen (1080x1920)."""
    print("📸 Creating Login Screen screenshot...")
    img = Image.new('RGB', (1080, 1920), color=(40, 40, 60))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Background with gradient
    for i in range(1920):
        color = (40 + i//40, 40 + i//40, 60 + i//30)
        draw.line([(0, i), (1080, i)], fill=color)
    
    # Title
    draw.text((540, 250), "RACING GAME", fill=(0, 200, 255), font=font_title, anchor="mm")
    draw.text((540, 380), "Sign In / Sign Up", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    # Email field
    draw.rectangle([(100, 550), (980, 650)], outline=(0, 200, 255), width=3)
    draw.text((120, 560), "📧 Email Address", fill=(0, 200, 255), font=font_small)
    draw.text((120, 610), "player@example.com", fill=(200, 200, 200), font=font_small)
    
    # Password field
    draw.rectangle([(100, 750), (980, 850)], outline=(0, 200, 255), width=3)
    draw.text((120, 760), "🔐 Password", fill=(0, 200, 255), font=font_small)
    draw.text((120, 810), "••••••••••", fill=(200, 200, 200), font=font_small)
    
    # Login button
    draw.rectangle([(200, 1000), (880, 1150)], fill=(0, 200, 100), outline=(255, 255, 255), width=4)
    draw.text((540, 1075), "LOGIN / SIGN UP", fill=(255, 255, 255), font=font_large, anchor="mm")
    
    # Info section
    draw.rectangle([(100, 1250), (980, 1550)], fill=(50, 50, 80), outline=(0, 200, 255), width=2)
    draw.text((540, 1300), "🎮 Multi-Player Support", fill=(0, 255, 100), font=font_medium, anchor="mm")
    draw.text((540, 1380), "Track your scores", fill=(200, 200, 255), font=font_small, anchor="mm")
    draw.text((540, 1440), "Play on multiple devices", fill=(200, 200, 255), font=font_small, anchor="mm")
    draw.text((540, 1500), "Secure cloud sync (coming soon)", fill=(200, 200, 255), font=font_small, anchor="mm")
    
    img.save("assets/screenshots/04_login_screen.png")
    print("✅ Screenshot 4 saved: assets/screenshots/04_login_screen.png")


def create_feature_graphic():
    """Feature Graphic for Play Store (1024x500)."""
    print("🎨 Creating Feature Graphic...")
    img = Image.new('RGB', (1024, 500))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Gradient background
    for i in range(500):
        ratio = i / 500
        r = int(0 * (1 - ratio) + 200 * ratio)
        g = int(100 * (1 - ratio) + 50 * ratio)
        b = int(255 * (1 - ratio) + 100 * ratio)
        draw.line([(0, i), (1024, i)], fill=(r, g, b))
    
    # Left side - car
    draw.rectangle([(50, 150), (250, 380)], fill=(255, 50, 50), outline=(255, 255, 255), width=3)
    draw.rectangle([(70, 170), (230, 280)], fill=(255, 200, 0))  # Window
    
    # Right side - text
    draw.text((650, 150), "RACING", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((650, 250), "GAME", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((650, 370), "Arcade Challenge", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    # Bottom tagline
    draw.rectangle([(0, 430), (1024, 500)], fill=(0, 0, 0, 100))
    draw.text((512, 465), "Dodge Traffic • Beat Your Score", fill=(0, 255, 100), font=font_small, anchor="mm")
    
    img.save("assets/graphics/feature_graphic_1024x500.png")
    print("✅ Feature Graphic saved: assets/graphics/feature_graphic_1024x500.png")


def create_app_icon():
    """App Icon for Play Store (512x512)."""
    print("🎯 Creating App Icon...")
    img = Image.new('RGB', (512, 512), color=(0, 100, 200))
    draw = ImageDraw.Draw(img)
    
    # Background gradient
    for i in range(512):
        ratio = i / 512
        r = int(0 * (1 - ratio) + 100 * ratio)
        g = int(100 * (1 - ratio) + 150 * ratio)
        b = int(200 * (1 - ratio) + 255 * ratio)
        draw.line([(0, i), (512, i)], fill=(r, g, b))
    
    # Car body (red)
    draw.rectangle([(100, 180), (412, 300)], fill=(255, 50, 50))
    
    # Car top (red)
    draw.rectangle([(140, 100), (372, 200)], fill=(255, 50, 50))
    
    # Windows (gold)
    draw.rectangle([(160, 120), (240, 180)], fill=(255, 200, 0))
    draw.rectangle([(272, 120), (352, 180)], fill=(255, 200, 0))
    
    # Wheels
    draw.ellipse([(120, 310), (180, 370)], fill=(50, 50, 50), outline=(255, 255, 255), width=3)
    draw.ellipse([(332, 310), (392, 370)], fill=(50, 50, 50), outline=(255, 255, 255), width=3)
    
    # Speed lines (right side)
    draw.line([(420, 200), (480, 180)], fill=(255, 255, 0), width=5)
    draw.line([(420, 250), (490, 240)], fill=(255, 255, 0), width=5)
    draw.line([(420, 300), (480, 320)], fill=(255, 255, 0), width=5)
    
    # Border
    draw.rectangle([(10, 10), (502, 502)], outline=(255, 255, 255), width=5)
    
    img.save("assets/icons/app_icon_512x512.png")
    print("✅ App Icon saved: assets/icons/app_icon_512x512.png")


def create_icon_small():
    """Small App Icon (192x192)."""
    print("🎯 Creating Small App Icon...")
    img = Image.new('RGB', (192, 192), color=(0, 100, 200))
    draw = ImageDraw.Draw(img)
    
    # Background
    for i in range(192):
        ratio = i / 192
        r = int(0 * (1 - ratio) + 100 * ratio)
        g = int(100 * (1 - ratio) + 150 * ratio)
        b = int(200 * (1 - ratio) + 255 * ratio)
        draw.line([(0, i), (192, i)], fill=(r, g, b))
    
    # Simple car shape
    draw.rectangle([(40, 70), (152, 110)], fill=(255, 50, 50))
    draw.rectangle([(55, 40), (137, 80)], fill=(255, 50, 50))
    draw.rectangle([(62, 48), (90, 72)], fill=(255, 200, 0))
    draw.rectangle([(102, 48), (130, 72)], fill=(255, 200, 0))
    
    img.save("assets/icons/app_icon_192x192.png")
    print("✅ Small Icon saved: assets/icons/app_icon_192x192.png")


def main():
    """Generate all assets."""
    print("\n" + "="*70)
    print("🎮 RACING GAME - PROFESSIONAL PLAY STORE ASSET GENERATOR")
    print("="*70 + "\n")
    
    try:
        create_directory()
        print()
        
        create_screenshot_1_menu()
        create_screenshot_2_gameplay()
        create_screenshot_3_gameover()
        create_screenshot_4_login()
        create_feature_graphic()
        create_app_icon()
        create_icon_small()
        
        print("\n" + "="*70)
        print("✅ ALL ASSETS GENERATED SUCCESSFULLY!")
        print("="*70 + "\n")
        
        print("📁 Asset Files Created:\n")
        print("SCREENSHOTS (1080x1920):")
        print("  ✓ 01_menu_screen.png")
        print("  ✓ 02_gameplay_action.png")
        print("  ✓ 03_game_over.png")
        print("  ✓ 04_login_screen.png")
        print()
        print("GRAPHICS:")
        print("  ✓ feature_graphic_1024x500.png (Feature banner)")
        print()
        print("ICONS:")
        print("  ✓ app_icon_512x512.png (Google Play icon)")
        print("  ✓ app_icon_192x192.png (Notification icon)")
        print()
        
        print("📍 Location: assets/")
        print()
        print("="*70)
        print("📋 NEXT STEPS FOR PLAY STORE UPLOAD:")
        print("="*70 + "\n")
        
        print("1. Go to: https://play.google.com/console")
        print("2. Create new app")
        print("3. Upload screenshots:")
        print("   • Add all 4 screenshots (1080x1920)")
        print("   • Arrange in order: Menu → Gameplay → GameOver → Login")
        print()
        print("4. Upload feature graphic (1024x500)")
        print("5. Upload app icon (512x512)")
        print()
        print("6. Fill app description from INSTANT_UPLOAD_GUIDE.md")
        print("7. Build APK: python publish_setup.py (choose option 3)")
        print("8. Upload APK to Play Store")
        print()
        print("✅ Ready to publish in under 2 hours!")
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure Pillow is installed:")
        print("  pip install pillow")


if __name__ == "__main__":
    main()
