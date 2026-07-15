#!/usr/bin/env python3
"""
Professional Game Image & Promotional Asset Generator
Creates high-quality images for your Racing Game
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def create_directory():
    """Create directories for game images."""
    directories = [
        "assets/game_images",
        "assets/promotional",
        "assets/marketing"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def get_fonts():
    """Get fonts with fallback."""
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
    except:
        font_title = font_large = font_medium = font_small = ImageFont.load_default()
    
    return font_title, font_large, font_medium, font_small


def create_game_cover():
    """Create high-resolution game cover art (1920x1080)."""
    print("🎨 Creating Game Cover Art...")
    img = Image.new('RGB', (1920, 1080))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Gradient background (blue to purple)
    for i in range(1080):
        ratio = i / 1080
        r = int(0 * (1 - ratio) + 80 * ratio)
        g = int(100 * (1 - ratio) + 50 * ratio)
        b = int(200 * (1 - ratio) + 150 * ratio)
        draw.line([(0, i), (1920, i)], fill=(r, g, b))
    
    # Road elements on left
    draw.rectangle([(50, 300), (850, 850)], fill=(100, 100, 100))
    draw.line([(450, 300), (450, 850)], fill=(255, 255, 0), width=8)
    
    # Multiple cars racing
    colors = [(255, 50, 50), (255, 200, 0), (100, 255, 100)]
    positions = [(150, 350, 300, 500), (600, 550, 750, 700), (200, 650, 350, 800)]
    
    for (x1, y1, x2, y2), color in zip(positions, colors):
        draw.rectangle([(x1, y1), (x2, y2)], fill=color)
        draw.rectangle([(x1+30, y1+20), (x2-30, y1+60)], fill=(255, 200, 0))
    
    # Speed lines
    for i in range(5):
        y = 400 + i * 100
        draw.line([(100, y), (400, y)], fill=(255, 255, 0), width=3)
    
    # Title - left side
    draw.text((450, 200), "RACING", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((450, 350), "GAME", fill=(0, 255, 200), font=font_title, anchor="mm")
    
    # Tagline
    draw.text((450, 500), "Dodge Traffic • Beat Your Score", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    # Right side - features
    features_x = 1200
    features_y = 300
    draw.text((features_x, features_y), "Features:", fill=(255, 255, 255), font=font_large, anchor="lm")
    
    features = [
        "✓ Arcade Gameplay",
        "✓ User Profiles",
        "✓ High Scores",
        "✓ NO Ads"
    ]
    
    y = features_y + 120
    for feature in features:
        draw.text((features_x, y), feature, fill=(0, 255, 200), font=font_medium, anchor="lm")
        y += 100
    
    # Download button area
    draw.rectangle([(1000, 800), (1850, 950)], fill=(0, 200, 100), outline=(255, 255, 255), width=5)
    draw.text((1425, 875), "DOWNLOAD NOW", fill=(255, 255, 255), font=font_large, anchor="mm")
    
    img.save("assets/game_images/racing_game_cover_1920x1080.png")
    print("✅ Game Cover saved: assets/game_images/racing_game_cover_1920x1080.png")


def create_banner_horizontal():
    """Create horizontal banner (2560x1440)."""
    print("🎨 Creating Horizontal Banner...")
    img = Image.new('RGB', (2560, 1440))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Background with gradient
    for i in range(1440):
        ratio = i / 1440
        r = int(20 * (1 - ratio) + 100 * ratio)
        g = int(20 * (1 - ratio) + 50 * ratio)
        b = int(40 * (1 - ratio) + 150 * ratio)
        draw.line([(0, i), (2560, i)], fill=(r, g, b))
    
    # Left side - game title
    draw.text((400, 720), "RACING GAME", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((400, 950), "Arcade Challenge", fill=(0, 255, 200), font=font_large, anchor="mm")
    
    # Center - car graphic with motion
    draw.rectangle([(900, 500), (1300, 800)], fill=(255, 50, 50))
    draw.rectangle([(950, 550), (1250, 680)], fill=(255, 200, 0))
    
    # Speed effect
    draw.line([(1350, 550), (1550, 500)], fill=(255, 255, 0), width=8)
    draw.line([(1350, 620), (1600, 620)], fill=(255, 255, 0), width=8)
    draw.line([(1350, 690), (1550, 750)], fill=(255, 255, 0), width=8)
    
    # Right side - features
    features_x = 1850
    features_y = 500
    
    features_text = [
        "• Smooth Controls",
        "• Progressive Difficulty",
        "• Track High Scores",
        "• Multi-Player Support",
        "• NO In-App Purchases"
    ]
    
    y = features_y
    for feature in features_text:
        draw.text((features_x, y), feature, fill=(255, 255, 255), font=font_medium, anchor="lm")
        y += 140
    
    # Call to action
    draw.rectangle([(1700, 1100), (2400, 1300)], fill=(0, 255, 100), outline=(255, 255, 255), width=5)
    draw.text((2050, 1200), "PLAY NOW", fill=(255, 255, 255), font=font_large, anchor="mm")
    
    img.save("assets/game_images/racing_game_banner_2560x1440.png")
    print("✅ Horizontal Banner saved: assets/game_images/racing_game_banner_2560x1440.png")


def create_portrait_poster():
    """Create vertical poster (1080x1920)."""
    print("🎨 Creating Vertical Poster...")
    img = Image.new('RGB', (1080, 1920))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Gradient background
    for i in range(1920):
        ratio = i / 1920
        r = int(0 * (1 - ratio) + 100 * ratio)
        g = int(100 * (1 - ratio) + 50 * ratio)
        b = int(200 * (1 - ratio) + 150 * ratio)
        draw.line([(0, i), (1080, i)], fill=(r, g, b))
    
    # Top - Game Title
    draw.text((540, 150), "RACING", fill=(255, 255, 255), font=font_title, anchor="mm")
    draw.text((540, 300), "GAME", fill=(0, 255, 200), font=font_title, anchor="mm")
    
    # Car in center
    draw.rectangle([(250, 500), (830, 750)], fill=(255, 50, 50))
    draw.rectangle([(300, 550), (780, 700)], fill=(255, 200, 0))
    draw.circle((330, 780), 50, fill=(50, 50, 50))
    draw.circle((750, 780), 50, fill=(50, 50, 50))
    
    # Speed lines
    for i in range(6):
        x_start = 150
        x_end = 400
        y = 550 + i * 30
        draw.line([(x_start, y), (x_end, y)], fill=(255, 255, 0), width=2)
    
    # Tagline
    draw.text((540, 900), "Dodge Traffic", fill=(255, 200, 0), font=font_large, anchor="mm")
    draw.text((540, 1000), "Beat Your Score", fill=(255, 200, 0), font=font_large, anchor="mm")
    
    # Features section
    draw.text((540, 1150), "Features:", fill=(0, 255, 200), font=font_medium, anchor="mm")
    
    features = [
        "✓ Arcade Gameplay",
        "✓ User Authentication",
        "✓ High Score Tracking",
        "✓ Multi-User Support"
    ]
    
    y = 1250
    for feature in features:
        draw.text((540, y), feature, fill=(255, 255, 255), font=font_small, anchor="mm")
        y += 120
    
    # Bottom - rating and stats
    draw.rectangle([(100, 1650), (980, 1850)], fill=(50, 50, 100), outline=(0, 255, 200), width=3)
    draw.text((540, 1700), "⭐⭐⭐⭐⭐ 4.8 Rating", fill=(255, 255, 0), font=font_medium, anchor="mm")
    draw.text((540, 1800), "Download on Google Play", fill=(0, 255, 200), font=font_small, anchor="mm")
    
    img.save("assets/game_images/racing_game_poster_1080x1920.png")
    print("✅ Vertical Poster saved: assets/game_images/racing_game_poster_1080x1920.png")


def create_social_media_image():
    """Create social media post image (1200x628)."""
    print("🎨 Creating Social Media Image...")
    img = Image.new('RGB', (1200, 628))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Split background - left and right
    draw.rectangle([(0, 0), (600, 628)], fill=(0, 100, 200))
    draw.rectangle([(600, 0), (1200, 628)], fill=(200, 100, 0))
    
    # Left - game title and car
    draw.text((300, 150), "RACING", fill=(255, 255, 255), font=font_large, anchor="mm")
    draw.text((300, 250), "GAME", fill=(0, 255, 200), font=font_large, anchor="mm")
    
    # Car graphic
    draw.rectangle([(100, 350), (400, 500)], fill=(255, 50, 50))
    draw.rectangle([(130, 380), (370, 450)], fill=(255, 200, 0))
    
    # Right - text
    draw.text((900, 200), "NOW LIVE!", fill=(255, 255, 255), font=font_large, anchor="mm")
    draw.text((900, 320), "Google Play Store", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    features_text = "Download Now\nFree • No Ads\nArcade Fun!"
    y = 420
    for line in features_text.split('\n'):
        draw.text((900, y), line, fill=(255, 255, 255), font=font_small, anchor="mm")
        y += 60
    
    img.save("assets/promotional/racing_game_social_1200x628.png")
    print("✅ Social Media Image saved: assets/promotional/racing_game_social_1200x628.png")


def create_thumbnail():
    """Create YouTube thumbnail (1280x720)."""
    print("🎨 Creating YouTube Thumbnail...")
    img = Image.new('RGB', (1280, 720))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Background with contrasting colors
    draw.rectangle([(0, 0), (640, 720)], fill=(255, 50, 50))
    draw.rectangle([(640, 0), (1280, 720)], fill=(0, 100, 255))
    
    # Large "RACING" text
    draw.text((320, 200), "RACING", fill=(255, 255, 0), font=font_title, anchor="mm")
    draw.text((320, 350), "GAME", fill=(255, 255, 0), font=font_title, anchor="mm")
    
    # Big number or badge
    draw.ellipse([(1050, 50), (1230, 230)], fill=(255, 200, 0), outline=(255, 255, 255), width=5)
    draw.text((1140, 140), "NEW", fill=(255, 50, 50), font=font_large, anchor="mm")
    
    # Small cars at bottom
    draw.rectangle([(50, 550), (250, 680)], fill=(100, 255, 100))
    draw.rectangle([(350, 550), (550, 680)], fill=(255, 255, 100))
    draw.rectangle([(650, 550), (850, 680)], fill=(200, 100, 255))
    
    # Text at bottom
    draw.text((640, 500), "DOWNLOAD NOW!", fill=(255, 255, 255), font=font_medium, anchor="mm")
    
    img.save("assets/promotional/racing_game_youtube_1280x720.png")
    print("✅ YouTube Thumbnail saved: assets/promotional/racing_game_youtube_1280x720.png")


def create_loading_screen():
    """Create in-game loading screen (1080x1920)."""
    print("🎨 Creating Loading Screen...")
    img = Image.new('RGB', (1080, 1920))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Gradient background
    for i in range(1920):
        ratio = i / 1920
        r = int(20 * (1 - ratio) + 100 * ratio)
        g = int(20 * (1 - ratio) + 50 * ratio)
        b = int(40 * (1 - ratio) + 150 * ratio)
        draw.line([(0, i), (1080, i)], fill=(r, g, b))
    
    # Logo/title
    draw.text((540, 400), "RACING GAME", fill=(255, 255, 255), font=font_title, anchor="mm")
    
    # Loading car animation
    draw.rectangle([(200, 800), (880, 950)], fill=(100, 100, 100), outline=(255, 255, 255), width=3)
    draw.rectangle([(250, 820), (850, 930)], fill=(50, 50, 50))
    
    # Progress bar filled 75%
    draw.rectangle([(250, 820), (712, 930)], fill=(0, 255, 100))
    
    # Loading text
    draw.text((540, 1100), "Loading...", fill=(0, 255, 100), font=font_large, anchor="mm")
    draw.text((540, 1200), "Get ready to race!", fill=(255, 200, 0), font=font_medium, anchor="mm")
    
    # Tips
    draw.text((540, 1500), "Tip: Use Arrow Keys to move", fill=(200, 200, 255), font=font_small, anchor="mm")
    draw.text((540, 1600), "Avoid traffic and survive as long as possible!", fill=(200, 200, 255), font=font_small, anchor="mm")
    
    # Version info
    draw.text((540, 1800), "v1.0 | Arcade Racing Game", fill=(150, 150, 150), font=font_small, anchor="mm")
    
    img.save("assets/game_images/racing_game_loading_screen.png")
    print("✅ Loading Screen saved: assets/game_images/racing_game_loading_screen.png")


def create_marketing_flyer():
    """Create marketing flyer (2550x3300)."""
    print("🎨 Creating Marketing Flyer...")
    img = Image.new('RGB', (2550, 3300))
    draw = ImageDraw.Draw(img)
    font_title, font_large, font_medium, font_small = get_fonts()
    
    # Header
    draw.rectangle([(0, 0), (2550, 600)], fill=(0, 100, 200))
    draw.text((1275, 300), "RACING GAME", fill=(255, 255, 255), font=font_title, anchor="mm")
    
    # Main visual
    draw.rectangle([(300, 700), (2250, 1800)], fill=(100, 100, 100))
    draw.rectangle([(500, 800), (2050, 1700)], fill=(128, 128, 128))
    
    # Multiple cars
    colors = [(255, 50, 50), (255, 200, 0), (100, 255, 100)]
    for i, color in enumerate(colors):
        x = 600 + i * 500
        draw.rectangle([(x, 1000), (x+200, 1400)], fill=color)
        draw.rectangle([(x+20, 1050), (x+180, 1150)], fill=(255, 200, 0))
    
    # Features section
    features_y = 2000
    draw.text((1275, features_y), "FEATURES", fill=(0, 100, 200), font=font_large, anchor="mm")
    
    features = [
        "Smooth, Responsive Controls",
        "Progressive Difficulty Levels",
        "Track Your High Scores",
        "Multi-Player Support",
        "NO Ads • NO In-App Purchases"
    ]
    
    y = features_y + 200
    for feature in features:
        draw.text((1275, y), feature, fill=(0, 0, 0), font=font_medium, anchor="mm")
        y += 200
    
    # Download section
    draw.rectangle([(300, 2900), (2250, 3200)], fill=(0, 255, 100), outline=(0, 0, 0), width=5)
    draw.text((1275, 3050), "DOWNLOAD ON GOOGLE PLAY", fill=(0, 0, 0), font=font_large, anchor="mm")
    
    img.save("assets/promotional/racing_game_flyer_2550x3300.png")
    print("✅ Marketing Flyer saved: assets/promotional/racing_game_flyer_2550x3300.png")


def main():
    """Generate all game images."""
    print("\n" + "="*70)
    print("🎨 RACING GAME - PROFESSIONAL IMAGE GENERATOR")
    print("="*70 + "\n")
    
    try:
        create_directory()
        print()
        
        create_game_cover()
        create_banner_horizontal()
        create_portrait_poster()
        create_social_media_image()
        create_thumbnail()
        create_loading_screen()
        create_marketing_flyer()
        
        print("\n" + "="*70)
        print("✅ ALL GAME IMAGES CREATED SUCCESSFULLY!")
        print("="*70 + "\n")
        
        print("📁 Game Images Created:\n")
        
        print("GAME GRAPHICS:")
        print("  ✓ racing_game_cover_1920x1080.png")
        print("  ✓ racing_game_banner_2560x1440.png")
        print("  ✓ racing_game_poster_1080x1920.png")
        print("  ✓ racing_game_loading_screen.png")
        print()
        
        print("PROMOTIONAL:")
        print("  ✓ racing_game_social_1200x628.png (Facebook/Twitter)")
        print("  ✓ racing_game_youtube_1280x720.png (YouTube Thumbnail)")
        print("  ✓ racing_game_flyer_2550x3300.png (Print Flyer)")
        print()
        
        print("📍 Location: assets/game_images/ & assets/promotional/")
        print()
        
        print("="*70)
        print("🎯 USE CASES:")
        print("="*70 + "\n")
        
        print("Game Screens:")
        print("  • Use cover_1920x1080 for game launch screen")
        print("  • Use loading_screen for in-game loading")
        print()
        
        print("Marketing & Promotion:")
        print("  • Use social_1200x628 for Facebook/Twitter posts")
        print("  • Use youtube_1280x720 for YouTube thumbnail")
        print("  • Use banner_2560x1440 for website headers")
        print("  • Use flyer for print materials")
        print()
        
        print("Play Store:")
        print("  • Use poster_1080x1920 as feature graphic")
        print("  • Use cover as app preview")
        print()
        
        print("="*70)
        print("📱 Ready for Marketing!")
        print("="*70 + "\n")
        
        print("Next Steps:")
        print("1. Use these images for your marketing campaign")
        print("2. Post on social media with hashtags:")
        print("   #RacingGame #MobileGaming #GooglePlay #ArcadeGame")
        print("3. Share with friends and family!")
        print("4. Use in your press releases")
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure Pillow is installed:")
        print("  pip install pillow")


if __name__ == "__main__":
    main()
