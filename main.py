from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routers import projects, auth_router

# -----------------------------------
# ⭐ API METADATA (Swagger UI)
# -----------------------------------
app = FastAPI(
    title="Simran's Portfolio Backend API",
    description="""
This API powers Simran’s Full-Stack Portfolio.

### Features:
- 🌟 Beautiful Home Page
- 🔐 Admin Login (JWT)
- 📁 Projects API
- ⚙ CRUD API Ready
""",
    version="1.0.5"
)

# -----------------------------------
# ⭐ HOME PAGE (YOUR COLORED PAGE STAYS SAME)
# -----------------------------------
@app.get("/", response_class=HTMLResponse, tags=["Home"], summary="Simran’s Portfolio Home Page")
def home():
    return """
    <html>
    <head>
        <title>Simran Portfolio</title>

        <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #fef9f3, #ffe0f0);
        color: #4a275f;  /* deep purple text */
        overflow-x: hidden;
        position: relative;
    }

    /* Floating Shapes Background */
    .shape {
        position: absolute;
        border-radius: 50%;
        background: rgba(200, 140, 255, 0.20);
        animation: float 6s infinite ease-in-out;
    }
    .shape1 { width: 130px; height: 130px; top: 10%; left: 15%; background: rgba(255,182,193,0.35); }
    .shape2 { width: 210px; height: 210px; top: 65%; left: 72%; background: rgba(186,232,255,0.35); }
    .shape3 { width: 90px; height: 90px; top: 40%; left: 38%; background: rgba(255,200,255,0.30); }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-35px); }
        100% { transform: translateY(0px); }
    }

    /* Typewriter Animation */
    .typewriter {
        font-size: 42px;
        font-weight: bold;
        white-space: nowrap;
        overflow: hidden;
        border-right: 4px solid #b30086;
        width: 0;
        animation: typing 4s steps(25) forwards, blink 0.7s infinite;
        color: #b30086;
    }
    @keyframes typing { from { width: 0; } to { width: 430px; } }
    @keyframes blink { 50% { border-color: transparent; } }

    /* Glow */
    .glow {
        box-shadow: 0 0 10px #ffb3d9,
                    0 0 20px #ffb3d9,
                    0 0 40px #ff80bf;
    }

    /* Profile Image */
    .profile {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 4px solid #d63384;
        margin-bottom: 15px;
        box-shadow: 0 0 18px #ff80bf;
    }

    .btn {
        padding: 12px 25px;
        margin: 10px;
        background: white;
        border: 2px solid #d63384;
        color: #d63384;
        border-radius: 8px;
        cursor: pointer;
        font-size: 18px;
        transition: 0.3s;
        box-shadow: 0 0 10px #ffb3d9;
    }
    .btn:hover {
        background: #ffedf7;
        transform: scale(1.05);
        box-shadow: 0 0 18px #ff80bf;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        width: 60%;
        margin: 20px auto;
        border: 2px solid #ffb3d9;
        box-shadow: 0 0 15px #ffd6e9;
        cursor: pointer;
    }

    h2 {
        color: #b30086;
        text-shadow: 0 0 8px #ffd6e9;
    }

    /* Social Icons */
    .social-icons a {
        margin: 10px;
        font-size: 30px;
        color: #b30086;
        text-decoration: none;
        transition: 0.3s;
    }
    .social-icons a:hover {
        color: #ff1493;
        text-shadow: 0 0 12px #ff80bf;
    }

    /* MODAL POPUP */
    .modal {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(8px);
        background: rgba(0,0,0,0.4);
    }

    .modal-content {
        background: white;
        padding: 25px;
        border-radius: 15px;
        width: 50%;
        margin: 10% auto;
        border: 2px solid #ffb3d9;
        color: #4a275f;
        animation: popup 0.4s ease;
        box-shadow: 0 0 25px #ff80bf;
    }

    @keyframes popup {
        from { transform: scale(0.6); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    .close {
        float: right;
        cursor: pointer;
        font-size: 24px;
        color: #b30086;
    }
    .close:hover { color: #ff1493; }
</style>

    </head>

    <body>

        <!-- FLOATING SHAPES -->
        <div class="shape shape1"></div>
        <div class="shape shape2"></div>
        <div class="shape shape3"></div>

        <!-- HERO SECTION -->
        <div class="section">
            <img class="profile" src="https://i.postimg.cc/Kc8xQH0B/profile.jpg" />

            <div class="typewriter">Simran Jamakhandi</div>

            <p>Machine Learning • Deep Learning • Full Stack Developer</p>

            <!-- SOCIAL -->
            <div class="social-icons">
                <a href="https://instagram.com/" target="_blank">📷</a>
                <a href="https://github.com/" target="_blank">💻</a>
                <a href="https://linkedin.com/" target="_blank">🔗</a>
            </div>

            <button class="btn" onclick="scrollToSection('projects')">Projects</button>
            <button class="btn" onclick="scrollToSection('skills')">Skills</button>
            <button class="btn" onclick="scrollToSection('about')">About</button>

            <a href="https://your-resume-link.com" download>
                <button class="btn">📄 Download Resume</button>
            </a>

            

        </div>

        <!-- PROJECTS -->
<div id="projects" class="section">
    <h2>🚀 My Projects</h2>

    <div class="card" onclick="openModal('sar')">
        <h3>🛰 SAR Image Colorization using Deep Learning</h3>
        <p>GAN • Deep Learning</p>
    </div>

    <div class="card" onclick="openModal('sugarcane')">
        <h3>🍃 Sugarcane Leaf Disease Detection</h3>
        <p>CNN • Real-time Plant Health Monitoring</p>
    </div>

    <div class="card" onclick="openModal('water')">
        <h3>💧 Water Quality Monitoring System</h3>
        <p>ML • IoT • Grey Water Analysis</p>
    </div>

    <div class="card" onclick="openModal('powerbi')">
        <h3>📊 Meta Ads Performance Dashboard (Power BI)</h3>
        <p>Business Analytics • Data Visualization</p>
    </div>
</div>


        <!-- MODAL -->
        <div id="modal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal()">✖</span>
                <h2 id="modal-title"></h2>
                <p id="modal-text"></p>
            </div>
        </div>

        <!-- SKILLS -->
        <div id="skills" class="section">
            <h2>💡 Skills</h2>
            <div class="card">
                Python • FastAPI • React • ML • CNN • SQL • Docker • Data Engineering
            </div>
        </div>

        <!-- ABOUT -->
        <div id="about" class="section">
            <h2>👩‍💻 About Me</h2>
            <div class="card">
                Hi, I’m Simran Jamakhandi — an AI/ML Engineer and Software Developer passionate about building intelligent, scalable, and real-world solutions. I specialize in developing high-performance machine learning models for NLP, computer vision, and real-time systems, and I enjoy turning ideas into practical applications using Python, TensorFlow, FastAPI, and modern ML tools.

With a strong foundation in OOP, data structures, backend development, and model deployment, I create systems that are not only accurate but also production-ready. I’m currently pursuing a B.E. in AI & ML at Bangalore Institute of Technology and have previously completed a Diploma in Computer Science. My work spans across impactful domains like plant disease detection, breast cancer prediction, activity detection, and water quality testing, blending technology with problem-solving.

I love exploring new technologies, experimenting with ML models, and building full-stack projects that make a difference
            </div>
        </div>

        <script>
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

function openModal(project) {
    const modal = document.getElementById('modal');
    const title = document.getElementById('modal-title');
    const text = document.getElementById('modal-text');

    let githubLink = "https://github.com/Flow12345-SS";

    if (project === "sar") {
        title.innerHTML = "🛰 SAR Image Colorization using Deep Learning";
        text.innerHTML = "Developed a deep learning model to convert grayscale SAR satellite images into realistic RGB colorized versions using GANs. Enhances terrain interpretation, boosts remote sensing analysis accuracy, and improves visualization for defense & environmental monitoring.";
    }

    if (project === "sugarcane") {
        title.innerHTML = "🍃 Sugarcane Leaf Disease Detection";
        text.innerHTML = "Built a CNN-based vision model to detect major sugarcane leaf diseases from images with high accuracy. Helps farmers identify diseases early through automated plant health analysis using deep learning.";
    }

    if (project === "water") {
        title.innerHTML = "💧 Water Quality Monitoring System";
        text.innerHTML = "Created a smart IoT + ML system to monitor microbial and chemical contamination in water. Used low-cost sensors and trained ML models to detect water quality issues for rural and grey-water applications.";
    }

    if (project === "powerbi") {
        title.innerHTML = "📊 Meta Ads Performance Dashboard (Power BI)";
        text.innerHTML = "Designed an interactive Power BI dashboard to track ad spending, conversions, ROI, and audience performance across Meta platforms. Provides insights for marketing optimization and decision-making.";
    }

    // Add GitHub Button to modal
    text.innerHTML += `
        <br><br>
        <a href="${githubLink}" target="_blank"
           style="display:inline-block; padding:10px 18px;
                  background:#d63384; color:white; border-radius:8px;
                  text-decoration:none; font-weight:bold;">
            🔗 View on GitHub
        </a>
    `;

    modal.style.display = "block";
}

function closeModal() {
    document.getElementById('modal').style.display = "none";
}
</script>



    </body>
    </html>
    """
