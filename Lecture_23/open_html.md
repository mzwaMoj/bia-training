# How to open the ML Math Lab (HTML lesson)

The lesson is a single file: **`S18_ML_Workflow_Interactive_Lesson.html`**.
It runs entirely in your browser. You don't need an internet connection, Python packages or an install.

---

## Option 1: Double-click (easiest)

1. Open the folder `01_ML WORKFLOW, DATA PREPARATION & VALIDATION`.
2. Double-click `S18_ML_Workflow_Interactive_Lesson.html`.

It opens in your default browser. Chrome, Edge, Safari and Firefox all work.

---

## Option 2: From the terminal

> The folder name contains spaces, so keep the **quotes** around paths.

### macOS (Terminal)

```bash
# 1. Go to the lesson folder (adjust the path to where you saved the course)
cd ~/"Developer/bia-training/Lecture_20/01_ML WORKFLOW, DATA PREPARATION & VALIDATION"

# 2. Open in your default browser
open S18_ML_Workflow_Interactive_Lesson.html

# ...or choose a browser
open -a "Google Chrome" S18_ML_Workflow_Interactive_Lesson.html
open -a Safari S18_ML_Workflow_Interactive_Lesson.html
```

### Windows: Command Prompt (cmd)

```bat
:: 1. Go to the lesson folder (adjust the path to where you saved the course)
cd /d "C:\Users\<your-name>\bia-training\Lecture_20\01_ML WORKFLOW, DATA PREPARATION & VALIDATION"

:: 2. Open in your default browser
start "" "S18_ML_Workflow_Interactive_Lesson.html"

:: ...or choose a browser
start chrome "%cd%\S18_ML_Workflow_Interactive_Lesson.html"
start msedge "%cd%\S18_ML_Workflow_Interactive_Lesson.html"
```

### Windows: PowerShell

```powershell
# 1. Go to the lesson folder
cd "C:\Users\<your-name>\bia-training\Lecture_20\01_ML WORKFLOW, DATA PREPARATION & VALIDATION"

# 2. Open in your default browser
Start-Process .\S18_ML_Workflow_Interactive_Lesson.html

# ...or choose a browser
Start-Process chrome (Resolve-Path .\S18_ML_Workflow_Interactive_Lesson.html)
Start-Process msedge (Resolve-Path .\S18_ML_Workflow_Interactive_Lesson.html)
```

---

## Option 3: Share it on your network (trainer)

Use this when students should open the lesson from **their own devices** on the same Wi-Fi.
It needs Python, which you already have for the notebooks.

**macOS**

```bash
cd ~/"Developer/bia-training/Lecture_20/01_ML WORKFLOW, DATA PREPARATION & VALIDATION"
python3 -m http.server 8000
```

**Windows**

```bat
cd /d "C:\Users\<your-name>\bia-training\Lecture_20\01_ML WORKFLOW, DATA PREPARATION & VALIDATION"
python -m http.server 8000
```

(If `python` isn't found on Windows, try `py -m http.server 8000`.)

Then open the lesson in a browser:

| Who | Address |
|---|---|
| You (same computer) | `http://localhost:8000/S18_ML_Workflow_Interactive_Lesson.html` |
| Students (same Wi-Fi) | `http://<your-IP>:8000/S18_ML_Workflow_Interactive_Lesson.html` |

To find your IP address:

- **macOS:** `ipconfig getifaddr en0`
- **Windows:** `ipconfig`, then use the **IPv4 Address** line (e.g. `192.168.1.25`)

Press **Ctrl + C** in the terminal to stop the server.
On Windows, allow Python through the firewall if a pop-up asks.

---

## Good to know

- **The page keeps changing when I save my notebook.** You're probably viewing it through a *live-reload* tool (VS Code "Live Server" / "Live Preview"). These reload the page whenever any file in the folder is saved. Open it with Option 1 or 2 instead, and it only reloads when you press **Ctrl + R** (Windows) or **⌘ + R** (Mac).
- **Your progress** (XP, completed topics, checklist ticks, best quiz score) is saved **in your browser on this computer**. Using another browser, a private/incognito window, or another device starts fresh.
- **Light / dark theme:** use the ◐ button in the top-right corner.
