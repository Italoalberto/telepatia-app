# Medical Assistant App (Firebase + Streamlit) — Secrets Fix

### Secrets (NEW way)
```
cd functions
npm install
firebase use telepatia-app
firebase functions:secrets:set OPENAI_API_KEY
```
No code, the secret is declared via:
```
import { defineSecret } from "firebase-functions/params";
const OPENAI_API_KEY = defineSecret("OPENAI_API_KEY");
export const myFn = functions.runWith({ secrets: [OPENAI_API_KEY] }).https.onRequest(...)
```
and used with `OPENAI_API_KEY.value()`.

### Build & Deploy
```
npm run build
firebase deploy --only functions
```

### Streamlit
```
cd ..
pip install -r requirements.txt
streamlit run streamlit_app.py
```
