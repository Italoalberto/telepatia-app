import { onRequest } from "firebase-functions/v2/https";
import { defineSecret } from "firebase-functions/params";
import OpenAI from "openai";

const OPENAI_API_KEY = defineSecret("OPENAI_API_KEY");
function buildOpenAI() {
  return new OpenAI({ apiKey: OPENAI_API_KEY.value() });
}

export const extract_medical_info = onRequest(
  { secrets: [OPENAI_API_KEY] },
  async (req: any, res: any) => {
    try {
      const { text } = req.body || {};
      if (!text) {
        res.status(400).json({ error: "Missing text input" });
        return;
      }

      const prompt = [
        "Extract structured medical info from this consultation text.",
        "Return ONLY a valid JSON with the following schema:",
        "{",
        '  "symptoms": [string],',
        '  "patient": { "name": string, "age": number, "id": string },',
        '  "reason_for_consultation": string',
        "}",
        "",
        "Text: " + text,
      ].join("\n");

      const openai = buildOpenAI();
      const completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: prompt }],
        temperature: 0,
      });

      const content = completion.choices[0].message?.content || "{}";
      const parsed = JSON.parse(content);
      res.json(parsed);
    } catch (e: any) {
      res.status(500).json({ error: e.message || String(e) });
    }
  }
);
