# Digital Productivity Index — Streamlit Dummy Prototype

This is a small demonstration app to test the Streamlit interface and deployment workflow.

## What it does
- Shows seven proposed digital work habit dimensions.
- Accepts 1–5 demo ratings.
- Calculates an illustrative 0–100 score and dimension scores after submission.
- Shows example strengths and improvement suggestions.
- Does **not** save responses or collect identifying information.

The scoring method and recommendations are placeholders only. Do not use this demo as the final research instrument or circulate it as a validated DPI.

## Run locally
1. Install Python.
2. Open a terminal in this folder.
3. Run:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Deploy to a public Streamlit URL
1. Create or sign in to GitHub.
2. Create a new repository, for example `dpi-streamlit-demo`.
3. Upload `app.py`, `requirements.txt`, and this `README.md`.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Choose **Create app**, select the repository, branch, and `app.py`.
6. Click **Deploy**. Streamlit Community Cloud will provide a URL ending in `streamlit.app`.
7. Open the URL in a private/incognito browser window to test the public view.

A GitHub account and your authorization to deploy are required; this project bundle does not create or host a public URL by itself.
